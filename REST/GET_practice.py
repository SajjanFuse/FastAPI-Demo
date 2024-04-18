

import requests 
import json 

api_url = "https://jsonplaceholder.typicode.com/todos/1"

# GET request 
response = requests.get(api_url)

print(response.json())
print(response.status_code)

api_url_post = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1,
    "title": "Buy milk",
    "completed": False
    }
headers =  {"Content-Type":"application/json"}

# json.dumps to serialize the dict? 
# more control over the request
response2 = requests.post(api_url_post, data=json.dumps(todo), headers=headers)

print(response2)
print(response2.json())
print(response2.status_code)

# for updating, PUT request 
print('RESPONSE 3, PUT')

api_url_3 = "https://jsonplaceholder.typicode.com/todos/10"
response_3 = requests.get(api_url_3)
response_3.json()
{'userId': 1, 'id': 10, 'title': 'illo est aut', 'completed': True}

todo = {"userId": 1, "title": "Wash car", "completed": True}
response_3 = requests.put(api_url_3, json=todo)
print(response_3.json())
print(response_3.status_code)

print(requests.get(api_url_3).json())

# PATCH for modifying a specific field 

print()
print() 
edited_field = {"title" : "PATCH modified title"}

response_4 = requests.patch(api_url_3, edited_field)
print(response_4.status_code)

print(requests.get(api_url_3).json())

