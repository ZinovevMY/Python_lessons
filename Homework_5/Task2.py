# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

user_str = "Some long-long string! :-)"
str_dict = {user_str[i]: ord(user_str[i]) for i in range(len(user_str))}
print(str_dict)