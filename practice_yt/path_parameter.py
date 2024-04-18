from fastapi import FastAPI
from enum import Enum 

class Gender(str, Enum):
    male = 'male'
    female = 'female'

app = FastAPI()

# IMP: Order of routes definition matters on which route gets chosen

# customer database 
@app.get('/customers')
def get_all_cyustomers():
    return {'message':'All customers'}

@app.get('/customer/1')
def get_first_customer():
    return {'message':'First Customer'}

@app.get('/customer/2')
def get_second_customer():
    return {'message':'second Customer'}

@app.get('/customer/{customer_id}')
def get_id_customer(customer_id:int): # data validation by Pydantic! 
    return {'message':customer_id}

@app.get('/customer/gender/{gender}')
def get_id_customer(gender:Gender): # data validation by Pydantic! 
    return {'gender':gender}

