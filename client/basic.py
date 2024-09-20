import requests

endpoint = "http://127.0.0.1:8000/product/"
response = requests.post(endpoint, 
                         json={'name': 'Banane', 
                               'content':'Juice Banane', 'price':10})
print(response.json())
print(response.status_code)

