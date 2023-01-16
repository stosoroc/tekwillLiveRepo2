with open('file.txt', 'w+') as file:
    file.write('Line1\n')
    file.write('Line2\n')
    file.writelines(['Line3\n', 'Line4\n', ])

with open('file.txt') as file:
    file.seek(7, 0)
    print(file.readlines()) # seteaza cursorul la sfarsit
    print(file.readlines())
    file.seek(0, 0)
    print(file.readlines())
