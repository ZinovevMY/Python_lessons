# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

line_count = int(input("Введите количество рядов: "))
delemiter = " "
counter = 1
for n in range(line_count):
    print(delemiter*(line_count - n) + "*"*counter)
    counter += 2
