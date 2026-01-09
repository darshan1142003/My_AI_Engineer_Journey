import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    posts = response.json()

    with open("api_data.json", "w") as f:
        json.dump(posts, f, indent = 4)

        print("API data saved successfully")

else:
    print("API requests Failed", response.status_code)