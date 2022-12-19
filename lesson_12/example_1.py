

a = dict(
    key1=1,
    key2=2
)
b= dict(
    key2=2,
    key1=1,
)

a = {} # dict
print(type(a))
a = {1,2} # set
print(type(a))
empty_set = set() 
a = {1:1, 2:2} # dict

print(a == b)
print(a is b)
print(a is a)

## Deleting keys from dict

a = dict(key1=1, key2=2)
print(a)
del a['key1']
print(a)
del a # Noi stegem a in interpretator
# print(a)


dl={1:10, 2:20, 3:30, 4:40} 
d2={5:50, 6:60, 7:70}
dl.update(d2)
print(dl)


my_set = {('x', 'y', 'z')}
print(my_set)

my_set = set()

