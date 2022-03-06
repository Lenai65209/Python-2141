# декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так.

from functools import wraps
from sys import argv


def val_checker(f_lambda):
    """checking the input values of the function and
    throwing a ValueError exception if something is wrong
    """

    def _logger(func):
        @wraps(func)
        def wrapper(*args):
            try:
                if f_lambda(int(args[0])):
                    result = func(int(args[0]))
                else:
                    msg = f"wrong val: {args[0]}"
                    raise ValueError(msg)
            except:
                msg = f"wrong val: {args[0]}"
                raise ValueError(msg)
            return result

        return wrapper

    return _logger


@val_checker(lambda x: x > 10)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    x = argv[1]
    print(calc_cube(x))
    print(calc_cube)
