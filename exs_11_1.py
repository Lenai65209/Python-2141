class Date:
    @staticmethod
    def validator(date):
        dt_lst = date.split("-")
        nam_dt_lst = []
        for i in dt_lst:
            if int(i) > 0:
                nam_dt_lst.append(int(i))
        if len(nam_dt_lst) != 3:
            return False
        if nam_dt_lst[1] > 12:
            return False
        if nam_dt_lst[1] == 2:
            if nam_dt_lst[0] <= 29 and (nam_dt_lst[2] % 4 == 0 or nam_dt_lst[2] % 10 == 0):
                return True
            elif nam_dt_lst[0] <= 28:
                return True
            else:
                return False
        if 3 < nam_dt_lst[1] < 7 and nam_dt_lst[1] % 2 == 0:
            if nam_dt_lst[0] <= 30:
                return True
            else:
                return False
        if 1 <= nam_dt_lst[1] <= 7 and nam_dt_lst[1] % 2 != 0:
            if nam_dt_lst[0] <= 31:
                return True
            else:
                return False
        if 8 <= nam_dt_lst[1] <= 12 and nam_dt_lst[1] % 2 == 0:
            if nam_dt_lst[0] <= 31:
                return True
            else:
                return False
        if 8 < nam_dt_lst[1] < 12 and nam_dt_lst[1] % 2 != 0:
            if nam_dt_lst[0] <= 30:
                return True
            else:
                return False

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_number(cls, date):
        dt_lst = date.split("-")
        nam_dt_lst = []
        for i in dt_lst:
            nam_dt_lst.append(int(i))
        print('число ', nam_dt_lst[0])
        print('тип данных ', type(nam_dt_lst[0]))
        print('месяц ', nam_dt_lst[1])
        print('тип данных ', type(nam_dt_lst[1]))
        print('год ', nam_dt_lst[2])
        print('тип данных ', type(nam_dt_lst[2]))


if __name__ == "__main__":

    date = input("Введите дату в формате ДД-ММ-ГГГГ (date): ")
    print("Вызов метода класса через название класса Date.date_number(date): ")
    Date.date_number(date)
    val_date = Date(date)
    print("Вызов метода класса через экземпляр класса val_date.date_number(date) : ")
    val_date.date_number(date)
    print("Провеврка валидности даты (вызов статического метода через название класса): ", Date.validator(date))
    print("Провеврка валидности даты (вызов статического метода через объект класса): ", val_date.validator(date))
    dates = ['01-13-2020', '00-12-2020', '32-01-2020', '31-01-2020', '32-03-2020', '31-03-2020', '32-05-2020',
             '31-05-2020', '32-07-2020', '31-07-2020', '32-08-2020', '31-08-2020', '32-10-2020', '31-10-2020',
             '32-12-2020', '31-12-2020', '31-04-2020', '30-04-2020', '31-06-2020', '30-06-2020', '31-09-2020',
             '30-09-2020', '31-11-2020', '30-11-2020', '29-02-2020', '30-02-2020', '28-02-2021', '29-02-2021',
             '29-02-2016', '30-02-2016']
    print("Проверка метода класса и статического метода на данных: ")
    for date in dates:
        val_date = Date(date)
        val_date.date_number(date)
        if val_date.validator(date):
            print("Дата введена корректно.")
        else:
            print("Невалидная дата.")
