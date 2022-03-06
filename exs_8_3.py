# декоратор для логирования типов позиционных аргументов функции (олько для одного)
from functools import wraps
from sys import argv


def type_logger(func):
    """covertly replaces the calculation of the cube of a number
    with the definition of the argument type
    """

    @wraps(func)
    def tag_wrapper(*args, **kwargs):
        tp_ar = None
        try:
            in_ar = int(args[0])
            tp_ar = type(in_ar)
            # print('tp_ar ', tp_ar)
        except:
            pass
        if tp_ar is None:
            try:
                fl_ar = float(args[0])
                tp_ar = type(fl_ar)
                # print('tp_ar ', tp_ar)
            except:
                tp_ar = type(args[0])
                # print('tp_ar ', tp_ar)
        st_res = f'{func.__name__}({args[0]}, {tp_ar})'
        return st_res

    return tag_wrapper


@type_logger
def calc_cube(x):
    """calculates the cube of a number"""
    return x ** 3


if __name__ == '__main__':
    x = argv[1]
    print(calc_cube(x))
    print(calc_cube)
