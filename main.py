# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from pydantic import BaseModel

# pyrefly: ignore [unknown-name]
app = FastAPI()

# pyrefly: ignore [unknown-name]
# class User(BaseModel):
#     name:str
#     age:int

# @app.post("/create-user")
# def create_user(user:User):
#     return {
#         "msg" : "user created",
#         "data" :user
#     }

class Address(BaseModel):
    city:str
    pin_code:str

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/create_user")
def create_user(user:User):
    return{
        "msg":"user created"
    }
