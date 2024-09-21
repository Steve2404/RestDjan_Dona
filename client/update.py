import requests

endpoint = "http://127.0.0.1:8000/product/11/update"
response = requests.put(endpoint,  
                        json={'name':'Papaye', 'content':'Juice Papaye','price':4})
print(response.json())
print(response.status_code)