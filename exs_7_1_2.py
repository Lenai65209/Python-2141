# Созданме стартера. Создает файлы и папки до четвертого уровня вложенности. Поясняет сделанное.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия

import os
from pathlib import Path

import yaml

DIC_TREE_1 = {
    'my_project': [{'settings': ['__init__.py', 'dev.py', 'prod.py']}, {'mainapp': ['__init__.py', 'models.py',
                                                                                    'views.py', {'templates': [
            {'mainapp': ['base.html', 'index.html']}]}]}, {'authapp': ['__init__.py', 'models.py', 'views.py',
                                                                       {'templates': [
                                                                           {'authapp': ['base.html',
                                                                                        'index.html']}]}]}]}

base_dir = os.path.dirname(__file__)
project_tree_path = os.path.join(base_dir, 'project_tree_7_1.yml')

with open(project_tree_path, 'w') as file:
    dy = []
    dy.append(DIC_TREE_1)
    documents = yaml.dump(dy, file)
with open(project_tree_path) as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)
    doc_tree = doc[0]
    print(f'Я прочитал словарь из файла YAML: ', doc_tree)
for key in doc_tree:
    dir_name = key
    project_tree_dir_path = Path(base_dir, key)
    if not os.path.exists(project_tree_dir_path):
        os.mkdir(project_tree_dir_path)
        print("Создал: ", project_tree_dir_path)
    else:
        print(f'Папка {os.path.abspath(key)} уже есть.')
    ls_key = doc_tree[key]
    for el in ls_key:
        if type(el) is dict:
            for key_el in el:
                project_tree_dir_folder_1_path = Path(project_tree_dir_path, key_el)
                if not (os.path.exists(project_tree_dir_folder_1_path)):
                    os.makedirs(project_tree_dir_folder_1_path)
                    print('Я создал папку перврго уровня вложенности: ', project_tree_dir_folder_1_path)
                else:
                    print(f'Папка первого уровня вложенности {project_tree_dir_folder_1_path} уже есть.')
                el_key = el[key_el]
                for el in el_key:
                    if type(el) is dict:
                        for key_el in el:
                            project_tree_dir_folder_2_path = Path(project_tree_dir_folder_1_path, key_el)
                            if not os.path.exists(project_tree_dir_folder_2_path):
                                os.makedirs(project_tree_dir_folder_2_path)
                                print('Я создал папку второго уровня вложенности: ', project_tree_dir_folder_2_path)
                            else:
                                print(f'Папка второго уровня вложенности {project_tree_dir_folder_2_path} уже есть.')
                            el_key = el[key_el]
                            for el in el_key:
                                if type(el) is dict:
                                    for key_el in el:
                                        project_tree_dir_folder_3_path = Path(project_tree_dir_folder_2_path, key_el)
                                        if not os.path.exists(project_tree_dir_folder_3_path):
                                            os.makedirs(project_tree_dir_folder_3_path)
                                            print('Я создал папку третьего уровня вложенности: ',
                                                  project_tree_dir_folder_3_path)
                                        else:
                                            print(
                                                f'Папка третьего уровня вложенности {project_tree_dir_folder_3_path} уже есть.')
                                        el_key = el[key_el]
                                        for el in el_key:
                                            if type(el) is not dict:
                                                project_tree_dir_file_4_path = Path(project_tree_dir_folder_3_path,
                                                                                    el)
                                                if not (os.path.isfile(project_tree_dir_file_4_path)):
                                                    with open(project_tree_dir_file_4_path, 'w') as file:
                                                        print('Я создал файл на четвертом уровне вложенности: ',
                                                              project_tree_dir_file_4_path)
                                                else:
                                                    print(
                                                        f'Файл четвертого уровня вложенности {project_tree_dir_file_4_path} уже есть.')

                                else:
                                    project_tree_dir_file_3_path = Path(project_tree_dir_folder_2_path, el)
                                    if not (os.path.isfile(project_tree_dir_file_3_path)):
                                        with open(project_tree_dir_file_3_path, 'w') as file:
                                            print('Я создал файл на третьем уровне вложенности: ',
                                                  project_tree_dir_file_3_path)
                                    else:
                                        print(
                                            f'Файл третьего уровня вложенности {project_tree_dir_file_3_path} уже есть.')

                    else:
                        project_tree_dir_file_2_path = Path(project_tree_dir_folder_1_path, el)
                        if not (os.path.isfile(project_tree_dir_file_2_path)):
                            with open(project_tree_dir_file_2_path, 'w') as file:
                                print('Я создал файл на втором уровне вложенности: ',
                                      project_tree_dir_file_2_path)
                        else:
                            print(f'Файл третьего уровня вложенности {project_tree_dir_file_2_path} уже есть.')

        else:
            project_tree_dir_file_path = Path(base_dir, el)
            if not (os.path.isfile(project_tree_dir_file_path)):
                with open(project_tree_dir_file_path, 'w') as file:
                    print(f"Создал файл в каталоге проекта: ", project_tree_dir_file_path)
                    continue
            else:
                print(f'Файл в каталоге проекта {project_tree_dir_file_path} уже есть.')
