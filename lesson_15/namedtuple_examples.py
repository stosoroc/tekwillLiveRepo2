from collections import namedtuple

UserType = namedtuple('User', ['username', 'first_name', 'last_name'])
print(UserType)

marius = UserType('mtricolci', 'marius', 'tricolici')
print(marius)
print(marius.username)
marius.username = 'Marius'

