from models.models import Academy_Profile, Academy_Profile_Spanish
from schemas.schemas import Academy_Profile_Schemas
from fastapi.responses import JSONResponse
from fastapi import HTTPException


# SERVICE ACADEMY PROFILE
class Academy_Profile():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE
    def create_academy_profile(self, academy_profile_schema: Academy_Profile_Schemas):
        try:
            data = Academy_Profile(**academy_profile_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    # GET UPDATE
    def get_academy_profile(self):
        try:
            data = self.db.query(Academy_Profile).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE
    def update_academy_profile(self, id: int, academy_profile_schema: Academy_Profile_Schemas):
        try:
            data = self.db.query(Academy_Profile).filter(Academy_Profile.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.title = academy_profile_schema.title
            data.description =  academy_profile_schema.description
            data.status = academy_profile_schema.status
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)

    
    # DELETE SERVICE
    def delete_academy_profile(self, id: int):
        try:
            data = self.db.query(Academy_Profile).filter(Academy_Profile.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)
        


# SERVICE ACADEMY PROFILE SPANISH
class Academy_Profile_Spanish():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE SPANISH
    def create_academy_profile(self, academy_profile_schema: Academy_Profile_Schemas):
        try:
            data = Academy_Profile_Spanish(**academy_profile_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    # GET UPDATE SPANISH
    def get_academy_profile(self):
        try:
            data = self.db.query(Academy_Profile_Spanish).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE SPANISH
    def update_academy_profile(self, id: int, academy_profile_schema: Academy_Profile_Schemas):
        try:
            data = self.db.query(Academy_Profile_Spanish).filter(Academy_Profile_Spanish.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.title = academy_profile_schema.title
            data.description =  academy_profile_schema.description
            data.status = academy_profile_schema.status
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)

    
    # DELETE SERVICE SPANISH
    def delete_academy_profile(self, id: int):
        try:
            data = self.db.query(Academy_Profile_Spanish).filter(Academy_Profile_Spanish.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)



    