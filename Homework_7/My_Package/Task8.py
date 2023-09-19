# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv
import os
from pathlib import Path


def get_file_extension(file_path: str):
    path = Path(file_path)
    return path.suffix


def file_renamer(wanted_name: str, nums_count: int, old_extension: str, new_extension: str, name_range: list):
    files = os.listdir(os.getcwd())
    counter = 0
    number = ""
    path = os.getcwd()
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            file_name, extension = os.path.splitext(file)
            if extension == old_extension:
                counter += 1
                if 0 < counter < 10:
                    number = ""
                    for _ in range(1, nums_count):
                        number = number + "0"
                    number = number + str(counter)
                elif 9 < counter < 100:
                    number = ""
                    for _ in range(1, nums_count - 1):
                        number = number + "0"
                new_file_name = file_name[name_range[0]:name_range[1]] + wanted_name + number
                new_file = new_file_name + new_extension
                os.rename(file, new_file)


if __name__ == "__main__":
    file_renamer("file", 3, ".txt", ".csv", [2, 5])
