from models.models import Professional_Profile, Professional_Profile_Spanish
from schemas.schemas import Professional_Profile_Schemas
from fastapi.responses import JSONResponse
from fastapi import HTTPException


# SERVICE ACADEMY PROFILE
class Professional_Profile():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE
    def create_professional_profile(self, professional_profile_schema: Professional_Profile_Schemas):
        try:
            data = Professional_Profile(**professional_profile_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    # GET UPDATE
    def get_professional_profile(self):
        try:
            data = self.db.query(Professional_Profile).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE
    def update_professional_profile(self, id: int, professional_profile_schema: Professional_Profile_Schemas):
        try:
            data = self.db.query(Professional_Profile).filter(Professional_Profile.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.title =professional_profile_schema.title
            data.date =  professional_profile_schema.date
            data.description= professional_profile_schema.description
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)

    
    # DELETE SERVICE
    def delete_professional_profile(self, id: int):
        try:
            data = self.db.query(Professional_Profile).filter(Professional_Profile.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)
        


# SERVICE ACADEMY PROFILE SPANISH
class Professional_Profile_Spanish():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE SPANISH
    def create_professional_profile(self, professional_profile_schema: Professional_Profile_Schemas):
        try:
            data = Professional_Profile_Spanish(**professional_profile_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    # GET UPDATE SPANISH
    def get_professional_profile(self):
        try:
            data = self.db.query(Professional_Profile_Spanish).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE SPANISH
    def update_professional_profile(self, id: int, professional_profile_schema: Professional_Profile_Schemas):
        try:
            data = self.db.query(Professional_Profile_Spanish).filter(Professional_Profile_Spanish.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.title = professional_profile_schema.title
            data.date = professional_profile_schema.date
            data.description = professional_profile_schema.description
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)

    
    # DELETE SERVICE SPANISH
    def delete_professional_profile(self, id: int):
        try:
            data = self.db.query(Professional_Profile_Spanish).filter(Professional_Profile_Spanish.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)

