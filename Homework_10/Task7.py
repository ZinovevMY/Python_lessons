# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from enum import Enum


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


class AnimalFactory:
    def __init__(self):
        self.animals = {
            'dog': Dog,
            'bird': Bird,
        }

    def create_animal(self, animal_type):
        if animal_type == 'dog':
            dog_name = input("Имя собаки: ")
            dog_weight = input("Вес собаки: ")
            dog_height = int(input("Высота в холке: "))
            dog_speed = int(input("Скорость собаки: "))
            dog_colour = input("Цвет собаки: ")
            dog_sound = input("Звук собаки: ")
            return self.animals[animal_type](dog_name, dog_weight, dog_height, dog_speed, dog_colour, dog_sound)
        elif animal_type == 'bird':
            bird_name = input("Имя птицы: ")
            bird_weight = input("Вес птицы: ")
            bird_wingspan = int(input("Размах крыльев: "))
            bird_speed = int(input("Скорость полета: "))
            bird_colour = input("Цвет птицы: ")
            bird_sound = input("Звук птицы: ")
            return self.animals[animal_type](bird_name, bird_weight, bird_wingspan, bird_speed, bird_colour, bird_sound)


if __name__ == '__main__':
    animal_factory = AnimalFactory()
    barbos = animal_factory.create_animal('dog')
    chizhik = animal_factory.create_animal('bird')
    print(barbos)
    print(chizhik)