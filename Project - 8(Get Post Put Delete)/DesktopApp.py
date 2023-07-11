import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# -------------------------------------------------------------------------------

# 1 - Read Data (Get Request)
'''
def GetData(id=None):
    d = {}

    # convert dict into a json
    json_data = json.dumps(d)

    req = requests.get(url = URL , data = json_data)

    response = req.json()

    return response

# Get all Data

all_data = GetData()
print(all_data)

# -------------------------------------------------------------------------------

# 2 - Insert values (Post Request)

def PostData():
    data = {
        'name': 'Rohan Salve',
        'age': 22,
        'course': 'Java Full Stack'}

    # convert dict into json
    json_data = json.dumps(data)

    req = requests.post(url=URL , data = json_data)

    response = req.json()

    return response

# Post Data

post_data = PostData()
print(post_data)


# -------------------------------------------------------------------------------

# 3 - Update Values (Put request)
# partially update

def UpdatePartial():
    d = {'id': 1,
        'name': 'Ramesh',
        'age': 36,
        'course': 'MERN Stack'}

    json_data = json.dumps(d)

    req = requests.put(url=URL, data=json_data)

    return req.json()

update_data = UpdatePartial()
print(update_data)


# -------------------------------------------------------------------------------

# 4 - Delete Data (Delete request)

def DeleteData(id=None):
    d = {}
    if d is not None:
        d = {'id': id}

    json_data = json.dumps(d)

    req = requests.delete(url=URL, data=json_data)

    return req.json()

delete_data = DeleteData(2)
print(delete_data)
 
'''


