# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

def mistery(mistery_text: str, clue: str, clues_list: list[str], attempts_num: int) -> int:
    counter = 0
    print(f'Отгадайте загадку "{mistery_text}" с {attempts_num} попыток!')
    while counter < attempts_num:
        for i in range(0, attempts_num):
            if clues_list[i].lower() == clue.lower():
                return counter + 1
            else:
                counter += 1
    else:
        return 0
