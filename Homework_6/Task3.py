# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

import argparse
from Homework_6.allmodules import somemodule as sm

parser = argparse.ArgumentParser(description="Получаем параметры функции")
parser.add_argument('bottom', type=int, help="Нижний диапазон генератора")
parser.add_argument('top', type=int, help="Верхний диапазон генератора")
parser.add_argument('attempts', type=int, help="Количество попыток")
args = parser.parse_args()

is_guessed = sm.guess_number(args.bottom, args.top, args.attempts)
if is_guessed:
    print("Угадал")
else:
    print("Не угадал")
