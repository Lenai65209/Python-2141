# Созданме стартера. С описанием процесса.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия

import os
import re
from pathlib import Path

import yaml

FILENAME = 'tree.txt'
filename_path = os.path.abspath(FILENAME)
my_key = []
my_str = ""
flag = True
lst_tree = []
dic_tree = {}
try:
    with open(filename_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line[0] == '|':
                project = re.sub("\|--|\|", "", line).strip()
            else:
                sp_ext = line.split(".")
                if len(sp_ext) == 1:
                    sp_ext_1 = line.split()
                    exam = sp_ext[0]
                    exam_key = re.sub("\|--|\|", "", exam)
                    if flag == False and exam_key.strip() != "templates":
                        my_key = []
                    flag = True
                else:
                    flag = False
                if flag == True:
                    to_key = sp_ext[0]
                    line_key = re.sub("\|--|\|", "", to_key)
                    my_key.append(line_key.strip())
                else:
                    my_str = ""
                    if len(sp_ext) != 1:
                        flag = False
                        to_key = sp_ext[0]
                        line_key = re.sub("\|--|\|", "", to_key)
                        my_ext = sp_ext[-1].strip('\n')
                        name_file = line_key.strip() + '.' + my_ext
                        for el in my_key:
                            my_str += el + '/'
                        my_path = my_str + name_file
                        lst_tree.append(my_path)

        dic_tree[project] = lst_tree

except Exception as e:
    print(f'error: {e}')

print(f'Прочитали из файла {filename_path}: \n', dic_tree)  # Дадее его не используем.
# Можно было передать в exs_7_1_2.py в виде функции чтения файла, но на реализацию времени не хватило.

print("Далее читали из YAML")

project_tree_path = os.path.abspath('project_tree.yml')

with open(project_tree_path) as file:  # Читаем из файла YAML
    documents = yaml.load(file, Loader=yaml.FullLoader)

for key in documents[0]:
    ls_key = documents[0][key]
    base_dir = os.path.dirname(__file__)
    dir_name = key
    project_tree_dir_path = Path(base_dir, key)
    if not os.path.exists(project_tree_dir_path):
        os.mkdir(project_tree_dir_path)
        print("Создал: ", project_tree_dir_path)
    else:
        print(f'Директория {project_tree_dir_path} уже есть.')
    for el in ls_key:
        length_lst = os.path.split(el)
        project_tree_dir_folder_path = length_lst[0]
        project_tree_dir_el_folder_path = Path(project_tree_dir_path, project_tree_dir_folder_path)
        if not os.path.exists(project_tree_dir_el_folder_path):
            os.makedirs(project_tree_dir_el_folder_path)
            print("Создал: ", project_tree_dir_el_folder_path)
        else:
            print(f'Папка {project_tree_dir_el_folder_path} уже есть.')
        project_file = length_lst[1]
        project_tree_dir_el_folder_file_path = Path(project_tree_dir_el_folder_path, project_file)
        if not (os.path.isfile(project_tree_dir_el_folder_file_path)):
            with open(project_tree_dir_el_folder_file_path, 'w') as file:
                print("Создал: ", os.path.abspath(project_file))
                continue
        else:
            print(f'Файл {project_tree_dir_el_folder_file_path} существует.')
