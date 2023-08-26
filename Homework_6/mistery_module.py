# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

MISTERY_DICT = {"Висит груша, нельзя скушать.": ['мяч', 'лампочка', 'арбуз', 'паровоз'],
                "Зимой и летом одним цветом.": ['песок', 'небо', 'паровоз', 'елка', 'мяч', 'молоток']}
_results_dict = {}


def get_clue():
    return input("Введите отгадку: ")


def mistery(mistery_text: str, clue_list: list[str], attempts: int) -> int:
    counter = 0
    print(f"Отгадайте загадку '{mistery_text}' за {attempts} попыток!")
    while counter < attempts:
        clue = get_clue()
        if clue.lower() in clue_list:
            return counter + 1
        else:
            counter += 1
    return 0


def puzzle_game():
    for k, v in MISTERY_DICT.items():
        _results_dict[k] = mistery(k, v, 3)


def print_scores():

    for k, v in _results_dict.items():
        if v != 0:
            print(f"{k} отгадали с {v} попытки.")
        else:
            print(f"{k} не отгадали.")


if __name__ == "__main__":
    puzzle_game()
    print_scores()
