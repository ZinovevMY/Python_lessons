# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
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


if __name__ == "__main__":
    arc1 = Archive(2, "23")
    arc2 = Archive(5, "15")
    print(arc1.nums)
    print(arc1.strings)
    print(arc2.nums)
    print(arc2.strings)
