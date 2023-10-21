# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = self.length
        else:
            self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def square(self):
        return self.length * self.width


rect = Rectangle(5, 12)
print(rect.perimeter())
print(rect.square())
