# Реализован класс Stationery (канцелярская принадлежность):
# в нём определен атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создано три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовано переопределение метода draw.
# Для каждого класса метод выводит уникальное сообщение.
# Созданы экземпляры классов и проверено, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = "Канцелярская принадлежность"

    def draw(self):
        print(F"Использован метод draw класса Stationery.")
        print("«Запуск отрисовки»")


class Pen(Stationery):

    def draw(self):
        print(f"Использован метод draw класса Pen.")
        print("Рисуем ручкой")


class Pencil(Stationery):

    def draw(self):
        print(f"Использован метод draw класса Pencil.")
        print("Рисуем карандашом")


class Handle(Stationery):

    def draw(self):
        print(f"Использован метод draw класса Handle.")
        print("Рисуем маркером")


if __name__ == '__main__':
    stationery = Stationery()
    print(f"{stationery.title} {stationery.__class__.__name__}")
    stationery.draw()
    pen = Pen()
    print(f"{pen.title} {pen.__class__.__name__}")
    pen.draw()
    pencil = Pencil()
    print(f"{pencil.title} {pencil.__class__.__name__}")
    pencil.draw()
    handle = Handle()
    print(f"{handle.title} {handle.__class__.__name__}")
    handle.draw()
