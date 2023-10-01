# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.
import csv
import json
import os
import pickle


def folder_traversal(path: str, content_dict: dict):
    for file in os.scandir(path):
        if file.is_file():
            content_dict[file.name] = {
                "path": os.path.dirname(file.path),
                "type": "File",
                "size": os.path.getsize(file.path)
            }
        elif file.is_dir():
            total_size = 0
            for f in os.listdir(file.path):
                if os.path.isfile(os.path.join(file.path, f)):
                    total_size += os.path.getsize(os.path.join(file.path, f))
            content_dict[file.name] = {
                "path": os.path.dirname(file.path),
                "type": "Folder",
                "size": total_size
            }
            folder_traversal(file.path, content_dict[file.name])
    return content_dict


if __name__ == "__main__":
    my_dict: dict = {}
    path = "C:\\Разное\\Python_lessons\\Homework_8"
    folder_traversal(path, my_dict)
    with (
        open(path + "\\task8.json", "w", encoding="utf-8") as json_file,
        open(path + "\\task8.csv", "w", encoding="utf-8", newline='') as csv_file,
        open(path + "\\task8.pickle", "wb") as pickle_file
    ):
        json.dump(my_dict, json_file, ensure_ascii=False)
        writer = csv.DictWriter(csv_file, fieldnames=[name for name in my_dict.keys()])
        writer.writeheader()
        writer.writerow(my_dict)
        pickle.dump(my_dict, pickle_file)
