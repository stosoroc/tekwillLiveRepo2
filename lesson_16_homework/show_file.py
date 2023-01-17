# Create a python program that will open the file _ex_2_file.txt_ [find it here](files/ex_2_file.txt) and print out it's
# content.
import os

def show_file(file1):
    with open(file1, 'r') as my_file:
         print(my_file.readlines())
         
#print(os.path.join(os.getcwd(), 'files', 'ex_2_file.txt'))         

if __name__ == '__main__':  
    show_file(os.path.join(os.getcwd(), 'lesson_16_homework', 'files', 'ex_2_file.txt'))