"""
Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).

Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?

Формат ввода
Вводится три целых числа.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
1
2
3
Вывод программы:
3
"""
#20.08.19
a, b, c = int(input()), int(input()), int(input())
res = [a, b, c]
print(sorted(res)[-1])