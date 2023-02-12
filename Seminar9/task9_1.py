"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

import copy

class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        s = ''
        for i in range(len(self.array)):
            s = s + ' '.join(map(str, self.array[i])) + '\n'  # вывод матрицы
        return s

    def __add__(self, other):
        if len(self.array) != len(other.array):
            return 'Нельзя складывать матрицы разной размерности!'
        result = copy.deepcopy(self.array)  # копия первой матрицы
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                result[i][j] = self.array[i][j] + \
                    other.array[i][j]  # сумма элементов матриц
        return Matrix(result)


array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_array1 = Matrix(array1)
m_array2 = Matrix(array2)
print('Исходные матрицы')
print(m_array1)
print(m_array2)
sum_array = m_array1 + m_array2
print('сумма матриц')
print(sum_array)
