# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint


def input_number(num1: int, num2: int) -> int:
    return int(input(f"Введите число от {num1} до {num2}: "))


def guess_number(bottom: int, top: int, attempts: int):
    if bottom > top:
        bottom, top = top, bottom
    guess_num = randint(bottom, top)
    counter = 1
    print(f"Попробуйте угадать число от {bottom} до {top} за {attempts} попыток!")
    while counter <= attempts:
        user_num = input_number(bottom, top)
        if user_num < guess_num:
            print("Введенное число меньше загаданного!")
            counter += 1
        elif user_num > guess_num:
            print("Введенное число больше загаданного!")
            counter += 1
        else:
            print(f"Вы угадали число {guess_num} за {counter} попыток!")
            break
    else:
        print(f"Вы не угадали число {guess_num}!")
