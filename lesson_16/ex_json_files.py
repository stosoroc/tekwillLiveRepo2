import json

with open('user.json') as file:
    data = json.load(file)
    print(data)
