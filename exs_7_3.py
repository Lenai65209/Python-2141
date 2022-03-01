# Сбор всех шаблонов в одну папку templates проекта. Без комментариев.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия

import os
import shutil
from pathlib import Path

ls_dir = []
my_project_path = os.path.abspath('my_project')
my_project_templates = Path(my_project_path, "templates")
if not os.path.exists(my_project_templates):
    os.makedirs(my_project_templates)

for root, dirs, files in os.walk(my_project_path):
    for dir in dirs:
        if dir == 'templates' and os.path.join(root, dir) != os.path.join(my_project_path, dir):
            ls_dir.append(os.path.join(root, dir))

if not os.path.exists(my_project_templates):
    os.makedirs(my_project_templates)

for el in ls_dir:
    source_dir = el
    target_dir = my_project_templates

    file_names = os.listdir(source_dir)
    for root, dirs, files in os.walk(source_dir):
        for dir in dirs:
            my_copy_templates = Path(my_project_path, 'templates', dir)
            if not os.path.exists(my_copy_templates):
                os.makedirs(my_copy_templates)
        for file in files:
            target_dir = os.path.join(my_copy_templates)
            if not os.path.isfile(target_dir):
                source_dir = os.path.join(root, file)
                shutil.copy2(os.path.join(source_dir), target_dir)
