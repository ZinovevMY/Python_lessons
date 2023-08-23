# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

def mistery(mistery_text: str, clues_list: list[str], attempts_num: int) -> int:
    counter = 1
    print(f'Отгадайте загадку с {attempts_num} попыток!')
    print(mistery_text)
    while counter <= attempts_num:
        clue = input("Введите отгадку: ")
        for item in clues_list:
            if item.lower() == clue.lower():
                return counter
            else:
                counter += 1
    else:
        return 0
