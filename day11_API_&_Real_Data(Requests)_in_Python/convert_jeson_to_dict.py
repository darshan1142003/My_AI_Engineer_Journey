import requests

response = requests.get('https://api.github.com/users/darshan1142003')
data = response.json()


print("Username:", data["login"])
print("Public Repos:", data["public_repos"])
print("Followers:", data["followers"])