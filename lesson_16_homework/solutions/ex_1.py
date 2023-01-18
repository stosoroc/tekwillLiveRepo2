def create_file_from_input():
    filename = input('FileName:')
    try:
        open(filename, 'x')
    except FileExistsError as ex:
        print('Fisierul deja exista')


if __name__ == '__main__':
    create_file_from_input()
