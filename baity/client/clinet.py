import requests
import secrets


ep = 'http://127.0.0.1:8000/house/create'

data = {
    "location": "",
    "description": "",
    "photos": [open('house.png', 'rb')]
}

print(data["photos"])

boundary = f'----{secrets.token_hex(16)}'
headers = {
    'Content-Type': f'multipart/form-data' f'boundary ={boundary}'
}


response = requests.post(ep, data=data, headers=headers)
print(response.json())
