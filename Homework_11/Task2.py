# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Archive class contains integer or float number and some string.
       The class also stores number and string values from previously created instances.
    """
    _instance = None
    nums = []
    strings = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            cls._instance.nums.append(cls._instance.number)
            cls._instance.strings.append(cls._instance.string)
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self, number: int | float, string: str):
        self.number = number
        self.string = string

    def __str__(self):
        return (f'Число в архиве = {self.number}, строка = {self.string}, значения ранее созданных экземпляров: '
                f'{self.nums} и {self.strings}.')

    def __repr__(self):
        return f'Archive({self.number}, {self.string})'


if __name__ == "__main__":
    arc1 = Archive(2, "23")
    arc2 = Archive(5, "15")
    arc3 = Archive(1, "11")
    print(help(Archive))
    print(arc1)
    print(repr(arc2))
