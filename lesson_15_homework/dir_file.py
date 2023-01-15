# Create a python program that will take as an input a path 
# in the computer: ex: C:\Program Files\.
# The program should list all files (and only files, not other folders) 
# inside the folder if the path provided is a folder.
# If the path is not a folder, the program should show a nice error:
#     Provided path is not a folder.
# If the path does not exist, the program should show a nice error:
#     Provided path does not exist.

import os

class NotAFolderError(Exception):
    pass

class PathNotFoundError(Exception):
    pass

#path = input("Enter a path: ")
#path = "D:\\Instal"
#path = "D:\\Install\\favicon.ico"
path = "D:\\Install"

try:
    if os.path.isdir(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                print(file)
    else:
        if os.path.exists(path):
            raise NotAFolderError("Provided path is not a folder. Please provide a valid folder path.")
        else:
            raise PathNotFoundError("Provided path does not exist. Please provide a valid path.")

except NotAFolderError as e:
    print(e)

except PathNotFoundError as e:
    print(e)
