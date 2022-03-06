# Реализован класс Road (дорога).
# определены атрибуты: length (длина), width (ширина);
# значения атрибутовпередаются при создании экземпляра класса;
# атрибуты сделаны защищёнными;
# определен метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использована формула: # длина * ширина * масса асфальта для покрытия одного кв.метра
# дороги асфальтом, толщиной в 1 см * число см толщины полотна
# проверена работа метода.

class Road:
    """
       class for calculating the mass of asphalt to cover the road.
       ...
       attributes
       --------
       _length : int or float (entered in meters)
       _width : int or float (entered in meters)
       height : int or float (entered in centimeters), by default, 5 cm

       methods
       ------
       asphalt_mass(self):
           calculating the mass of asphalt to cover the road.
       """
    __weight_per_1_m_1_m_1_cm = 25

    def __init__(self, width, length, height=5):
        """
        Sets all the necessary attributes for the road object.
        Parameters
        ---------
        _width : int or float (entered in meters)
        _length : int or float (entered in meters)
        height : int or float (entered in centimeters), by default, 5 cm
        """
        self._width = width
        self._length = length
        self.height = height
        Road.asphalt_mass(self)

    def asphalt_mass(self):
        """
        Outputs the estimated mass of asphalt to cover the road.
        If the height argument is not specified, it considers it equal to 5 cm.
        parameters
        ---------
        accepts parameters when creating a class
        and calculates the mass of asphalt to cover the road.
        prints the received value
        return value
        ---------------------
        None
        """
        need_tons_of_asphalt = self._width * self._length * self._Road__weight_per_1_m_1_m_1_cm * self.height / 1000
        print(
            f'Для покрытия догоги шириной {self._width} и длиной {self._length} (при высоте покрвтия {self.height} см) нужно {int(need_tons_of_asphalt)} т асфальта.')


if __name__ == '__main__':
    road_exs = Road(20, 5000)
    road = Road(9, 89000)
    # print(Road.__doc__)
    # help(Road)
