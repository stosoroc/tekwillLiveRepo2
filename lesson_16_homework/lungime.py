# Creati un program care va citi un fisier textual conform unui path, din input. 
# Programul va afisa linia din text care are cea mai mare lungime.
import os

def pe_linii(file1='bucate.txt'):
    file2 = open((os.path.join(os.getcwd(),'lesson_16_homework', file1)), 'r')
    return file2.readlines()

def mai_mare(linia):
    mare = 0
    cea_mai = 0
    for l in linia:
        if len(l) > mare:
            mare = len(l)
            cea_mai = l
    return cea_mai

if __name__ == '__main__':
    print(mai_mare(pe_linii()))
    