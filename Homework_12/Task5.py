# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.
import csv


class ValidValue:
    def __set_name__(self, owner, name):
        self.param_name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value[0].isupper() and not value.isdigit():
            setattr(instance, self.param_name, value)
        else:
            raise ValueError("Неверный формат имени!")

    # def validate(self, name: str):
    #     if len(name) == 0:
    #         raise ValueError("Имя не может быть пустой строкой!")
    #     if not name[0].isupper():
    #         raise ValueError("Имя должно начинаться с заглавной буквы!")
    #     if name[0].isdigit():
    #         raise ValueError("Имя не может начинаться с цифры!")
    #     if name.isdigit():
    #         raise ValueError("Имя не может содержать только цифры!")


class Student:
    full_name = ValidValue()

    def __init__(self, full_name: str, file_name: str):
        self.full_name = full_name
        self.lessons = {}
        self.tests = {}
        with open(file_name, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                self.lessons.update({row[0]: 0})
                self.tests.update({row[0]: 0})

    def check_lesson(self, lesson: str, lessons: dict):
        if lesson not in lessons.keys():
            raise ValueError("Такой предмет студент не изучает!")

    def set_test_result(self, lesson: str, result: int):
        self.check_lesson(lesson, self.tests)
        if result not in range(0, 101):
            raise ValueError("Результат теста должен быть от 0 до 100 баллов")
        self.tests[lesson] = result

    def set_lesson_grade(self, lesson: str, grade: int):
        self.check_lesson(lesson, self.lessons)
        if grade not in range(2, 6):
            raise ValueError("Оценка по предмету должны быть от 2 до 5")
        self.lessons[lesson] = grade

    def gpa(self, lessons: dict):
        result = 0
        for v in lessons.values():
            result += v
        return result / len(lessons)

    def __str__(self):
        return (f"Студент {self.full_name} имеет оценки: {self.lessons}. Результаты тестов: {self.tests}."
                f"Средний балл по предметам: {self.gpa(self.lessons)}."
                f"Средний балл по тестам: {self.gpa(self.tests)}.")


if __name__ == '__main__':
    ivanov = Student("Иванов", "ivanov.csv")
    # petrov = Student("Петров Петр Петрови4", "petrov.csv")
