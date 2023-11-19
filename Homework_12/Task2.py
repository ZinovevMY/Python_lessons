# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.
from math import factorial


class Generator:
    def __init__(self, *args):
        if len(args) == 3:
            self.start, self.stop, self.step = args
        if len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        if len(args) == 1:
            self.start = 1
            self.step = 1
            self.stop = args[0]

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            self.result = factorial(self.start)
            self.start += self.step
            return self.result
        raise StopIteration


if __name__ == "__main__":
    fact_gen = Generator(4)
    for f in fact_gen:
        print(f)
