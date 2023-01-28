import json

user_json = '{"name": "Eoin Senior","position": "Nurse Practitioner","salary": 2344,"employee_from": "03/16/2010"}'


class User:

    def __init__(self, name, position, salary, employee_from):
        self.name = name
        self.position = position
        self.salary = salary
        self.employee_from = employee_from

    def to_json(self):
        return json.dumps(dict(name=self.name,
                               position=self.position,
                               salary=self.salary,
                               employee_from=self.employee_from))

    @classmethod
    def from_json(cls, json_data):
        json_dict = json.loads(json_data)
        return cls(**json_dict)

    @staticmethod
    def from_json_static(json_data):
        json_dict = json.loads(json_data)
        return User(**json_dict)  # BAD, DUring inheritance breaks


class NewUser(User):
    pass


my_user = User.from_json(user_json)
print(my_user)
print(my_user.name)
print(my_user.to_json())

my_user = NewUser.from_json(user_json)
print(my_user)

my_user = NewUser.from_json_static(user_json)
print(my_user)
