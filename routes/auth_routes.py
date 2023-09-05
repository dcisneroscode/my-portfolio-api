from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.schemas import User_Schemas
from tokens.jwt import JWTBearer, create_token

auth_routes = APIRouter()


@auth_routes.post(
    path="/login"
)
def login(user: User_Schemas):
    if user.username == "dcisneros":
        return create_token(user.model_dump())
    else:
        return JSONResponse(content={"messagge": "User not found"}, status_code=404)

