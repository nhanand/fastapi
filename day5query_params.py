# query params
# ex: /products?price=100
# used in search sort filter





from fastapi import FastAPI
app = FastAPI()

#optional parameters
@app.get("/users")
#def get_user(name):
def get_user(name: str=None):     # if no params passed o/p is null. this is optional paramters
    return{"name": name}    

# http://127.0.0.1:8000/users?name=mohit

# default values
@app.get("/products")
#def get_user(name):
def get_user(limit: int=10):     # 10 is by default limit.
    return{"limit": limit} 

#http://127.0.0.1:8000/products
#http://127.0.0.1:8000/products?limit=100

#multiple query params
@app.get("/items")
#def get_user(name):
def get_user(name: str=None, price: int=0):     
    return{"name": name,
           "price": price
           } 

# http://127.0.0.1:8000/items
# http://127.0.0.1:8000/items?name=anand&price=2000