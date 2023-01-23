elements = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

filtered = list(filter(lambda a: a[::-1] == a, elements))

print(filtered)
