import requests
import json

URL="http://127.0.0.1:8000/home/"

response = requests.get(url = URL) # response <--- request 
print(response)
json_data = response.json()
print(json_data)
