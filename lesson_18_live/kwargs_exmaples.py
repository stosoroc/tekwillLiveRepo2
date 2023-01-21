def func(url, data):
    print(url, data)


def func_2(nr_of_retries, *args, **kwargs):
    print(nr_of_retries)
    if not 'url' in kwargs:
        raise Exception('URL MIssing')
    func(*args, **kwargs)


func_2(2, url='google.com', data=None)

to_send_to_func = dict(
    url='google.com',
    data=dict(message="Hello")
)

func_2(3, **to_send_to_func)
