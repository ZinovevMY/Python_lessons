# Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.
import json
import os
import pickle
from pathlib import Path


def get_file_extension(file_path: str):
    path = Path(file_path)
    return path.suffix


def get_file_name(file_path: str):
    full_name = os.path.basename(file_path)
    return os.path.splitext(full_name)[0]


def json_to_pickle(folder_name: str):
    files = os.listdir(folder_name)
    for file in files:
        if os.path.isfile(os.path.join(folder_name, file)):
            extension = get_file_extension(file)
            if extension == '.json':
                pickle_name = get_file_name(file) + ".pickle"
                with open(file, encoding='utf-8') as read_file:
                    file_data = json.load(read_file)
                with open(pickle_name, 'wb') as write_file:
                    pickle.dump(file_data, write_file)


if __name__ == "__main__":
    json_to_pickle("C:\\Разное\\Python_lessons\\Homework_8")