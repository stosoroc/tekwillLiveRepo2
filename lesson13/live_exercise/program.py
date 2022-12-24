# Un program, care permite sa cream si modificam o lista de oaspeti la un eveniment. 


list_oaspeti = []


class RegistrationExemption(Exception):
    pass

class StopExecution(Exception):
    pass

def add_oaspete():
    name = input('Numele oaspetelui')
    if name in list_oaspeti:
        raise RegistrationExemption('Already registered')
    list_oaspeti.append(name)
    
def remove_oaspete():
    name = input('Numele oaspetelui')
    if name not in list_oaspeti:
        raise RegistrationExemption('Oaspete does not exist')
    list_oaspeti.remove(name)
    
def viz_list():
    if not list_oaspeti:        
        print("nu avem oaspeti")
    for name in list_oaspeti:
        print(name)
    
    
def show_menu():
    print('\n')
    print('Selectati optiunea: 1 Pentru a adauga oaspete, 2 pentur a sterge oaspete, 3: pentru a vizualiza lista \
          sau orice altceva pentru a opri programul')
    opt = input('Optiunea')
    if opt == '1':
        add_oaspete()
    elif opt == '2':
        remove_oaspete()
    elif opt == '3':
        viz_list()
    else:
        raise StopExecution()
    
    
while True:
   try:
       show_menu()
   except RegistrationExemption as ex:
       print()
       print(ex)
       print()
   except StopExecution as ex:
       break