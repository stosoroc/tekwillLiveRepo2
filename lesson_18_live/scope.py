from decimal import Decimal

a = 'Bye'

CONST = Decimal('0')


def some_other_function():
    some_function()


def some_function():
    a = 'Hey'

    def change_b():
        b = 'Privet'
        a = 'Hey'
        c = 'Hola'

    def chage_c():
        pass

    change_b()


print(some_function())

print(a)
print(a)
