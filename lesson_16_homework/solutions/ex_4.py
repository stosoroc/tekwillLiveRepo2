import json


def get_dishes():
    try:
        with open('dishes.json', 'r+') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_dishes(dish_list):
    with open('dishes.json', 'w') as file:
        return json.dump(dish_list, file)


def list_dishes():
    print('Lista de bucate:')
    for dish in get_dishes():
        print(dish)


def add_dish():
    dish_name = input('Dish Name:')
    all_dishes = get_dishes()
    all_dishes.append(dish_name)
    save_dishes(all_dishes)


def menu():
    print('Selectati optiunea:')
    print('1 pentru a vedea lista')
    print('2 pentru a adauga element')
    option = int(input('Optiunea'))
    if option == 1:
        list_dishes()
    elif option == 2:
        add_dish()


if __name__ == '__main__':
    while True:
        try:
            menu()
        except Exception as ex:
            print('Eroare', ex)
