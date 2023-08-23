import requests
import json

jsonplaceholder_url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(jsonplaceholder_url)
json_data = json.loads(response.text)
print(len(json_data))
print(json_data[0])
print(json_data[0].keys())

post_req = {'userId':1, 'title':'test', 'body':'test body'}
response = requests.post(jsonplaceholder_url, post_req)
print(response.text)