#dynamic routes  --- routes that changes based on path parameters
# like user1 
#      user2


from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
# def get_user(user_id):

#automatic validation i.e datatype input should be int, pass str if string
def get_user(user_id: int):       
    return{"user_id": user_id}



# http://127.0.0.1:8000/users/101