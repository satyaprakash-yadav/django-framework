import requests
'''
def GETDATA(id):
    URL = 'http://127.0.0.1:8000/get_data/'+str(id)
    req = requests.get(url=URL)
    JsonData = req.json()
    return JsonData

data = GETDATA(1)
print(data)
'''


URL = 'http://127.0.0.1:8000/get_alldata'
req = requests.get(url=URL)
json_data = req.json()
print(json_data)


