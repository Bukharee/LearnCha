import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={
    "title": "Hello World"})
print(get_response.json())
