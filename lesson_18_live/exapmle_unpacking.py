def fun(*args):
    # print(1, 2, 3, sep=' | ')
    print(*args, sep=' | ')


def boo(*args):
    print(args, sep=' | ')


fun(1, 2, 3, 12, 1, 2, 2, 3, 4)
boo(1, 2, 3)

example = [1, 2, 3, 45, 1, 2, 12, 3, 12, 3]
fun(example)
fun(*example)


def baz(arg1, arg2, arg3=None):
    print(arg1)
    print(arg2)
    print(arg3)


args_for_baz = [1, 2]

baz(*args_for_baz)


def create_list(*elements):
    return list(elements)
