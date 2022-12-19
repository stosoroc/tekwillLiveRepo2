
users = {1:'Marius', 2:'Ion', 3:'Elena'}

uid = 1

# for user in users:
#     print('Iter for ', user)
#     if uid == user:
#         print(users[user])
#         break
# else:
#     print('User not found')


found_user = None
for user in users:
    print('Iter for ', user)
    if uid == user:
        found_user = users[user]
if found_user:
    print(f"Found user {found_user}")
else:
    print('User not found')
