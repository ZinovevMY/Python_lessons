# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def json_creator(file_path: str):
    with open(file_path, encoding="utf-8") as file:
        temp_dict = {}
        all_vals = file.read().split('\n')
        for line in all_vals:
            line = line.strip()
            if line:
                line = line.replace("  ", " ")
                values = [val for val in line.split(" ")]
                temp_dict[values[0].capitalize()] = float(values[1])
    with open("task1.json", "w") as json_file:
        json.dump(temp_dict, json_file)


if __name__ == "__main__":
    json_creator("C:\\Разное\\Python_lessons\\Homework_7\\task3_text.txt")
