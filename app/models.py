from pydantic import BaseModel 

class Employee(BaseModel):
    """Model for storing information of employees

    Arguments:
        BaseModel -- _description_
    """
    id: int 
    name: str 
    department: str