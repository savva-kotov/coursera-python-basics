"""
Напишите функцию phib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы - используйте рекурсию.

Формат ввода
Вводится удовлетворяющее условию задачи число.

Формат вывода
Выведите ответ на задачу.

Примечание
Обратите внимание на нумерацию чисел, показанную в примерах.

Тест 1
Входные данные:
1
Вывод программы:
1

Тест 2
Входные данные:
2
Вывод программы:
1

Тест 3
Входные данные:
3
Вывод программы:
2
"""
# 03.09.19
a = int(input())


def fib(a):
    f0, f1 = 0, 1
    for i in range(a-1):
        f0, f1 = f1, f0+f1
    return f1


print(fib(a))
