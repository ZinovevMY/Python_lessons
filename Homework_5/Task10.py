# Создайте функцию генератор чисел Фибоначчи

def fib_generator(num: int):
    num1, num2 = 0, 1
    yield num1
    yield num2

    for _ in range(num - 2):
        num1, num2 = num2, num1 + num2
        yield num2


fib_number = int(input("Введите количество чисел последовавтельности Фибоначчи: "))
sequence = []
for num in fib_generator(fib_number):
    sequence.append(num)

print(sequence)
