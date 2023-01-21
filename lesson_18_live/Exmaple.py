print(1, 2, 3, sep=' | ')


def new_function(arg1, arg2, arg3, arg4):
    pass


def new_function_with_default(arg1, arg2, arg3, arg4=None):
    pass


new_function(1, 2, 3, 4)

# new_function(
#     arg2=4,
#     arg3=3,
#     arg1=1,
# ) # ERROR
new_function(1, 2, 3, 4)
new_function_with_default(1, 2, 3)
