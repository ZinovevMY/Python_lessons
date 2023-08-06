# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

factor_1 = [2, 3, 4, 5, 6, 7, 8, 9]
factor_2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
mult = [f"{i} * {j} = {i * j}" for i in factor_1 for j in factor_2]

step = len(mult)//len(factor_2) + 1
divider = len(mult)//len(factor_1)
last_elem = 0

for i in range(divider):
    for j in range(len(factor_1)//2):
        last_elem = i+j*step
        print(mult[last_elem], end='\t')
    print()
print("--------------------------------------")
# for i in range(divider):
#     for j in range(len(factor_1)//2):
#         print(mult[i+j*step], end='\t')
#     print()
# print("--------------------------------------")
