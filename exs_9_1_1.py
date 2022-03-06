# Создан класс TrafficLight (светофор):
# У него один атрибут color (цвет) и метод running (запуск);
# атрибут реализован как приватный;
# в рамках метода реализовао переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — 7 секунд;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# работа примера проверена, созданием экземпляра и вызвом описанного метода.
# Светофор не ломается.

import time


class TrafficLight:
    __color = "цвета нет"
    counter_trafficLight = 0

    def __init__(self):
        TrafficLight.counter_trafficLight += 1
        self.id = TrafficLight.counter_trafficLight

    def running(self):
        print(f"Светофор id {self.id} работает! \n The traffic light id {self.id} is working!")
        print('TrafficLight.__color: ')
        TrafficLight.__color = "\033[7m\033[31m {} \033[K"
        print(TrafficLight.__color.format("Горит красный сигнал светофора!!!"), end='', flush=True)
        time.sleep(7)
        TrafficLight.__color = "\r\033[33m {} \033[K"
        print("\r\033[33m {} \033[K ".format("Внимание, желтый!"), end='', flush=True)
        time.sleep(2)
        TrafficLight.__color = "\r\033[32m {} \033[K"
        print(TrafficLight.__color.format("= ) Зеленый = )"), end='', flush=True)
        time.sleep(7)
        TrafficLight.__color = '\r\033[0m{}\033[K '
        print(TrafficLight.__color.format(' '))
        TrafficLight.__color = "цвета нет"


if __name__ == '__main__':
    trafficLight = TrafficLight()
    try:
        print(TrafficLight.__color)
    except AttributeError:
        print("AttributeError: type object 'TrafficLight' has no attribute '__color'")
    check = trafficLight._TrafficLight__color
    print("trafficLight._TrafficLight__color: ", check)
    TrafficLight.running(trafficLight)
    trafficLight = TrafficLight()
    try:
        print(TrafficLight.__color)
    except AttributeError:
        print("AttributeError: type object 'TrafficLight' has no attribute '__color'")
    check = trafficLight._TrafficLight__color
    print("trafficLight._TrafficLight__color: ", check)
    TrafficLight.running(trafficLight)
    trafficLight = TrafficLight()
    TrafficLight.running(trafficLight)
