# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def duplicates_in_list(source_list: list) -> list:
    res_list = []
    for i in range(len(source_list)):
        if source_list.count(i) > 1 and i not in res_list:
            res_list.append(i)
    return res_list


my_list = [1, 2, 3, 1, 2, 4, 5, 3, 6, 5]
new_list = duplicates_in_list(my_list)
print(my_list)
print(new_list)