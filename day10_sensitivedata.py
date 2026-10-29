#Response Models + Data Validation + Hide Sensitive Data

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

# data to hide or say what fe to show
class UserResponse(BaseModel):
    name:str
    age:int 

@app.get("/user",response_model=UserResponse)
def get_user():
    return{
        "name": "rahul",
        "age": 24,
        "password":"sdcfghbj"
    }