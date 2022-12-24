class IndexNotFound(Exception):
    pass


def find_index(list_to_search, element_to_search):
    for index, elem in enumerate(list_to_search):
        if elem == element_to_search:
            return index
    raise IndexNotFound(f'Element {element_to_search} is not in list')
    
    
def handle_list_lement_not_found(list_to_add_to, exception):
    anwer = input('Would you like to add it ? y/n: ')
    if anwer != 'y':
        return
    try:
        element = int(str(exception).split(' ')[1])
        list_to_add_to.append(element)
    except Exception:
        print('Failet to add element')
        return
    
my_list = [1,2,3]
while True:
    try:
        print(find_index(my_list, int(input())))
    except IndexNotFound as ex:
        print(ex)
        handle_list_lement_not_found(my_list, ex)
    except ValueError as ex:
        print(type(ex))
        print(ex)
    except Exception:
        print("I dunno what went wrong")