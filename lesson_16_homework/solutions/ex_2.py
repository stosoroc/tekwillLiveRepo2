def open_and_print(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print('File does not exist')


if __name__ == '__main__':
    open_and_print("C:\\Users\\mariu\\PycharmProjects\\tekwillLiveRepo2\\lesson_16_homework\\files\\ex_2_file.txt")
