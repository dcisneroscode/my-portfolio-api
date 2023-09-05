from pydantic import BaseModel


class User_Schemas(BaseModel):
    username: str
    password: str


class About_Me_Schema(BaseModel):
    about_me: str
    front_end: str
    back_end: str
    responsive_design: str
    technical_support: str
    it_security: str
    cover_letter: str

class Academy_Profile_Schemas(BaseModel):
    title: str
    description: str
    status: str


class Professional_Profile_Schemas(BaseModel):
    title: str
    date: str
    description: str


class Certificate_Schemas(BaseModel):
    academy: str
    title: str
    url_certificate: str

class Project_Schemas(BaseModel):
    title: str
    description: str
    url_project: str


class Images_Schemas(BaseModel):
    images: str


class Documents_Schemas(BaseModel):
    document: str
