# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.
# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=None):
        self._length = length
        if width is None:
            self._width = self._length
        else:
            self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError("Ширина не может быть отрицательной!")

    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise ValueError("Длина не может быть отрицательной!")

    def perimeter(self):
        return (self.length + self.width) * 2

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
    rect1.length = 8
    print(rect1.square())
    # rect1.width = -3
    print(rect1.__slots__)
    print(Rectangle.__dict__)
