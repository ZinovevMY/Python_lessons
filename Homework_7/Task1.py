# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def fill_file(str_count: int, filename: str):
    with open(filename, 'a', encoding='utf-8') as file:
        for _ in range(1, str_count + 1):
            first_num = randint(-1000, 1000)
            second_num = uniform(-1000.0, 1000.0)
            file.write(f'{first_num} | {second_num: .2f}\n')


fill_file(15, "task1_text.txt")
