# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Validsize:

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("Значение должно быть целым числом!")
        if value <= 0:
            raise ValueError("Значение должно быть положительным!")


class Rectangle:
    length = Validsize()
    width = Validsize()

    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = self.length
        else:
            self.width = width

    def perimeter(self):
        return (self.__getattribute__() + self.width) * 2

    def square(self):
        return self.length * self.width

    def __add__(self, other):
        return Rectangle(self.length, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(self.length, abs(self.width - other.width))

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __ge__(self, other):
        return self.square() <= other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() >= other.square()


if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(6, 7)
    print(rect1.width)
    print(rect1.square())
    print(rect1.__dict__)
