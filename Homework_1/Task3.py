# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


def printresult(number_1, number_2):
    print(number_1, "x", number_2, "=", number_1 * number_2, end='\t')


first_num = 2
second_num = 2
while second_num < 11:
    while first_num < 6:
        printresult(first_num, second_num)
        first_num += 1
    second_num += 1
