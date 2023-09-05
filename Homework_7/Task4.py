# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from os import urandom
import random

__all__ = ['file_generator']
def file_generator(file_description, min_name_len=6, max_name_len=30, min_bytes_count=256,
                    max_bytes_count=4096, files_count=42):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for _ in range(files_count):
        name_length = random.randint(min_name_len, max_name_len)
        file_name = ""
        for _ in range(name_length):
            file_name += random.choice(letters)
        file_name += f'.{file_description}'
        bytes_count = random.randint(min_bytes_count, max_bytes_count)
        with open(file_name, 'wb') as file:
            random_bytes = urandom(bytes_count)
            file.write(random_bytes)


if __name__ == "__main__":
    file_generator('txt', 4, 7, 28, 128, 3)
