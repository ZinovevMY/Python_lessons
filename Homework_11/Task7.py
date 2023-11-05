# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    values = []

    def __init__(self, rows_num: int, col_num: int):
        self.rows_num = rows_num
        self.col_num = col_num

