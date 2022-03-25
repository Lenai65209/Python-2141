from abc import ABCMeta, abstractproperty


class Clothes():
    __metaclass__ = ABCMeta

    @abstractproperty
    def fabric_consumption():
        """calculation of fabric consumption"""

    pass


class Coat(Clothes):
    def __init__(self, v_size):
        self.v_size = v_size

    @property
    def fabric_consumption(self):
        print('Расход ткани на пошив пальто: ', self.v_size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, h_height):
        self.h_height = h_height

    @property
    def fabric_consumption(self):
        print('Расход ткани на пошив костюма: ', 2 * self.h_height + 0.3)


if __name__ == '__main__':
    coat = Coat(13)
    coat.fabric_consumption
    suit = Suit(1.60)
    suit.fabric_consumption
