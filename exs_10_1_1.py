#  Только для сложения двух матриц.

class Matrix():

    def __init__(self, lst_of_lists):
        self.lst_of_lists = lst_of_lists
        ls_ln_lists = []
        for i in range(len(lst_of_lists)):
            self.i = lst_of_lists[i]
            ls_ln_lists.append(len(lst_of_lists[i]))
        self.ls_ln_lists = ls_ln_lists
        self.ln_matrix = len(lst_of_lists)
        nam = ls_ln_lists[0]

        for i in range(1, len(ls_ln_lists)):
            if nam != ls_ln_lists[i]:
                msg = 'Это не матрица!'
                raise ValueError(msg)

    def __str__(self):
        for i in range(len(self.lst_of_lists)):
            for el in self.lst_of_lists[i]:
                print("%-3s%3s" % (el, ''), end="")
            print('\r')
        return '\r'

    def __add__(self, other):
        print(self, end='')
        print("+")
        print(other, end='')
        print("--------------")
        rez_ls = []
        if self.ls_ln_lists == other.ls_ln_lists:
            for (a, b) in zip(self.lst_of_lists, other.lst_of_lists):
                for (x, y) in zip(a, b):
                    print("%-3s%3s" % (x + y, ''), end="")
                print('\r')
            return ''
        else:
            msg = 'Матрицы разной размерности!'
            raise ValueError(msg)

        def __radd__(self, other):
            if not isinstance(other, Matrix):
                return self
            else:
                return self.__add__(other)


if __name__ == '__main__':
    matrix = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    matrix_1 = Matrix([[2, 3, 4], [2, 3, 4], [2, 3, 4]])
    print(matrix + matrix_1)
    matrix = Matrix([[0, 1, 2], [23, 4, 5], [6, 7, 8]])
    matrix_1 = Matrix([[9, 1, 8], [-1, 10, 5], [-1, 2, 2]])
    print(matrix + matrix_1)
