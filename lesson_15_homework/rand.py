# Using the Random Module, create a small 
# program that will simulate 2 x 6 sided dice.
# The programm should allow the user to roll the dice, 
# and show the values on each dice, and the total sum.

import random
print()
while True:
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    total = zar1 + zar2
    print("Un  Zar: " + str(zar1))
    print("Alt Zar: " + str(zar2))
    print("Total:   " + str(total))
    inca = input("\nInca o data? (Enter pentru DA): ")
    if inca:
        break

