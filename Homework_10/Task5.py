# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Bird:
    def __init__(self, name, weight, wing_span, fly_speed, colour, sound):
        self.name = name
        self.weight = weight
        self.wing_span = wing_span
        self.fly_speed = fly_speed
        self.colour = colour
        self.__sound = sound

    def make_sound(self):
        return f'{self.__sound}'

    def fly(self):
        return f'Птица {self.name} летит со скоростью {self.fly_speed} км/ч.'

    def __str__(self):
        return f'{self.name}, цвет: {self.colour}, размах крыла: {self.wing_span}, вес: {self.weight} килограмм.'


class Dog:
    def __init__(self, name, weight, height, speed, colour, sound):
        self.name = name
        self.weight = weight
        self.height = height
        self.speed = speed
        self.colour = colour
        self.__sound = sound

    def make_sound(self):
        return f'{self.__sound}'

    def __str__(self):
        return f'{self.name}, цвет: {self.colour}, высота в холке: {self.height} см., вес: {self.weight} килограмм.'