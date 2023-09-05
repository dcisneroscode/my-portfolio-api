from database.database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__  = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class About_Me(Base):

    __tablename__ = "about_me_information"

    id = Column(Integer, primary_key=True, index=True)
    about_me = Column(String)
    front_end = Column(String)
    back_end = Column(String)
    responsive_design = Column(String)
    technical_support = Column(String)
    it_security = Column(String)
    cover_letter = Column(String)



class Academy_Profile(Base):

    __tablename__ = "academy_profile"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)

class Professional_Profile(Base):

    __tablename__ = "professional_profile"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(String)
    description = Column(String)

class Certificate(Base):

    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url_certificate = Column(String)


class Project(Base):

    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    url_project = Column(String)


class Images(Base):

    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    images = Column(String)

class Documents(Base):
    
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    documents = Column(String)



class About_Me_Spanish(Base):

    __tablename__ = "about_me_information_spanish"

    id = Column(Integer, primary_key=True, index=True)
    about_me = Column(String)
    front_end = Column(String)
    back_end = Column(String)
    responsive_design = Column(String)
    technical_support = Column(String)
    it_security = Column(String)
    cover_letter = Column(String)


class Academy_Profile_Spanish(Base):

    __tablename__ = "academy_profile_spanish"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)

class Professional_Profile_Spanish(Base):

    __tablename__ = "professional_profile_spanish"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(String)
    description = Column(String)

class Certificate_Spanish(Base):

    __tablename__ = "certificate_spanish"

    id = Column(Integer, primary_key=True, index=True)
    academy = Column(String)
    title = Column(String)
    url_certificate = Column(String)


class Project_Spanish(Base):

    __tablename__ = "project_spanish"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    url_project = Column(String)

