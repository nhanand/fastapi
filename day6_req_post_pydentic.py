#json input handling
#post req
#intro to pydantic

# using pydantic we can vaildate and define data



from fastapi import FastAPI
from pydantic import BaseModel        #importing pydantic for data validation

app = FastAPI()
class user(BaseModel):
    name: str
    age: int

@app.post("/crreate_user")
def create_user(name:str,age:int):
    return{
        "name": name,
        "age": age
    }

# real world example
@app.post("/create_user")
def create_user(user:dict):
    return{
        "message": "user created",
        "data": user
    }          


#{
  #"name": "avi",
  #"age": 24,
  #"place": "pune"
#}

# pydantic example
@app.post("/create_pydantic_user")
def create_user(user:user):
    return{
        "message": "user created",
        "data": user
    }          

#{
 # "name": "string",
 # "age": 0
#}