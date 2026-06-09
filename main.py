# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from pydantic import BaseModel

# pyrefly: ignore [unknown-name]
app = FastAPI()

# pyrefly: ignore [unknown-name]
class User(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(user:User):
    return {
        "msg" : "user created",
        "data" :user
    }