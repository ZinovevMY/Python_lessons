# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

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

    def __add__(self, other):
        return Rectangle(self.length, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(self.length, abs(self.width - other.width))


if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(6, 7)
    rect3 = rect1 + rect2
    rect4 = rect1 - rect2
    print(rect3.length, rect3.width)
    print(rect4.length, rect4.width)