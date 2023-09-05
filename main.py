from fastapi import FastAPI
from routes.auth_routes import auth_routes


app = FastAPI()


app.include_router(auth_routes, prefix="/api")