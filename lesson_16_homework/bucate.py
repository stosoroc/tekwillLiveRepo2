# Creati un program care va avea 2 optiuni:
# * Afiseaza toate bucatele
#   * Va afisa toate bucatele stocate intr-un fisier
# * Adauga bucata
#   * Va adauga o bucata in lista din fisier
# Daca utilizatorul re-porneste programul, la afisarea bucatelor, 
# trebuie sa fie afisate toate elementele salvate anterior.

import os.path
import sys
from lesson_16_homework.c_i_s import text_nou_file
from lesson_16_homework.create_file import create_file
from lesson_16_homework.show_file import show_file


if __name__ == '__main__':        
   if not os.path.exists('bucate.txt'):
    create_file('bucate.txt')
    text_nou = input("\nAdauga bucate: ")
    text_nou_file('bucate.txt', text_nou)
    sys.exit()
   print()
   show_file('bucate.txt')
   bucata_noua = input("\nBucata noua: ")
   text_nou_file('bucate.txt', bucata_noua)
   print()