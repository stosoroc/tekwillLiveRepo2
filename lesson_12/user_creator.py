

def user_creator():
    un = input('UserName: ')
    pwd = input('Password: ')
    return dict(username=un, password=pwd)


def multiple_user_creator(user_count):
    user_list = []
    for i in range(user_count):
        user_list.append(user_creator())
    return user_list


multiple_user_creator(3)

# print(list_of_users)
# print(len(list_of_users))