# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi ** 2 * self.radius


new_circle = Circle(12)
print(f'{new_circle.length(): .2f}')
print(f'{new_circle.square(): .2f}')