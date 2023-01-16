# Using the Random Module, create a small 
# program that will simulate 2 x 6 sided dice.
# The programm should allow the user to roll the dice, 
# and show the values on each dice, and the total sum.

import random


def zar_random(parti,zaruri):
    total = 0
    print()
    for i in range(zaruri):
        zar = random.randint(1, parti)
        total += zar
        print(f"Zar{i+1}:  " + str(zar))
    print("Total: " + str(total))

def zar_start(parti,zaruri):
    while True:
        zar_random(parti,zaruri)
        inca = input("\nInca o data? (Enter pentru DA): ")
        if inca:
            break
    
parti = 6
zaruri = 2

zar_start(parti,zaruri)

# while True:
#     # zar1 = random.randint(1, 6)
#     # zar2 = random.randint(1, 6)
#     # total = zar1 + zar2
#     # print("Un  Zar: " + str(zar1))
#     # print("Alt Zar: " + str(zar2))
#     # print("Total:   " + str(total))
#     zar_random(parti,zaruri)
#     inca = input("\nInca o data? (Enter pentru DA): ")
#     if inca:
#         break

