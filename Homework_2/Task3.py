# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


def gcb(num1: int, num2: int) -> int:
    if num1 == 0:
        return num2
    return gcb(num2 % num1, num1)


def mult_fractions(fract1: list, fract2: list) -> str:
    numerators_mult = int(fract1[0]) * int(fract2[0])
    denominators_mult = int(fract1[1]) * int(fract2[1])
    divisor = gcb(numerators_mult, denominators_mult)
    if divisor != 0:
        numerators_mult = numerators_mult // divisor
        denominators_mult = denominators_mult // divisor
    return str(numerators_mult) + "/" + str(denominators_mult)


fraction1 = input("Введите первое дробное число: ")
fraction2 = input("Введите второе дробное число: ")

first_fraction = list(fraction1.split('/'))
second_fraction = list(fraction2.split('/'))

print(mult_fractions(first_fraction, second_fraction))