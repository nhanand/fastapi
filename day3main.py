from fastapi import FastAPI

app = FastAPI()

#home route
@app.get("/")
def home():
    return {"message:" "welcome to fatapi"}
    
# about route
@app.get("/about")
def about():
    return {"message": "this is about page"}

# user route
@app.get("/user")
def user():
    return{
            "user": ["mohit", "rohit", "amit"]
           }

