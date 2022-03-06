# Реализован базовый класс Car:
# у класса следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые сообщают, что машина поехала, остановилась, повернула (куда);
# описано несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# в базовый класс добавлен метод show_speed, который показывает текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределен метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) выводится сообщение о превышении скорости.
#
# Созданы экземпляры классов, переданы значения атрибутов.
# Выполнен доступ к атрибутам, выведен результат. Вызованы методы и показн результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name}, go!")

    def stop(self):
        print(f"{self.name}, stop!")

    def turn(self, direction):
        print(f"{self.name}, turn {direction}!")

    def show_speed(self):
        print(f"The speed of the {self.name} is {self.speed} km/h.")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self, direction):
        super().turn(direction)

    def show_speed(self):
        print(f"The speed of the {self.name} is {self.speed} km/h.")
        if self.speed > 60:
            print("The speed is exceeded!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self, direction):
        super().turn(direction)

    def show_speed(self):
        super().show_speed()


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self, direction):
        super().turn(direction)

    def show_speed(self):
        print(f"The speed of the {self.name} is {self.speed} km/h.")
        if self.speed > 40:
            print("The speed is exceeded!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name)
        self.is_police = True

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self, direction):
        super().turn(direction)

    def show_speed(self):
        super().show_speed()


if __name__ == '__main__':
    car = Car(100, "white", "Car")
    print(f"It's a {car.color} {car.name}.")
    print(f"Class name: {car.__class__.__name__}.")
    car.go()
    car.stop()
    car.turn("left")
    car.turn("right")
    car.show_speed()
    print(f"Is this a police car? {car.is_police}.")
    town_car = TownCar(100, "red", "Lada")
    print(f"This is the {town_car.color} {town_car.name}.")
    print(f"Class name: {town_car.__class__.__name__}.")
    town_car.go()
    town_car.stop()
    town_car.turn("left")
    town_car.turn("right")
    town_car.show_speed()
    print(f"Is this a police car? {town_car.is_police}.")
    sport_car = SportCar(350, "blue", "Audi R8")
    print(f"It's a {sport_car.color} {sport_car.name}.")
    print(f"Class name: {sport_car.__class__.__name__}.")
    sport_car.go()
    sport_car.stop()
    sport_car.turn("left")
    sport_car.turn("right")
    sport_car.show_speed()
    print(f"Is this a police car? {sport_car.is_police}.")
    work_car = WorkCar(50, "orange", "Tractor")
    print(f"Class name: {work_car.__class__.__name__}.")
    print(f"It's an {work_car.color} {work_car.name}.")
    work_car.go()
    work_car.stop()
    work_car.turn("left")
    work_car.turn("right")
    work_car.show_speed()
    print(f"Is this a police car? {work_car.is_police}.")
    police_car = PoliceCar(150, "blue and white", "Ford")
    print(f"Class name: {police_car.__class__.__name__}.")
    print(f"It's a {police_car.color} {police_car.name}.")
    police_car.go()
    police_car.stop()
    police_car.turn("left")
    police_car.turn("right")
    police_car.show_speed()
    print(f"Is this a police car? {police_car.is_police}.")
