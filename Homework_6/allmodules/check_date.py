# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['check_date']


def _is_leap_year(year: int) -> bool:

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def check_date(incoming_date: str) -> bool:
    day, month, year = map(int, incoming_date.split("."))
    if 1 <= year <= 9999:
        if 1 <= month <= 12:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if 1 <= day <= 31:
                    return True
            elif month in [4, 6, 9, 11]:
                if 1 <= day <= 30:
                    return True
            elif month == 2:
                if _is_leap_year(year):
                    if 1 <= day <= 29:
                        return True
    return False


if __name__ == "__main__":
    print(check_date("26.05.2021"))
