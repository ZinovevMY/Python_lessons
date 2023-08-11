# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def string_splitter(string: str) -> tuple:
    tmp = string.split('\\')
    file_path = ""
    file_name = ""
    file_extension = ""
    for i in range(len(tmp) - 1):
        file_path += tmp[i]
        file_path += "\\"
    tmp = tmp[len(tmp) - 1].split(".")
    file_name = tmp[0]
    file_extension = tmp[1]
    return file_path, file_name, file_extension


string_path = "C:\Разное\Python_lessons\main.py"
result = string_splitter(string_path)
print(result)
