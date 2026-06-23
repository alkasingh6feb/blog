# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
app = FastAPI()

#custom exception
class UserNotFoundExeption(Exception):
    def __init__(self,name:str):
        self.name = name

#global exception handler
@app.exception_handler(UserNotFoundExeption)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundExeption):
    return JSONResponse(
        status_code=404,
        content={"detail": f"User {exc.name} not found"},
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name != "alka":
        raise UserNotFoundExeption(name)
    return {
        "name": name,
    }

@app.get("/users/{user_id}")    
def get_users(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {
        "id": 1,
        "name": "alka"
    }