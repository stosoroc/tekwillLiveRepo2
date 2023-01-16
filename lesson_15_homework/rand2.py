# Using the Random Module, create a small program that will simulate 2 x 6 sided dice.
# The programm should allow the user to roll the dice, and show the values on each dice, and the total sum.

# Improve the exercise above to let the user pick how many sides the Dice has and how many dice there are.
# After the dice are configured, let the user roll the dice until STOP.

import random
from lesson_15_homework.rand import zar_start

print()

parti = int(input("Cite parti are zar: "))
zaruri = int(input("Cite zaruri avem: "))

zar_start(parti,zaruri)

# while True:
#     total = 0
#     for i in range(zaruri):
#         zar = random.randint(1, parti)
#         total += zar
#         print(f"Zar{i+1}:  " + str(zar))
    
#     print("Total: " + str(total))
#     inca = input("\nInca o data? (Enter pentru DA): ")
#     if inca:
#         break
