# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def kwargs_2_dict(**kwargs) -> dict:
    result = {}
    for k, v in kwargs.items():
        if v.__hash__ is None:
            result[str(v)] = k
        else:
            result[v] = k
    return result


print(kwargs_2_dict(res=1, reverse=[1, 2, 3]))
