class Cell:
    def __init__(self, number_of_cells):
        try:
            self.number_of_cells = int(number_of_cells)
            print(F'Создана клетка. Количество ячеек: {self.number_of_cells}.')
        except:
            raise ValueError(f'Это не целое число: {number_of_cells}')

    def __add__(self, other):
        return self.number_of_cells + other.number_of_cells

    def __sub__(self, other):
        if self.number_of_cells >= other.number_of_cells:
            return self.number_of_cells - other.number_of_cells
        else:
            return "Ошибка! Результат отрицательный."

    def __mul__(self, other):
        total_number_of_cells = self.number_of_cells * other.number_of_cells
        common_cell = Cell(total_number_of_cells)
        mul_cell = f"Число клеток при умножении: {common_cell.number_of_cells}"
        return mul_cell

    def __floordiv__(self, other):
        total_number_of_cells = self.number_of_cells // other.number_of_cells
        common_cell = Cell(total_number_of_cells)
        floordiv_cell = f"Число клеток при делении: {common_cell.number_of_cells}"
        return floordiv_cell

    def make_order(self, cells_in_a_row):
        row = self.number_of_cells // cells_in_a_row
        # print('row', row)
        remains = self.number_of_cells % cells_in_a_row
        # print('remains', remains)
        if remains:
            print("Количество рядов: ", row + 1)
        else:
            print("Количество рядов: ", row)
        st_row = ''
        for _ in range(row):
            st_row += '*' * cells_in_a_row + "\n"
        if remains:
            st_row = st_row + '*' * remains
        else:
            st_row = st_row[:len(st_row) - 1]
        return st_row


if __name__ == '__main__':
    cell_1 = Cell(20)
    cell_2 = Cell(7)
    print('Объединение двух клеток. Количество ячеек: ', cell_1 + cell_2)
    print('Вычитание второй из первой клетки (результат больше нуля). Количество ячеек: ', cell_1 - cell_2)
    print('Вычитание первой из второй клетки (результат меньше нуля). Количество ячеек: ', cell_2 - cell_1)
    print("Умножаем клетки.")
    print(cell_2 * cell_1)
    print("Делим клетки.")
    print(cell_1 // cell_2)
    print("    Проверка метода .make_order()")
    print(f"В этой клетке {cell_1.number_of_cells} ячеек.")
    print("    Количество ячеек в ряду 5")
    print(cell_1.make_order(5))
    print("    Количество ячеек в ряду 10")
    print(cell_1.make_order(10))
    print("    Количество ячеек в ряду 3")
    print(cell_1.make_order(3))
    print(f"В этой клетке {cell_2.number_of_cells} ячеек.")
    print("    Количество ячеек в ряду 5")
    print(cell_2.make_order(5))
    print("    Количество ячеек в ряду 10")
    print(cell_2.make_order(10))
    print("    Количество ячеек в ряду 3")
    print(cell_2.make_order(3))
