# Avand urmatorul fisier JSON: [file](files/employee_list.json).
# Creati un program care va afisa urmatoare informatie din fisier.
# * Lista de toti lucratorii
# * Lista la toate pozitiile din companie (Unicale)
# * Calculeaza suma totala care compania are de achitat lucratorii
# * Calculeaza suma totala de impozite care compania are de achitat intr-o luna
#   * Valoarea de % impozit e introdusa la consola
# * Afiseaza informatie despre 10 cei mai bine platiti lucratori 
#      (name, position, salary, employment_start_date) de la mai mult la mai putin.
# * Afiseaza informatie despre 10 lucratori cu cel mai mult timp in companie 
#      (name, position, salary,employment_start_date) de la mare la mic. 

import json
import os
from datetime import datetime

def open_json(jj=(os.path.join(os.getcwd(),'lesson_16_homework', 'files', 'employee_list.json'))):
    with open(jj) as json_file:
        return json.load(json_file)

def print_name():  
    #Lista de toti lucratorii  
    data = open_json()
    for employee in data:
        print(employee['name'])

def poz():
    #Lista la toate pozitiile din companie (Unicale)    
    pozitiile = []
    data = open_json()
    for employee in data:
        if not employee['position'] in pozitiile:
            pozitiile += [employee['position']]
            print(employee['position'])

def calc_tot():
    #Calculeaza suma totala care compania are de achitat lucratorii
    tot = 0
    data = open_json()
    for employee in data:
        tot += int(employee['salary'])
    return tot

def impozit():
    # * Calculeaza suma totala de impozite care compania are de achitat intr-o luna
    # * Valoarea de % impozit e introdusa la consola
    imp1 = int(input("Procent de impozit: "))
    return calc_tot()*imp1/100

def top10sal():
    # * Afiseaza informatie despre 10 cei mai bine platiti lucratori 
    #   (name, position, salary, employment_start_date) de la mai mult la mai putin.
    data = open_json()
    sorted_list = sorted(data, key=lambda d: d['salary'], reverse=True)
    i = 0
    for employee in sorted_list:
        print(employee)
        i +=1
        if i == 10:
            break
def top10vechime():
    # * Afiseaza informatie despre 10 lucratori cu cel mai mult timp in companie 
    #   (name, position, salary,employment_start_date) de la mare la mic.            
    data = open_json()
    #sorted_list = sorted(data, key=lambda d: d['employee_from'])
    data.sort(key=lambda d: datetime.strptime(d['employee_from'], "%m/%d/%Y"))
    
    i = 0
    for employee in data:
        print(employee)
        i +=1
        if i == 10:
            break
                    
if __name__ == '__main__':  

    print()    
    print('Lista de toti lucratorii:')
    print_name()

    print()
    print('Lista la toate pozitiile din companie Unicale:')
    poz()

    print()
    print('Calculeaza suma totala care compania are de achitat lucratorii:')
    print(calc_tot())

    print()
    print('Calculeaza suma totala de impozite care compania are de achitat intr-o luna')
    print('Valoarea de procent impozit e introdusa la consola: ')
    print(impozit())

    print()        
    print('Afiseaza informatie despre 10 cei mai bine platiti lucratori')
    print('name, position, salary, employment_start_date de la mai mult la mai putin: ')
    top10sal()
    
    print()           
    print('Afiseaza informatie despre 10 lucratori cu cel mai mult timp in companie')
    print('name, position, salary,employment_start_date de la mare la mic: ')
    top10vechime()
    