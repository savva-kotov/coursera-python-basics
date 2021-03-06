"""
Дано натуральное число n>1. Проверьте, является ли оно простым. Программа должна вывести слово YES, если число простое и NO, если число составное. Решение оформите в виде функции IsPrime(n), которая возвращает True для простых чисел и False для составных чисел. Программа должна иметь сложность O(корень из n): количество действий в программе должно быть пропорционально квадратному корню из n (иначе говоря, при увеличении входного числа в k раз, время выполнения программы должно увеличиваться примерно в корень из k раз).

Формат ввода
Вводится натуральное число.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
2
Вывод программы:
YES

Тест 2
Входные данные:
4
Вывод программы:
NO

Тест 3
Входные данные:
3
Вывод программы:
YES
"""
# 02.09.19
import math as m
a = int(input())
n = 2
while a % n != 0:
    if n > m.sqrt(a):
        n = a
        break
    else:
        n += 1

if a == n:
    print('YES')
else:
    print('NO')
