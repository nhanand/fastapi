# Pydantic Models + Data Validation + Nested Schemas

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usser(BaseModel):
    name:str
    age:int
    email:str

@app.post("/crreate_user")
def create_user(user: Usser):
    return{
        "message": "user created",
        "data": user
    }

# nested schemas

class Address(BaseModel):
    city:str
    pincode: int

class User(BaseModel):
    name: str
    address: Address

@app.post("/create_user")
def create_user(user: User):
    return{
        "message": "user created",
        "data": user
    }
