# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

MIN_VALUE = 1
MAX_VALUE = 999


def prompt():
    return int(input("Введите число от 1 до 999: "))


while True:
    number = prompt()
    if number < MIN_VALUE or number > MAX_VALUE:
        continue
    else:
        count = len(str(number))
        match count:
            case 1:
                print("Введена цифра, ее квадрат равен", number * number)
                break
            case 2:
                result = 1
                for n in str(number):
                    result *= int(n)
                print("Введено двузначное число, произведение цифр равно", result)
                break
            case 3:
                if number % 10 == 0:
                    result = str(int(number / 10))
                    print(result[::-1])
                else:
                    result = str(number)
                    print(result[::-1])
                break

