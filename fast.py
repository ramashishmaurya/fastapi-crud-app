from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {
        "hello":"worlds"    }

@app.get('/Extract/{id}')
def extract(id:int , q :str | None=None):
    return {
        "id":id , 
        "Q":'this id q '
    }