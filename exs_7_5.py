# Cкрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# значения — кортежи вида (<files_quantity>, [<files_extensions_list>]).
# результаты сохранены в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
# скрипт exs_7_5.py находится в папке venv, откуда его и запускали.

import json
import os
from pprint import pprint

import yaml

same_data_path = os.path.abspath('same_data')

files_counter = 0
size_max_100 = 0
size_min_100_max_1000 = 0
size_min_1000_max_10000 = 0
size_min_10000_max_100000 = 0
els_counter = 0
statistics_dic = {}
files_extensions_st_max_100 = set()
files_extensions_st_min_100_max_1000 = set()
files_extensions_st_min_1000_max_10000 = set()
files_extensions_st_min_10000_max_100000 = set()
for root, dirs, files in os.walk(same_data_path):
    for file in files:
        files_counter += 1
        f_path = os.path.join(root, file)
        file_ext = os.path.splitext(file)[1][1:]
        file_size = os.stat(f_path).st_size
        if file_size <= 100:
            size_max_100 += 1
            statistics_dic = {}
            if file_ext not in files_extensions_st_max_100:
                files_extensions_st_max_100.add(file_ext)
        elif 100 < file_size < 1000:
            size_min_100_max_1000 += 1
            if file_ext not in files_extensions_st_min_100_max_1000:
                files_extensions_st_min_100_max_1000.add(file_ext)
        elif 1000 < file_size < 10000:
            size_min_1000_max_10000 += 1
            if file_ext not in files_extensions_st_min_1000_max_10000:
                files_extensions_st_min_1000_max_10000.add(file_ext)
        elif 10000 < file_size < 100000:
            size_min_10000_max_100000 += 1
            if file_ext not in files_extensions_st_min_10000_max_100000:
                files_extensions_st_min_10000_max_100000.add(file_ext)
        else:
            els_counter += 1

print('Всего файлов: ', files_counter)
statistics_dic[100] = (size_max_100, list(files_extensions_st_max_100))
statistics_dic[1000] = (size_min_100_max_1000, list(files_extensions_st_min_100_max_1000))
statistics_dic[10000] = (size_min_1000_max_10000, list(files_extensions_st_min_1000_max_10000))
statistics_dic[100000] = (size_min_10000_max_100000, list(files_extensions_st_min_10000_max_100000))
print(f'Получили словарь со статистикой: {statistics_dic}')
print(f'Файлов размером больше 100000, которые не попали в словарь: ', els_counter)
print("Проверка наличия подсчитанных файлов: ",
      statistics_dic[100][0] + statistics_dic[1000][0] + statistics_dic[10000][0] + statistics_dic[100000][
          0] + els_counter)
print("Распечатка: ")
print(f'Обычная печать: {statistics_dic}')
print("Построчная печать: ")
print("{")
for key, value in statistics_dic.items():
    print("    ", key, ':', value)
print("}")
print('Заспечатка с помощью pprint: ')
pprint(statistics_dic)

base_dir = os.path.dirname(__file__)
venv_summary_json = os.path.join(base_dir, 'venv_summary.json')
data = json.dumps(statistics_dic, sort_keys=True)
with open(venv_summary_json, 'w') as file:
    json.dump(data, file)
with open(venv_summary_json, 'r') as file:
    json.load(file)
print("Запмсали и прочли файл в JSON.")
print("Ключи словарей JSON всегда являются строками.")
print('Печатаем содержание файла venv_summary.json: ', data)
venv_summary_yml = os.path.join(base_dir, 'venv_summary.yml')
with open(venv_summary_yml, 'w') as file:
    yaml.dump(statistics_dic, file)
with open(venv_summary_yml, 'r') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)
print("Запмсали и прочли файл в YAML.")
print("Ключи словарей YAML могут быть числами.")
print('Печатаем содержание файла venv_summary.yml: ', doc)
