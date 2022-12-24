from lesson_12_homework.input_utils import input_numbers_list


def mult_list(lst_to_mult: list):
    mult = 1
    for a in lst_to_mult:
        mult *= a
    return mult



def mult_list_recursiv(lst_to_mult: list):
    if len(lst_to_mult) == 1:
        return lst_to_mult[0]
    return lst_to_mult[0] * mult_list(lst_to_mult[1:])


# 1, 2, 3
# 1 * 
# 2, 3
# 1 * 2
# 3 
# 1 * 2 * 3 


if __name__ == '__main__':  # Pentru executarea codului
    print('Executat din ex_1')
    numbers = input_numbers_list()
    print(mult_list_recursiv(numbers))
