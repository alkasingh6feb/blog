
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []
class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"Todo added successfully", "data":todo}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message":"todo not found"}
    
@app.put("/todos{todo_id}")
def update_todo(todo_id:int,update_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return {"message":"todo updated successfully", "data":update_todo}
    return {"message":"todo not found"}
    
@app.delete("/todos{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message":"todo deleted successfully"}
    return {"message":"todo not found"}
