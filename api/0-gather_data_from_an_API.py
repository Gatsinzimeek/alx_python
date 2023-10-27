import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

print(response.json()['items'])