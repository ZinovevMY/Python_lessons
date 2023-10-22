# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from Task3 import Human


def calc_level(id):
    tmp = str(id)
    res = 0
    for i in range(len(tmp)):
        res += int(tmp[i])
    return res % 7


class Employee(Human):
    def __init__(self, first_name, middle_name, last_name, age, gender, employee_id):
        super().__init__(first_name, middle_name, last_name, age, gender)
        self.employee_id = employee_id
        self.level = calc_level(self.employee_id)

    def employee_info(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} id: {self.employee_id} level: {self.level}'


if __name__ == "__main__":
    new_employee = Employee('Mikhail', 'Yurevich', 'Zinovev', 41,
                            'male', 987654)
    print(new_employee.employee_info())
