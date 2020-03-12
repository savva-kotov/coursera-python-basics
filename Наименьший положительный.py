"""
Выведите значение наименьшего из всех положительных элементов в списке. Известно, что в списке есть хотя бы один положительный элемент, а значения всех элементов списка по модулю не превосходят 1000.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
5 -4 3 -2 1
Вывод программы:
1

Тест 2
Входные данные:
10 5 0 -5 -10
Вывод программы:
5

Тест 3
Входные данные:
-1 -2 -3 -4 100
Вывод программы:
100
"""
# 10.09.19
a = list(map(int, input().split()))
b = [i for i in a if i > 0]
print(min(b))