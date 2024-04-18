from fastapi import FastAPI

app = FastAPI() 

# query parameter: function parameters that are not path parameters
#   - i.e they are not used in the path of the route 

# pagination : offset, limit 



@app.get('/customers')
def get_customers():
    return {'message':'All customers'}