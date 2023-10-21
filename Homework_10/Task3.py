# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Human:
    def __init__(self, first_name, middle_name, last_name, age, gender):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.__age = age
        self.gender = gender

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}, возраст: {self.get_age()}, пол: {self.gender}'

    def get_age(self):
        return self.__age


Misha = Human('Михаил', 'Юрьевич', 'Зиновьев', 41, 'мужской')
print(Misha.full_name())
Misha.birthday()
print(Misha.full_name())
