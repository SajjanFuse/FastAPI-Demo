from pydantic import BaseModel 

class Employee(BaseModel):
    """Model for storing information of employees
    Specified data type for each field as expected

    Arguments:
        BaseModel -- _description_
    """
    id: int 
    name: str 
    department: str