import requests
try:
    response = requests.get('https://api.github.com/users/darshan11423')

    data = response.json()
    if response.status_code == 200:
        print("username:", data["login"])

    else:
        print("failed ! API Error :", response.status_code)    

except requests.exceptions.RequestException as e:
    print("API Error", e)