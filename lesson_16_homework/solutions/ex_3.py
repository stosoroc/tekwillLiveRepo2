def create_file_from_input_and_add_text(file_name):
    try:
        with open(file_name, 'w') as file:
            data = input('Info to add:')
            file.write(data)
    except FileExistsError as ex:
        print('Fisierul deja exista')


def open_and_print(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print('File does not exist')


if __name__ == '__main__':
    filename = input('FileName:')
    create_file_from_input_and_add_text(filename)
    open_and_print(filename)
