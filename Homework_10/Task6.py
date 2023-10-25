# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, weight, colour, sound):
        self.name = name
        self.weight = weight
        self.colour = colour
        self.__sound = sound

    def make_sound(self):
        return f'{self.__sound}'


class Dog(Animal):
    def __init__(self, name, weight, height, speed, colour, sound):
        super().__init__(name, weight, colour, sound)
        self.height = height
        self.speed = speed

    def make_sound(self):
        super().make_sound()

    def __str__(self):
        return f'{self.name}, цвет: {self.colour}, высота в холке: {self.height} см., вес: {self.weight} килограмм.'


class Bird(Animal):
    def __init__(self, name, weight, wing_span, fly_speed, colour, sound):
        super().__init__(name, weight, colour, sound)
        self.wing_span = wing_span
        self.fly_speed = fly_speed

    def make_sound(self):
        super().make_sound()

    def __str__(self):
        return f'{self.name}, цвет: {self.colour}, размах крыла: {self.wing_span}, вес: {self.weight} килограмм.'
