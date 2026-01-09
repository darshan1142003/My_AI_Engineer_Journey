import json

with open("api_data.json", "r") as f:
    data = json.load(f)

print(data)    