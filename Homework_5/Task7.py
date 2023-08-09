# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(num):
    counter = 0
    number = 2
    while counter < num:
        if is_prime(number):
            yield number
            counter += 1
        number += 1


nums = int(input("Введите количество простых чисел: "))

print(*prime_generator(nums))
