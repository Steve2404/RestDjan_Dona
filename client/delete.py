import requests

id = int(input("Enter the id of product tat you want to delete: "))
endpoint = f"http://127.0.0.1:8000/product/{id}/delete"
response = requests.delete(endpoint)

print(response.status_code, response.status_code ==204)