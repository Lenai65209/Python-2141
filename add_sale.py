# скрипт с интерфейсом командной строки:
# для записи данных о суммах продаж булочнойв файл 'bakery.csv'
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия
# lenai65209@rambler.ru

import os
from sys import argv

valute_name_str = argv[1]
print("Добавлена выручка: ", valute_name_str)
base_dir = os.path.dirname(__file__)
valute_name_str_path = os.path.join(base_dir, 'bakery.csv')
with open(valute_name_str_path, 'a', encoding='utf-8') as f:
    f.write(argv[1] + "\n")
