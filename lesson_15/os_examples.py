import os

program_files = os.path.join('C:\\', 'Program Files', 'Android', 'Android Studio', 'lib')
print(program_files)

file_path = os.path.join(program_files, 'annotations-java5.jar')

print(os.listdir(program_files))
print(os.path.isdir(program_files))
print(os.path.isdir(file_path))

new_file_name = file_path.replace('annotations-java5.jar', 'something')
os.rename(file_path, new_file_name)
