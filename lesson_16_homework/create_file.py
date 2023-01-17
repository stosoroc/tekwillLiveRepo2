#Create a python program that will create a file with the name input from console
import os


class NotAFolderError(Exception):
    pass

class PathNotFoundError(Exception):
    pass

def create_file(nume_nou):
    with open(nume_nou, 'w+') as my_file:
        pass  # Do something

def get_files(folder_path):
        if os.path.isdir(folder_path):
            return [(os.path.join(folder_path, file)) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        else:
            raise ValueError("Error!!! Provided path is not a folder")
        

if __name__ == '__main__':
    nume_nou = input("\nNume fisier nou: ")
    create_file(nume_nou)
    for f in get_files(os.getcwd()):
        if f == os.path.join(os.getcwd(), nume_nou):
            print('\x1b[0;32;40m' + f + '\x1b[0m')
        else:
            print(f)
    print()