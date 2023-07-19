# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


def mult_table(start_number: int, finish_number: int):
    for n in range(2, 11):
        for m in range(start_number, finish_number + 1):
            print(m, "x", n, "=", m * n, end='\t')
        print(" ")


mult_table(2, 5)
print('\n')
mult_table(6, 9)