from models.models import Certificate, Certificate_Spanish
from schemas.schemas import Certificate_Schemas
from fastapi.responses import JSONResponse
from fastapi import HTTPException

# SERVICE ACADEMY PROFILE
class Certificate():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE
    def create_certificate(self, certificate_schema: Certificate_Schemas):
        try:
            data = Certificate(**certificate_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    # GET UPDATE
    def get_certificate(self):
        try:
            data = self.db.query(Certificate).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE
    def update_certificate(self, id: int, certificate_schema: Certificate_Schemas):
        try:
            data = self.db.query(Certificate).filter(Certificate.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.academy = certificate_schema.academy
            data.title =  certificate_schema.title
            data.url_certificate = certificate_schema.url_certificate
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)

    
    # DELETE SERVICE
    def delete_certificate(self, id: int):
        try:
            data = self.db.query(Certificate).filter(Certificate.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)
        


# SERVICE ACADEMY PROFILE SPANISH
class Certificate_Spanish():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE SPANISH
    def create_certificate(self, certificate_schema: Certificate_Schemas):
        try:
            data = Certificate_Spanish(**certificate_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
        
    # GET UPDATE SPANISH
    def get_certificate(self):
        try:
            data = self.db.query(Certificate_Spanish).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE SPANISH
    def update_certificate(self, id: int, certificate_schema: Certificate_Schemas):
        try:
            data = self.db.query(Certificate_Spanish).filter(Certificate_Spanish.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.academy = certificate_schema.academy
            data.title =  certificate_schema.title
            data.url_certificate = certificate_schema.url_certificate
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)

    
    # DELETE SERVICE SPANISH
    def delete_certificate(self, id: int):
        try:
            data = self.db.query(Certificate_Spanish).filter(Certificate_Spanish.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)

