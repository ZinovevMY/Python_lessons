# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

def guess_number(number: int, attempts: int):

    def game():
        for _ in range(attempts):
            num = int(input("Введите число: "))
            if num == number:
                return True
        return False
    return game


if __name__ == "__main__":
    proc = guess_number(25, 5)
    print(proc())
