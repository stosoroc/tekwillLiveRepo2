
lista = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palin = list(filter(lambda x: x == x[::-1], lista))
print("Palindrome:", palin)




#Ver2
list(filter(lambda x: print(x,end=' ') if x == x[::-1] else None, ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']))

print()

#Ver3
[x for x in ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa'] if x == x[::-1] and print(x)]