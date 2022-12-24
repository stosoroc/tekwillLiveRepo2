def input_numbers_list():
    text = input('Scrieti o lista de numere separate prin spatiu')
    nums_list =  [int(el) for el in text.split(' ') if el]
    return nums_list


def input_strings_list():
    pass


if __name__ == '__main__':
    # Code for testing my function
    print('Executat din input_utils')
    print(input_numbers_list())