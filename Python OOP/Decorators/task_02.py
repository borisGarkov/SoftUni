import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for ar in args:
            if not isinstance(ar, int) or ar % 2 != 0:
                return "Please use only even numbers!"
        return func(*args, **kwargs)

    return wrapper


@even_parameters
def func():
    return "hi"


result = func()
