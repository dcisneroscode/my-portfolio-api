from models.models import User
from schemas.schemas import User_Schemas
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from tokens.encrypt_password import hash_password




class User():
    
    def __init__(self, db):
        self.db = db

    def create_user(self, user_schema: User_Schemas):
        try:
            data = User(**user_schema.model_dump())
            encryption = hash_password(data.password)
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)


    def get_user(self):
        try:
            data = self.db.query(User).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    
    def get_update(self, id: int, user_schema: User_Schemas):
        try:
            data = self.db.query(User).filter(User.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.username = user_schema.username
            data.password = hash_password(user_schema.password)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    
    def delete_update(self, id: int):
        try:
            data = self.db.query(User).filter(User.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)
    
        

    
 