# Скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия

import json
import os

same_data_path = os.path.abspath('same_data')

files_counter = 0
size_max_100 = 0
size_min_100_max_1000 = 0
size_min_1000_max_10000 = 0
size_min_10000_max_100000 = 0
els_counter = 0
statistics_dic = {}

for root, dirs, files in os.walk(same_data_path):
    for file in files:
        files_counter += 1
        f_path = os.path.join(root, file)
        file_size = os.stat(f_path).st_size
        if file_size <= 100:
            size_max_100 += 1
        elif 100 < file_size < 1000:
            size_min_100_max_1000 += 1
        elif 1000 < file_size < 10000:
            size_min_1000_max_10000 += 1
        elif 10000 < file_size < 100000:
            size_min_10000_max_100000 += 1
        else:
            els_counter += 1

print('Всего файлов: ', files_counter)
statistics_dic[100] = size_max_100
statistics_dic[1000] = size_min_100_max_1000
statistics_dic[10000] = size_min_1000_max_10000
statistics_dic[100000] = size_min_10000_max_100000
print(f'Файлов размером больше 100000, которые не попали в словарь: ', els_counter)
print("Проверка наличия подсчитанных файлов: ",
      statistics_dic[100] + statistics_dic[1000] + statistics_dic[10000] + statistics_dic[100000] + els_counter)
print("Распечатка: ")
print(f'Обычная печать: {statistics_dic}')
print("Построчная печать: ")
for key, value in statistics_dic.items():
    print(key, ':', value)
print("Печать в формате json строки: ")
print(json.dumps(statistics_dic, indent=4, sort_keys=True))
