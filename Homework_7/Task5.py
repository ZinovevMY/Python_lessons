# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи

import Task4 as t

def generate_many_files(files_dict: dict):
    """
    Use files count as dict key and file description as value!
    """

    for count, descr in files_dict.items():
        t.file_generator(file_description=descr, files_count=count)


if __name__ == "__main__":
    file_dict = {2: 'txt', 1: 'dsc', 3: 'bin'}
    generate_many_files(file_dict)