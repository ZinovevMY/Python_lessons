# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_VALUE = 1
MAX_VALUE = 100000


def prompt():
    return int(input("Введите число : "))


while True:
    number = prompt()
    if number < MIN_VALUE or number > MAX_VALUE:
        continue
    else:
        counter = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                counter += 1
        if counter == 0:
            print("Число", number, "простое.")
            break
        else:
            print("Число", number, "составное.")
            break
