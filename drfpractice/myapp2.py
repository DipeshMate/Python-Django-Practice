#  client Application frontend

import requests
import json
URL = "http://127.0.0.1:8000/stucreate/" # url of your view

data = {
    'name': 'Chunmoon',
    'roll' : 88848486,
    'age' : 35,
} # python native object 

# Convert the data to JSON format
json_data = json.dumps(data) # convert to json_data

# Send the POST request with proper headers
response = requests.post(url=URL, data=json_data,headers={'Content-Type': 'application/json'})

# Print the response to see the result
print(response.status_code)
print(response.text)