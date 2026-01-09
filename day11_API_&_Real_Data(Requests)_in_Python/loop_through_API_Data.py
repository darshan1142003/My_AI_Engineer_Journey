import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    posts = response.json()

    for post in posts:
        print(post)