import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        make_time = os.path.getmtime(file_path)
        file_size = os.path.getsize(file_path)
        dir_name_file = os.path.dirname(file_path)

        print(f'Обнаружен файл ({file}) | путь к файлу ({file_path})')
        print(f'Дата создания ({time.ctime(make_time)}) --- '
              f'размер {file_size} --- '
              f'находится в директории {dir_name_file}')
        print()