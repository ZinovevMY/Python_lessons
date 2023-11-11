# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
import random


class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        res = ''
        for row in self.data:
            res += " ".join(str(cell) for cell in row) + "\n"
        return res

    def __eq__(self, other):
        return self.cols == other.cols and self.rows == other.rows

    def __add__(self, other):
        if self == other:
            res = Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    res[r][c] = self.data[r][c] + other.data[r][c]
            return res

    def __mul__(self, other):
        if self == other:
            res = Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    res[r][c] = self.data[r][c] * other.data[r][c]
            return res


if __name__ == "__main__":
    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(2, 3)
    for r in range(matrix1.rows):
        for c in range(matrix1.cols):
            num = random.randint(-5, 10)
            matrix1.data[r].__setitem__(c, num)
            matrix2.data[r].__setitem__(c, num + 2)
    summatr = matrix1 + matrix2
    mulmatr = matrix1 * matrix2
    print(matrix1)
    print(matrix2)
    print(summatr)
    print(mulmatr)
