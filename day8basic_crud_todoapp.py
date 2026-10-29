from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

# creating todo data
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return{
        "message": "tddo created",
        "data": todo
    }
# fetching all data
@app.get("/todos")
def get_todos():
    return todos

# fetching single data
@app.get("/todos/{todo_id}")    # path params
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return{"error": "todos not found"}

# update
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index]=updated_todo
            return{"message": "datae updated",
                   "data": updated_todo
                   }
    return{"error": "todos not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return{"message": "data deleted"}
    return{"error": "todos not found"}    

