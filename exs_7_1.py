# скрипт, создающий стартер (заготовку) для проекта со структурой папок из словаря
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия

import os
from pathlib import Path

import yaml

DIC_TREE = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def mk_my_folders(project_name, folders_name):
    """
    creates a directory and folders in it

   :param project_name: directory name
          folders_name: folder list
    """

    base_dir = os.path.dirname(__file__)
    project_tree_dir_path = Path(base_dir, project_name)
    if not os.path.exists(project_tree_dir_path):
        os.mkdir(project_tree_dir_path)
    for folder_name in folders_name:
        folder_tree_dir_path = Path(project_tree_dir_path, folder_name)
        if not os.path.exists(folder_tree_dir_path):
            os.makedirs(folder_tree_dir_path)


base_dir = os.path.dirname(__file__)
project_tree_path = os.path.join(base_dir, 'project_tree_7_3.yml')

with open(project_tree_path, 'w') as file:
    documents = yaml.dump(DIC_TREE, file)
with open(project_tree_path) as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)
    doc_tree = doc
    print(f'Я прочел из файла YAML словарь со структурой папок: {doc_tree}')

for key, val in doc_tree.items():
    mk_my_folders(key, val)
    print(f'Из ключей я соэдал каталог в рабочей директории: {key}')
    print("Вот он:", os.path.abspath(key))
    print(f'В этом каталоге я создал папки:')
    os.chdir(os.path.abspath(key))
    for el in val:
        print(f' -{el}')
        print("путь к папке:", os.path.abspath(el))
