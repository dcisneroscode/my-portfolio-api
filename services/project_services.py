from models.models import Project, Project_Spanish
from schemas.schemas import Project_Schemas
from fastapi.responses import JSONResponse
from fastapi import HTTPException


# SERVICE ABOUT ME 
class Project():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE
    def create_project(self, project_schema: Project_Schemas):
        try:
            data =Project(**project_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # GET ALL SERVICE
    def get_project(self):
        try:
            data = self.db.query(Project).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE
    def update_project(self, id: int, project_schema: Project_Schemas):
        try:
            data = self.db.query(Project).filter(Project.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.title = project_schema.title
            data.description = project_schema.description
            data.url_project = project_schema.url_project
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "update data"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)


    # DELETE SERVICE
    def delete_project(self, id: int):
        try:
            data = self.db.query(Project).filter(Project.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)



# SERVICE ABOUT ME SPANISH
class Project_Spanish():

    def __init__(self, db):
        self.db = db

    # CREATE SERVICE SPANISH
    def create_project(self, project_schema: Project_Schemas):
        try:
            data = Project_Spanish(**project_schema.model_dump())
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "created data"}, status_code=201)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # GET ALL SERVICE SPANISH
    def get_project(self):
        try:
            data = self.db.query(Project_Spanish).all()
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)
    
    # UPDATE SERVICE SPANISH
    def update_project(self, id: int, project_schema: Project_Schemas):
        try:
            data = self.db.query(Project_Spanish).filter(Project_Spanish.id == id).first()
            if not data:
                raise HTTPException(status_code=404, detail="can't update")
            data.title = project_schema.title
            data.description = project_schema.description
            data.url_project = project_schema.url_project
            self.db.commit()
            self.db.refresh(data)
            return JSONResponse(content={"message": "data collected"}, status_code=200)
        except Exception as error:
            return JSONResponse(content={"message": "error"}, status_code=400)


    # DELETE SERVICE SPANISH
    def delete_project(self, id: int):
        try:
            data = self.db.query(Project_Spanish).filter(Project_Spanish.id == id).first()
            self.db.delete(data)
            self.db.commit()
            return JSONResponse(content={"message": "deleted data"}, status_code=200)
        except Exception as error:
              return JSONResponse(content={"message": "error"}, status_code=400)

