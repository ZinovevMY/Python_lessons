# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def gcb(num1: int, num2: int) -> int:
    if num1 == 0:
        return num2
    return gcb(num2 % num1, num1)


def lcm(num1: int, num2: int) -> int:
    if num1 < num2:
        for i in range(2, num2 + 1):
            if (num1 * i) % num2 == 0:
                return num1 * i
    else:
        for i in range(2, num1 + 1):
            if (num2 * i) % num1 == 0:
                return num2 * i


def mult_fractions(fract1: list, fract2: list) -> str:
    numerators_mult = int(fract1[0]) * int(fract2[0])
    denominators_mult = int(fract1[1]) * int(fract2[1])
    divisor = gcb(numerators_mult, denominators_mult)
    if divisor != 0:
        numerators_mult = numerators_mult // divisor
        denominators_mult = denominators_mult // divisor
    return str(numerators_mult) + "/" + str(denominators_mult)


def summ_fractions(fract1: list, fract2: list) -> str:
    if int(fract1[1]) == int(fract2[1]):
        numerators_summ = int(fract1[0]) + int(fract2[0])
        denominators_summ = int(fract1[1])
    else:
        multiple = lcm(int(fract1[1]), int(fract2[1]))
        denominators_summ = multiple
        numerator1 = (multiple // int(fract1[1])) * int(fract1[0])
        numerator2 = (multiple // int(fract2[1])) * int(fract2[0])
        numerators_summ = numerator1 + numerator2

    divisor = gcb(numerators_summ, denominators_summ)
    if divisor != 0:
        numerators_summ = numerators_summ // divisor
        denominators_summ = denominators_summ // divisor

    return str(numerators_summ) + "/" + str(denominators_summ)


def check_with_fractions(fract1: list, fract2: list) -> None:
    fraction1 = Fraction(int(fract1[0]), int(fract1[1]))
    fraction2 = Fraction(int(fract2[0]), int(fract2[1]))
    print(f"Умножение с помощью Fraction вернуло {fraction1 * fraction2}")
    print(f"Сложение с помощью Fraction вернуло {fraction1 + fraction2}")


fraction1 = input("Введите первое дробное число: ")
fraction2 = input("Введите второе дробное число: ")

first_fraction = list(fraction1.split('/'))
second_fraction = list(fraction2.split('/'))

print(f"Результат умножения дробей равен {mult_fractions(first_fraction, second_fraction)}")
print(f"Результат сложения дробей равен {summ_fractions(first_fraction, second_fraction)}")
check_with_fractions(first_fraction, second_fraction)
