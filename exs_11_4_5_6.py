class Warehouse:
    @staticmethod
    def ware_quantity(quant, flag=True):
        try:
            quanty = int(quant)
        except ValueError:
            flag = False
            print("Количество не может быть строкой. Повторите ввод.")
        return flag

    def __init__(self, warehouse_name, my_dict={}):
        self.warehouse_name = warehouse_name
        self.my_dict = my_dict

    def arrival(self, ware, quantity):
        print(F"    Количество поступающего товара {ware}: ", quantity)
        if Warehouse.ware_quantity(quantity):
            if ware not in self.my_dict.keys():
                self.my_dict[ware] = quantity
            else:
                self.my_dict[ware] = self.my_dict[ware] + quantity
            return (f'Остатки товара: {self.my_dict}')

    def consumption(self, ware, quantity):
        if ware not in self.my_dict:
            print(f"    Товар {ware} отсутствует на складе.")
        elif self.my_dict[ware] < quantity:
            print(f"    Товара {ware} недостаточно. На остатках {self.my_dict[ware]} шт.")
        else:
            self.my_dict[ware] = self.my_dict[ware] - quantity
            if self.my_dict[ware] == 0:
                del self.my_dict[ware]
                print(f"    Товара {ware} больше нет на остатке.")
        return (f'Остатки товара: {self.my_dict}')


class OfficeEquipment:
    equ_count = 0

    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brend = brand
        OfficeEquipment.equ_count += 1


class Printer(OfficeEquipment):
    printer_count = 0

    def __init__(self, name, price, brand, print_color, printing_technology, availability_of_functions, print_format):
        super().__init__(name, price, brand)
        self.print_color = print_color
        self.printing_technology = printing_technology
        self.availability_of_functions = availability_of_functions
        self.print_format = print_format
        Printer.printer_count += 1

    def __repr__(self):
        return f'{self.name} {self.brend} {self.print_color} цена {self.price}'


class Scanner(OfficeEquipment):
    scanner_count = 0

    def __init__(self, name, price, brand, dots_per_inch, color_depth, scan_field_size):
        super().__init__(name, price, brand)
        self.dots_per_inch = dots_per_inch
        self.color_depth = color_depth
        self.scan_field_size = scan_field_size
        Scanner.scanner_count += 1

    def __repr__(self):
        return f'{self.name} {self.brend} цена {self.price}'


class Copier(OfficeEquipment):
    copier_count = 0

    def __init__(self, name, price, brand, chroma, paper_format, number_of_copies, dpi, print_speed):
        super().__init__(name, price, brand)
        self.chroma = chroma
        selfюpaper_format = paper_format
        self.number_of_copies = number_of_copies
        self.dpi = dpi
        self.print_speed = print_speed
        Copier.copier_count += 1

    def __repr__(self):
        return f'{self.name} {self.brend} цена {self.price}'


if __name__ == "__main__":
    warehouse = Warehouse("Первый")
    printer = Printer('printer', 50000, "HP", "цветной", "лазерный", "МФУ", "А4")
    print(warehouse.arrival(printer, "р"))
    print(warehouse.arrival(printer, 3))
    printer_1 = Printer('printer', 30000, "Samsung", "чрно-белая печать", "лазерный", "МФУ", "А4")
    print(warehouse.arrival(printer_1, 3))
    scanner = Scanner('scanner', 10000, "HP", "1200x1200 dpi", "48 бит", "А4")
    print(warehouse.arrival(scanner, 2))
    scanner_1 = Scanner('scanner', 7000, "Canon", "1200x1200 dpi", "36 бит", "А4")
    print(warehouse.arrival(scanner_1, 2))
    print(warehouse.consumption("copier", 6))
    print(warehouse.consumption(scanner, 5))
    print(warehouse.consumption(scanner, 2))
    сopier = Copier("сopier", 40000, "Xerox", "черно-белая печать", "А4", 6000, "До 1200 dpi", "30 стр/мин")
    print(warehouse.arrival(сopier, 1))
