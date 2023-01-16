import random


def roll_dice(sides, number_of_dice):
    sum_of_dice = 0
    for i in range(number_of_dice):
        dice_roll = random.randint(1, sides)
        print('Dice', i + 1, dice_roll)
        sum_of_dice += dice_roll
    print('Suma: ', sum_of_dice)


if __name__ == '__main__':
    nr_of_sides = input("Numarul de laturi:")
    number_of_dices = input("Numarul de zaruri:")
    while True:
        next = input('Apasati enter pentru a continua, scrie ceva pentru a opri')
        if next:
            break
        roll_dice(int(nr_of_sides), int(number_of_dices))
