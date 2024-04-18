from fastapi import FastAPI, HTTPException
from database import cursor, connection
from models import Employee

app = FastAPI()

@app.on_event("startup")
async def startup():
    print("App is starting up")


# Endpoint to get all employees
@app.get("/employees/")
async def get_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return [{"id": row[0], "name": row[1], "department": row[2]} for row in employees]

# Endpoint to get a specific employee by ID
@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
    employee = cursor.fetchone()
    if employee:
        return {"id": employee[0], "name": employee[1], "department": employee[2]}
    raise HTTPException(status_code=404, detail="Employee not found")

# Endpoint to create a new employee
@app.post("/employees/")
async def create_employee(employee: Employee):
    cursor.execute("INSERT INTO employees (name, department) VALUES (?, ?)", (employee.name, employee.department))
    
    # for committing change to the db
    connection.commit()
    return {"id": cursor.lastrowid, **employee.model_dump()}

# Endpoint to delete an employee by ID
@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    connection.commit()
    return {"message": "Employee deleted"}

# Endpoint to update an employee's data
@app.put("/employees/{employee_id}/{column}/{new_value}")
async def update_employee(employee_id: int, column: str, new_value: str):
    if column not in ['name', 'department']:
        raise HTTPException(status_code=400, detail="Invalid column name")

    cursor.execute(f"UPDATE employees SET {column}=? WHERE id=?", (new_value, employee_id))
    connection.commit()
    return {"message": "Employee updated"}
