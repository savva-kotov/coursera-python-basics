"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите их значение и индекс первого из них.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
1 2 3 2 1
Вывод программы:
3 2

Тест 2
Входные данные:
1 2 3
Вывод программы:
3 2

Тест 3
Входные данные:
1 3 2
Вывод программы:
3 1
"""
# 11.09.19
a = list(map(int, input().split()))
print(max(a), a.index(max(a)))