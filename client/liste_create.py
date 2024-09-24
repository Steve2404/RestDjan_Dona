import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/product/auth/"
username = input("Entrer votre username: \n")
password = getpass("Entrer votre possword: \n")
auth_response = requests.post(endpoint, json={'username': username, 'password': password})


if auth_response.status_code == 200:
    endpoint = "http://127.0.0.1:8000/product/liste"
    token = auth_response.json().get('token')
    headers = {
        'Authorization':f'Bearer {token}'
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)