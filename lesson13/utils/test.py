
from string_utils.sting_utils import split_by_comma_input
from utils import print_dict_each_element_on_row


if __name__ == '__main__':
    user_input = split_by_comma_input()
    print(user_input)
    
    my_dict = dict(key1=[1,2,3], key2=[3,4,5])
    print_dict_each_element_on_row(my_dict)
    