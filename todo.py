from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional

todolist = []

app = FastAPI()

class Todo(BaseModel):
    name: str
    course: str
    fees: Optional[str]=None


@app.post('/adddata') 
def appendata(data: Todo):
    data1 = data.model_dump()
    todolist.append(data1)

    return {
        "message": "Data added successfully",
        "data": data1
    }


@app.get('/home')
def getresult():
    return todolist

@app.delete('/delete')
def deletefunction():
    del todolist


