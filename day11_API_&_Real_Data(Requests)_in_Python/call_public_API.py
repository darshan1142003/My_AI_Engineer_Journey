import requests

response = requests.get('https://api.github.com/users/darshan1142003')

print(response.json())