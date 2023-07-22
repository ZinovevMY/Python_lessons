# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


number = int(input("Введите число: "))
hex_digits = "0123456789ABCDEF"
hex_number = ""

while number > 0:
    remainder = number % 16
    dec_hex_number = hex_digits[remainder]
    hex_number = dec_hex_number + hex_number
    number //= 16

print(hex_number)
