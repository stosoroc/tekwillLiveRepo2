import json
from decimal import Decimal

user = {'username': "mtricolici",
        'age': 24,
        'password': 'askhjdklajsdha',
        'points': Decimal('24.01')}


def serialize_user(user_data):
    serializable_user = dict(user_data)
    serializable_user['points'] = str(serializable_user['points'])
    return serializable_user


def deserialize_user(user_data: dict):
    user_data['points'] = float(user_data['points'])
    return user_data


print(type(user))

json_user_data = json.dumps(serialize_user(user))

print(json_user_data)
print(type(json_user_data))

with open('user.json', 'w+') as file:
    file.write(json_user_data)

# Reading back the data
with open('user.json', 'r+') as file:
    user_json_data = file.read()

user_data = deserialize_user(json.loads(user_json_data))
print(user_data)
print(type(user_data))
print(user_data)
