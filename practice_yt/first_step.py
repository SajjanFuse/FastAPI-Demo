from fastapi import FastAPI 

# instance 
app = FastAPI() 

# path operation decorator 
@app.get('/') # operations: get, post, put, delete
def home():
    return {'message': 'Hello World'}

@app.get('/test') # operations: get, post, put, delete
def home():
    return {'message': 'Hello World test'}