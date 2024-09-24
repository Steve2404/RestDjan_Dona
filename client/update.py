import requests

endpoint = "http://127.0.0.1:8000/product/15/update"
response = requests.put(endpoint,  
                        json={'name':'Orange', 'content':'Juice Orange','price':4})
print(response.json())
print(response.status_code)