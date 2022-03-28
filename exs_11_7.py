class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = int(real_part)
        self.imaginary_part = int(imaginary_part)
        self.complex_number = complex(self.real_part, self.imaginary_part)

    def __str__(self):
        return str(self.complex_number)

    def __add__(self, other):
        res_real_part = self.real_part + other.real_part
        res_imaginary_part = self.imaginary_part + other.imaginary_part
        return ComplexNumber(res_real_part, res_imaginary_part)

    def __mul__(self, other):
        res_real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        res_imaginary_part = self.real_part * other.imaginary_part + other.real_part * self.imaginary_part
        return ComplexNumber(res_real_part, res_imaginary_part)


if __name__ == '__main__':
    complex_number_1 = ComplexNumber(20, 1)
    print(f"a = {complex_number_1}")
    complex_number_2 = ComplexNumber(10, 2)
    print(f"b = {complex_number_2}")
    print('Сложение  комплексных чисел a + b = ', complex_number_1 + complex_number_2)
    print("Умножение комплексных чисел a * b = ", complex_number_1 * complex_number_2)
    print("    Проверка.")
    a = complex(20, 1)
    print(f"a = {a}")
    b = complex(10, 2)
    print(f"b = {b}")
    print(f"Сумма a + b = {a + b}")
    print(f"Произведение a * b = {a * b}")
