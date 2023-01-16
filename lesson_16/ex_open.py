# with open('file2.txt', 'w+') as my_file:
#     pass
#
#
# #
# # with open('file2.txt', 'r') as my_file:
# #     print(my_file.readlines())
#

def create_file(file_name):
    with open(file_name, 'w+') as my_file:
        pass  # Do something


def create_file_x(file_name):
    open(file_name, 'x')


def add_to_file(file_name, text):
    with open(file_name, 'a') as file:
        file.write(text)


# create_file_x('file3.txt')
# add_to_file('file_4.txt', 'Bye python\n')

open('file_5.txt', 'r')
