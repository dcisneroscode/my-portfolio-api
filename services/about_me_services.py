from models.models import About_Me, About_Me_Spanish
from schemas.schemas import About_Me_Schema
from fastapi.responses import JSONResponse
from fastapi import HTTPException


# SERVICE ABOUT ME 
class About_Me():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE
    def create_about_me(self, about_me_schema: About_Me_Schema):
        try:
            data = About_Me(**about_me_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # GET ALL SERVICE
    def get_about_me(self):
        try:
            data = self.db.query(About_Me).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE
    def update_about_me(self, id: int, about_me_schema: About_Me_Schema):
        try:
            data = self.db.query(About_Me).filter(About_Me.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.about_me = about_me_schema.about_me
            data.front_end = about_me_schema.front_end
            data.back_end = about_me_schema.back_end
            data.responsive_design = about_me_schema.responsive_design
            data.it_security = about_me_schema.it_security
            data.cover_letter = about_me_schema.cover_letter
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)


    # DELETE SERVICE
    def delete_about_me(self, id: int):
        try:
            data = self.db.query(About_Me).filter(About_Me.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)



# SERVICE ABOUT ME SPANISH
class About_Me_Spanish():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE SPANISH
    def create_about_me(self, about_me_schema: About_Me_Schema):
        try:
            data = About_Me_Spanish(**about_me_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # GET ALL SERVICE SPANISH
    def get_about_me(self):
        try:
            data = self.db.query(About_Me_Spanish).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE SPANISH
    def update_about_me(self, id: int, about_me_schema: About_Me_Schema):
        try:
            data = self.db.query(About_Me_Spanish).filter(About_Me_Spanish.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.about_me = about_me_schema.about_me
            data.front_end = about_me_schema.front_end
            data.back_end = about_me_schema.back_end
            data.responsive_design = about_me_schema.responsive_design
            data.it_security = about_me_schema.it_security
            data.cover_letter = about_me_schema.cover_letter
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)


    # DELETE SERVICE SPANISH
    def delete_about_me(self, id: int):
        try:
            data = self.db.query(About_Me_Spanish).filter(About_Me_Spanish.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)

