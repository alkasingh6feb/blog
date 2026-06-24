from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def verify_token(token: str = Header(None)):
    if token == "mohit":
        return True
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/sequre-data")
def sequre_data(user = Depends(verify_token)):
    return{
        "msg" : "sequre data accesssed"
    }

# def common_logic():
#     return {
#         "this is common logic"
#     }

# @app.get("/home")
# def home(data=Depends(common_logic)):
#     return data

# @app.get("/profile")
# def profile(data=Depends(common_logic)):
#     return data
