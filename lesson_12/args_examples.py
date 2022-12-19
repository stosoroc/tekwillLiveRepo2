
def do_something(connection,
                 something_else,
                 number_of_times,
                 number_of_retries=5,
                 ignore_error=False
                 ):
    print(connection,
          something_else,
          number_of_times,
          number_of_retries,
          ignore_error)

do_something(
    connection=None,
    something_else=10,
    number_of_times=20,
    ignore_error=True
)
do_something(
    connection=None,
    something_else=10,
    number_of_times=20,
    number_of_retries=10
)

def add_example(a: str = 0, b:str = 0):
    print(a+b)
    
add_example()