# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import random
from pathlib import Path
import Task1 as t1
import Task2 as t2
import Task3 as t3


def generate_file_name(length: int)-> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name = ""
    for _ in range(length):
        name += random.choice(letters)
    name += ".txt"
    return name


def files_in_folder(dir_name: str):
    full_path = Path(dir_name)
    if not full_path.exists():
        Path.mkdir(full_path)

    file1 = dir_name + generate_file_name(8)
    file2 = dir_name + generate_file_name(8)
    file3 = dir_name + generate_file_name(8)
    t1.fill_file(10, file1)
    t2.pseudonyms(file2)
    t3.file_comparator(file1, file2, file3)


if __name__ == "__main__":
    files_in_folder("C:\\Разное\\Python_lessons\\Info\\")

