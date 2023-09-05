import os
from fastapi import  Request
from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from fastapi.security import HTTPBearer

load_dotenv()
key_jwt = os.getenv("SECRET_TOKEN")


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def create_token(data: dict,):
    token = encode(payload={**data,  "exp": expire_date(2)}, key=key_jwt, algorithm="HS256")
    return token

def validate_token(token):
    try:
        return decode(token, key=key_jwt, algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message" : "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message" : "Token Expired"}, status_code=401)


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        return data


