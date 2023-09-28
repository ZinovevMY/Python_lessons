# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.
import os


def folder_traversal(path: str, depth=0):
    content_dict: dict = {}
    dict_data = []
    for file in os.scandir(path):
        if file.is_file():
            dict_data.append(os.path.dirname(file.path))
            dict_data.append("File")
            dict_data.append(os.path.getsize(file.path))
            content_dict[file.name] = dict_data
            dict_data = []
        elif file.is_dir():
            total_size = 0
            for f in os.listdir(file.path):
                if os.path.isfile(f):
                    total_size += os.path.getsize(f)
            dict_data.append(os.path.dirname(file))
            dict_data.append("Folder")
            dict_data.append(total_size)
            content_dict[file.name] = dict_data
            dict_data = []
            folder_traversal(file.path, depth + 1)
    print(content_dict)



folder_traversal("C:\\Разное\\Python_lessons\\Homework_8")
