# Просто запуск скрипта — выводит все записи;
# Запуск скрипта с одним параметром - числом
# — выводит все записи с номера, равного этому числу, до конца;
# Запуск скрипта с двумя числами 
# — выводит записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Ошибки не обработаны.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия
# lenai65209@rambler.ru

from itertools import islice
from sys import argv

if len(argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        lines = islice(f, 1, None)
        print('', *lines)
elif len(argv) == 2:
    valute_name = int(argv[1])
    print('valute_name', valute_name)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        lines = islice(f, valute_name, None)
        print('', *lines)
else:
    valute_name = int(argv[1])
    valute_name_1 = int(argv[2])
    print('valute_name_str_1', valute_name_1)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        lines = islice(f, valute_name, valute_name_1 + 1)
        print('', *lines)
