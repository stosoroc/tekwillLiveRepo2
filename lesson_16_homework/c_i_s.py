# Creati un program python care va citi numele unui fisier de la consola.
# Programul va crea un fisierl cu numele fisierului citit de la consola, 
# apoi va intreba utilizatorul sa scrie un text.
# Textul introdus de utilizator trebuie adaugat in fisier.
# Apoi cititi din fisier textul introdus de utilizator.
import os
from lesson_16_homework.create_file import create_file
from lesson_16_homework.show_file import show_file

def text_nou_file(nume_nou, text_nou):
    with open(nume_nou, 'a') as file:
          file.write(text_nou+"\n")
    
    

if __name__ == '__main__':        
   nume_nou = input("\nNume fisier nou: ")
   create_file(nume_nou)
   text_nou = input("\nText nou: ")
   text_nou_file(nume_nou, text_nou)
   print()
   show_file(nume_nou)
   print()