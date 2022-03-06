# Создан класс TrafficLight (светофор):
# У него один атрибут color (цвет) и метод running (запуск);
# атрибут реализован как приватный;
# в рамках метода реализовао переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — 7 секунд;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# работа примера проверена, созданием экземпляра и вызвом описанного метода.
# Реализована проверка порядка режимов.
# При его нарушении выводится соответствующее сообщение и завершается скрипт.
import time


class TrafficLight:
    __color = "цвета нет"
    counter_trafficLight = 0

    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        TrafficLight.counter_trafficLight += 1
        self.id = TrafficLight.counter_trafficLight

    def running(self):
        if self.red == 'красный' and self.yellow == "желтый" and self.green == "зеленый":
            print(f"Светофор id {self.id} работает! \n The traffic light id {self.id} is working!")
            print('TrafficLight.__color: ')
            TrafficLight.__color = "\033[7m\033[31m {} \033[K"
            print(TrafficLight.__color.format(self.red), end='', flush=True)
            time.sleep(7)
            TrafficLight.__color = "\r\033[33m {} \033[K"
            print("\r\033[33m {} \033[K ".format(self.yellow), end='', flush=True)
            time.sleep(2)
            TrafficLight.__color = "\r\033[32m {} \033[K"
            print(TrafficLight.__color.format(self.green), end='', flush=True)
            time.sleep(7)
            TrafficLight.__color = '\r\033[0m{}\033[K '
            print(TrafficLight.__color.format(' '))
            TrafficLight.__color = "цвета нет"
        else:
            raise ValueError(f'Светофор id {self.id} сломался! \n The traffic light id {self.id} is broken!')


if __name__ == '__main__':
    trafficLight = TrafficLight('красный', "желтый", "зеленый")
    try:
        print(TrafficLight.__color)
    except AttributeError:
        print("AttributeError: type object 'TrafficLight' has no attribute '__color'")
    check = trafficLight._TrafficLight__color
    print("trafficLight._TrafficLight__color: ", check)
    TrafficLight.running(trafficLight)
    trafficLight = TrafficLight('красный', "желтый", "зеленый")
    try:
        print(TrafficLight.__color)
    except AttributeError:
        print("AttributeError: type object 'TrafficLight' has no attribute '__color'")
    check = trafficLight._TrafficLight__color
    print("trafficLight._TrafficLight__color: ", check)
    TrafficLight.running(trafficLight)
    trafficLight = TrafficLight("зеленый", "желтый", 'красный')
    TrafficLight.running(trafficLight)
