def find_max_line_in_file(file_path):
    with open(file_path) as file:
        line = file.readline()
        longest_line = ''
        longes_line_words = 0
        while line:
            clean_line = line.replace('\n', '').split(' ')
            if len(clean_line) > longes_line_words:
                longes_line_words = len(clean_line)
                longest_line = line
            line = file.readline()
    print('Longest line is', longest_line)


if __name__ == '__main__':
    path = input('Path: ')
    find_max_line_in_file(path)
