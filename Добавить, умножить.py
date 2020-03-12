"""
Добавьте в предыдущий класс следующие методы:
    __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.

    __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.

    __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа. Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.

Иллюстрация:

    В следующем случае вызовется __mul__: Matrix([[0, 1], [1, 0]) * 10.
    В следующем случае вызовется __rmul__ (так как у int не определен __mul__ для матрицы справа): 10 * Matrix([[0, 1], [1, 0]).

Разумеется, данные методы не должны менять содержимое матрицы.

Формат ввода
Как в предыдущей задаче.

Формат вывода
Как в предыдущей задаче.

Тест 1
Входные данные:
# Task 2 check 1
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m.size())
Вывод программы:
(3, 2)

Тест 2
Входные данные:
# Task 2 check 2
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
Вывод программы:
1	1	0
20	1	-1
-1	-2	1

Тест 3
Входные данные:
# Task 2 check 3
m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)
Вывод программы:
15	15	0
0	30	150
150	225	450
15	15	0
0	30	150
150	225	450
"""
# 08.10.19
from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def __add__(self, other):
        return Matrix()

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        return Matrix(list(map(
                        lambda x, y: list(map(lambda z, w: z + w, x, y)),
                        self.matrix, other.matrix)))

    def __mul__(self, other):
        return Matrix([[i * other for i in list] for list in self.matrix])

    __rmul__ = __mul__


exec(stdin.read())
