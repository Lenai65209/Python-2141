#  Для сложения нескольких матриц.


class Matrix():
    counter = 0

    def __init__(self, lst_of_lists):
        Matrix.counter += 1
        self.counter = Matrix.counter
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
        print(f"Матрица {self.get_name()} №", self.counter)
        for i in range(len(self.lst_of_lists)):
            for el in self.lst_of_lists[i]:
                print("%-3s%3s" % (el, ''), end="")
            print('\r')
        return '\r'

    def __radd__(self, other):
        if not isinstance(other, Matrix):
            return self
        else:
            return self.__add__(other)

    def __add__(self, other):
        # print(f"Складываем матрицу № {self.counter} и матрицу № {other.counter}.")
        rez_ls = []
        sm_both_lst_of_lists = []
        both_lst_of_lists = []
        if self.ls_ln_lists == other.ls_ln_lists:
            for (a, b) in zip(self.lst_of_lists, other.lst_of_lists):
                for (x, y) in zip(a, b):
                    sm_both_lst_of_lists.append(x + y)
                both_lst_of_lists.append(sm_both_lst_of_lists)
                sm_both_lst_of_lists = []
            # print("___________")
            matr = Matrix(both_lst_of_lists)
            # print(f"Получили матрицу № {matr.counter}.")
            return matr
        else:
            msg = f'Матрицы {self.get_name()} (матрица № {self.counter}) и {other.get_name()} (матрица № {other.counter}) разной размерности!'
            raise ValueError(msg)

    def get_name(self):
        for i, j in globals().items():
            if j is self:
                return i


if __name__ == '__main__':
    matrix = Matrix([[0, 1, 1], [1, 2, 1], [0, 1, 2]])
    print(matrix)
    matrix_1 = Matrix([[10, 1, 2], [2, 120, 2], [1, 0, 20]])
    print(matrix_1)
    matrix_2 = Matrix([[2, 1, 42], [-3, 1, 1], [0, 1, 323]])
    print(matrix_2)
    print("Сложим matrix, matrix_1 и matrix_2.")
    print(matrix + matrix_1 + matrix_2)
    matr_sm = [matrix, matrix_1, matrix_2]
    print("Воспользуемся для сложения функцией sum()")
    print(sum(matr_sm))
    matrix_3 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    matrix_4 = Matrix([[1, 2, 3], [1, 2, 3]])
    print("Сложим matrix_3 и matrix_4.")
    print(matrix_3 + matrix_4)
    # matrix_3 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2]])
