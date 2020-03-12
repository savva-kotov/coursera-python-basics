"""
Даны два списка, упорядоченных по возрастанию (каждый список состоит из различных элементов).
Найдите пересечение множеств элементов этих списков, то есть те числа, которые являются элементами обоих списков. Алгоритм должен иметь сложность O(len(A)+len(B)).
Решение оформите в виде функции Intersection(A, B). Функция должна возвращать список пересечения данных списков в порядке возрастания элементов. Модифицировать исходные списки запрещается.

Формат ввода
Программа получает на вход два возрастающих списка, каждый в отдельной строке.

Формат вывода
Программа должна вывести последовательность возрастающих чисел, являющихся элементами обоих списков.

Тест 1
Входные данные:
1 3 4 7 9
2 3 7 10 11
Вывод программы:
3 7 

Тест 2
Входные данные:
1 4 6 8
1 4 6 8
Вывод программы:
1 4 6 8 

Тест 3
Входные данные:
2 4 6 8 10
1 3 5 7 9
Вывод программы:
"""
# 19.09.19
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(*sorted(set(a) & set(b)))