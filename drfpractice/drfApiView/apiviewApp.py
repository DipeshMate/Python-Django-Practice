import requests
import json
URL = "http://127.0.0.1:8888/Home/"

def get_data(id=None):
   data = {}
   if id is not None:
     data={
        'id':id
      }
   json_data = json.dumps(data)
   headers={'content-Type':'application/json'}
   r = requests.get(url = URL,data = json_data, headers=headers)
   data = r.json()
   print(data)
#get_data()

def post_data():
   # id is auto matic we can't put manually put can update
   data={
       "name":"Rajnish",
       "age":31,
       "gender":"M",
       }
   json_data = json.dumps(data)
   headers={'content-Type':'application/json'}
   r = requests.post(url = URL,data = json_data, headers=headers)
   r_data = r.json()
   print('r_data:',r_data)
# post_data()

def update_data():
   data={
       "id":3,
       "name":"Ravina",
       "age":25,
       "gender":"F", 
       }
   json_data = json.dumps(data)
   headers={'content-Type':'application/json'}
   r = requests.put(url = URL,data = json_data, headers=headers)
   r_data = r.json()
   print('r_data:',r_data)
#update_data()

def delete_data(id = None):
   data = {}
   if id is not None:
     data={
        'id':id
      }
   json_data = json.dumps(data)
   headers={'content-Type':'application/json'}
   r = requests.delete(url = URL,data = json_data, headers=headers)
   r_data = r.json()
   print('r_data:',r_data)
#delete_data(2)
   




