# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
from collections import defaultdict
from math import factorial


class Factorial:
    def __init__(self, count):
        self.storage = defaultdict(list)
        self.count = count

    def __call__(self, value):
        self.result = factorial(value)
        if len(self.storage) < self.count:
            self.storage[value].append(self.result)

    def __str__(self):
        return f'Последние {self.count} значений: {self.storage}'


if __name__ == '__main__':
    f = Factorial(6)
    for i in range(4, 10):
        f(i)
    print(f)
