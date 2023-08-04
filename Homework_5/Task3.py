# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

user_str = "Some long-long string! :-)"
str_dict = {user_str[i]: ord(user_str[i]) for i in range(len(user_str))}
dict_iter = iter(str_dict.items())
for i in range(0, 5):
    print(next(dict_iter))
