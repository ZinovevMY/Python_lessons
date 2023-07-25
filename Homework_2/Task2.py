# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def dec_to_hex(number: int) -> str:
    hex_digits = "0123456789abcdef"
    hex_number = ""

    while number > 0:
        remainder = number % 16
        dec_hex_number = hex_digits[remainder]
        hex_number = dec_hex_number + hex_number
        number //= 16
    return "0x" + hex_number


number = int(input("Введите число: "))


print(f"Введенное число {number} в 16-ричной системе {dec_to_hex(number)}")
print(f"Проверка с помощью функции hex возвращает {hex(number)}")
