"""
Найдите количество положительных элементов в данном списке.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
1 -2 3 -4 5
Вывод программы:
3

Тест 2
Входные данные:
1 2 3 -1 -4
Вывод программы:
3

Тест 3
Входные данные:
9 3 4 1 2
Вывод программы:
5
"""
# 10.09.19
a = input().split()
res = [i for i in a if int(i) > 0]
print(len(res))