# Using functions you have created for the exercise above (ex1.) 
# create a program that will take as input a path to a folder.
# WARNING: Use a test path, with files specifically created for the test purpose. 
# Be careful as to not change something is system folders.
# The program should rename all files in the folder to numbers (from 1 to n)
# sorted by the creation date of the file: os.path.getctime(file_path) - will return the date created of the file.
# The program should not overwrite the extension of the file: file.extension - 
# For example some_Doc.docx should be renamed to 1.docx.
# Also add an option to add a prefix, for example: Prefix doc will 
# rename all files to doc1.docx, doc2.png, doc3.pdf, doc4.docx....
import os

class NotAFolderError(Exception):
    pass

class PathNotFoundError(Exception):
    pass

def get_files(folder_path):
        if os.path.isdir(folder_path):
            return [(os.path.join(folder_path, file)) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        else:
            raise ValueError("Error!!! Provided path is not a folder")
    

#path = input("Enter a path: ")
#path = "D:\\Instal"
#path = "D:\\Install\\favicon.ico"
path = "D:\\Test"

# prefix = input("Enter a prefix: ")
prefix = "mig"

list_of_files = get_files(path)
sorted_list = sorted( list_of_files, key = os.path.getmtime)

#print(sorted_list)

i = 0
try:
    if os.path.isdir(path):
        #for file in os.listdir(path):
        for file in sorted_list:
            #if os.path.isfile(os.path.join(path, file)):
            i += 1
            extension = os.path.splitext(str(file))[1]
            new_name = path + "\\" + prefix + str(i) + extension
            os.rename(str(file), new_name)
            print(f"old name is {file}, new name is {new_name}")
    else:
        if os.path.exists(path):
            raise NotAFolderError("Error!!! Provided path is not a folder")
        else:
            raise PathNotFoundError("Error!!! Provided path does not exist")

except NotAFolderError as e:
    print(e)

except PathNotFoundError as e:
    print(e)
