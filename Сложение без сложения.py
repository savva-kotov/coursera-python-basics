"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

Формат ввода
Вводятся два удовлетворяющих условию задачи числа. Числа не превышают 900.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
2
2
Вывод программы:
4

Тест 2
Входные данные:
123
456
Вывод программы:
579

Тест 3
Входные данные:
179
0
Вывод программы:
179
"""
#02.09.19
def powerr(a, b):
    if b == 0:
        return a
    return powerr(a+1, b-1)


print(powerr(a, b))