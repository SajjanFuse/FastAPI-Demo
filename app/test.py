import requests

data = {
    "name": "John Doe",
    "department": "Engineering"
}

response = requests.post("http://127.0.0.1:8000/employees/", json=data)

print(response.json())
