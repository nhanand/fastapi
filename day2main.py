from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello world from FastAPI VENV"}



@app.get("/about")
def about():
    return {"message":"its about page"}

@app.get("/user")
def user():
    return {
        "user": ["mohit", "rohit", "amit"]
            }