import requests
from getpass import getpass

password = getpass()

auth_endpoint = "http://127.0.0.1:8000/api/auth"

auth_response = requests.post(auth_endpoint, json={
    "username": "bukhari", "password": password})


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = "http://127.0.0.1:8000/api/product/list-or-create"
    get_response = requests.get(endpoint, headers=headers, json={
        "title": "fresh title"})

    print(get_response)
