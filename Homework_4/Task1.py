# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def matrix_transposition(matrix: list) -> tuple:
    return zip(*matrix)


my_matrix = [[1, 2, 3], [4, 5, 6]]
transp_matrix = matrix_transposition(my_matrix)
print(f"Исходная матрица: {my_matrix}")
print(f"Транспонированная матрицы: {list(transp_matrix)}")
