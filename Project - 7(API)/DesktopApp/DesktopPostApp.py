import requests
import json

def PostData(data):
    URL = 'http://127.0.0.1:8000/post_data/'
    js_data = json.dumps(data)
    req = requests.post(url=URL, data=js_data)
    return req.json()

data = {'name':'jay', 'roll':121, 'course':'BSCCS'}
x = PostData(data)
print(x)
