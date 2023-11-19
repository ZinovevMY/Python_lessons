# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json
from math import factorial


class Factorial:
    def __init__(self, count):
        self.storage = []
        self.count = count

    def __call__(self, value):
        self.result = factorial(value)
        if len(self.storage) == self.count:
            self.storage.pop(0)
        if len(self.storage) < self.count:
            self.storage.append({value: self.result})

    def __str__(self):
        return f'Последние {self.count} значений: {self.storage}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("task1.json", "w") as file:
            json.dump(self.storage, file)


if __name__ == '__main__':
    fact = Factorial(5)
    with fact as f:
        for i in range(4, 10):
            f(i)
    print(f)
