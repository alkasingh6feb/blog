# pyrefly: ignore [missing-import]
from fastapi import FastAPI, status, HTTPException

app =FastAPI()

@app.get("/users")
def get_users():
    return{
        "name":"alka",
        "age": 24,
        "data":"data fetched"
    }

@app.get("/users/{user_id}")
def get_singal_user(user_id:int):
    # pyrefly: ignore [parse-error]
    if user_id !=1:
        
        raise HTTPException(
            status_code=404,
            detail="user not found" 
        )

    return{
        "name":"alka",
        "age": 24,
        "data":"data fetched"
    }