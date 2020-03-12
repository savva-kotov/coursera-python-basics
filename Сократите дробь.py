"""
Даны два натуральных числа n и m.
Сократите дробь (n / m), то есть выведите два других числа p и q таких, что (n / m) = (p / q) и дробь (p / q) — несократимая.
Решение оформите в виде функции ReduceFraction(n, m), получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).

Формат ввода
Вводятся два натуральных числа.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
12
16
Вывод программы:
3 4

Тест 2
Входные данные:
7
9
Вывод программы:
7 9

Тест 3
Входные данные:
10
100
Вывод программы:
1 10
"""
# 03.09.19
a, b = int(input()), int(input())


def evk(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


nod = evk(a, b)
print(int(a / nod), int(b / nod))