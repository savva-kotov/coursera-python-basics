"""
Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.

В класс Matrix внесите следующие изменения:

    Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым аргументом __add__ (просто self), а matrix2 — вторым (второй операнд для сложения).

    Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса Matrix)

    Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу. Пример статического метода.

Формат ввода
Как в предыдущей задаче.

Формат вывода
Как в предыдущей задаче.

Тест 1
Входные данные:
# Task 3 check 1
# Check exception to add method
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
m2 = Matrix([[0, 1, 0], [20, 0, -1]])
try:
    m = m1 + m2
    print('WA\n' + str(m))
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)
Вывод программы:
1	1	0
20	1	-1
-1	-2	1
1	0	0
0	1	0
0	0	1
0	1	0
20	0	-1

Тест 2
Входные данные:
# Task 3 check 2
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
m1 = m.transpose()
print(m)
print(m1)
Вывод программы:
10	10
0	0
1	1
10	0	1
10	0	1
10	0	1
10	0	1

Тест 3
Входные данные:
# Task 3 check 3
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
print(Matrix.transposed(m))
print(m)
Вывод программы:
10	10
0	0
1	1
10	0	1
10	0	1
10	10
0	0
1	1
"""
# 08.10.19
from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, lists):
        self.lists = deepcopy(lists)

    def __str__(self):
        strRep = ""
        amount = 0
        for lists in self.lists:
            if amount != 0:
                strRep += "\n"
            new_str = "\t".join(str(elem) for elem in lists)
            strRep += new_str
            amount += 1
        return strRep

    def size(self):
        return len(self.lists), len(self.lists[0])

    def __add__(self, other):
        if len(self.lists) == len(other.lists):
            lenght = len(self.lists[0])
            for row in self.lists:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.lists:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.lists)):
                for j in range(len(self.lists[0])):
                    summa = other.lists[i][j] + self.lists[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.lists[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, alpha):
        if isinstance(alpha, int) or isinstance(alpha, float):
            result = []
            numbers = []
            for i in range(len(self.lists)):
                for j in range(len(self.lists[0])):
                    summa = self.lists[i][j] * alpha
                    numbers.append(summa)
                    if len(numbers) == len(self.lists[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    def transpose(self):
        t_matrix = list(zip(*self.lists))
        self.lists = t_matrix
        return Matrix(t_matrix)

    def transposed(self):
        t_matrix = list(zip(*self.lists))
        return Matrix(t_matrix)

    __rmul__ = __mul__


exec(stdin.read())
