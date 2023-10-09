# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.
import random


def validate(func):
    def wrapper(number: int, attempts: int):
        if not 1 <= number <= 100:
            number = random.randint(1, 100)
        if not 1 <= attempts <= 10:
            attempts = random.randint(1, 10)
        return func(number, attempts)
    return wrapper


@validate
def game(number: int, attempts: int):
    for _ in range(attempts):
        num = int(input("Введите число: "))
        if num == number:
            return True
    return False


if __name__ == "__main__":
    print(game(140, 35))
