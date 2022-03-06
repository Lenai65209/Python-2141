# Реализован базовый класс Worker (работник):
# определены атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен является защищённым и ссылается на словарь,
# содержащий элементы «оклад» и «премия»: {"wage": wage, "bonus": bonus};
# создан класс Position (должность) на базе класса Worker;
# в классе Position реализован метод получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверена работа примера на реальных данных:
# создан экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызваны методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(F"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        try:
            print(self.__income)
        except AttributeError:
            print("AttributeError: 'Position' object has no attribute '_Position__income'")
        total_income = self._Worker__income["wage"] + (
                self._Worker__income["wage"] / 100 * self._Worker__income["bonus"])
        print(f'Доход с учётом премии: {total_income}')


if __name__ == '__main__':
    position_1 = Position("Иван", "Петров", "директор", 100000, 20)
    position_1.get_full_name()
    print(f"Занимаемая должность: {position_1.position}.")
    try:
        print(position_1.wage)
    except AttributeError:
        print("AttributeError: 'Position' object has no attribute 'wage'")
    print(f'Оклад {position_1._Worker__income["wage"]}.')
    try:
        print(position_1.bonus)
    except AttributeError:
        print("AttributeError: 'Position' object has no attribute 'bonus'")
    print(f'Премия {position_1._Worker__income["bonus"]} %.')
    position_1.get_total_income()
    position_2 = Position("Федор", "Сидоров", "бухгалтер", 90000, 15)
    position_2.get_full_name()
    print(f"Занимаемая должность: {position_2.position}.")
    position_2.get_total_income()
    position_3 = Position("Петр", "Иванов", "инженер", 90000, 20)
    position_3.get_full_name()
    print(f"Занимаемая должность: {position_3.position}.")
    position_3.get_total_income()
