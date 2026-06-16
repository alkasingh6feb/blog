from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id":1,
        "name":"alka",
        "email":"alka@gmail.com"
        
    }
  

