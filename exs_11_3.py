class MyOwnError(Exception):
    pass


class OwnError(Exception):
    """The flag is set to False if a number is entered. The flag is set to True if a string is entered."""

    def __init__(self, number):
        self.number = number
        self.flag = False
        try:
            if number != "stop":
                try:
                    number = float(number)
                except ValueError:
                    self.flag = True
                    print("Это строка, не число! Повторите ввод.")
                except Exception as err:
                    self.flag = True
            else:
                self.flag = True
                raise MyOwnError("Ввод закончен.")
        except (MyOwnError, Exception) as err:
            print(f"{err}")
            self.flag = True


if __name__ == "__main__":
    ls_numb = []
    numb = input("Введите число: ")
    el_numb = OwnError(numb)
    if not el_numb.flag:
        ls_numb.append(float(numb))
    while numb != "stop":
        numb = input("Введите число: ")
        el_numb = OwnError(numb)
        if not el_numb.flag:
            ls_numb.append(float(numb))
    print("Сформирован список: ", ls_numb)
