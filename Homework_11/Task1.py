# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyStr(str):
    """MyStr class implements from str. Added author of string and
       creation time in seconds.
    """
    def __new__(cls, string: str, author_name: str):
        instance = super().__new__(cls, string)
        instance.author_name = author_name
        instance.create_time = time.time()
        return instance


if __name__ == "__main__":
    new_str = MyStr('Мама мыла раму', 'Я')
    print(new_str)
    print(new_str.author_name, new_str.create_time)
    print(help(MyStr))