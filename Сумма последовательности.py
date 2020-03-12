"""
Определите сумму всех элементов последовательности, завершающейся числом 0.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, а служит как признак ее окончания).

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
1
7
9
0
Вывод программы:
17

Тест 2
Входные данные:
1
1
1
1
1
1
1
1
1
0
Вывод программы:
9

Тест 3
Входные данные:
34
2345
2345
2345
2345
345
3
345
3
345
1
3
424
5
453
0

Вывод программы:
11341
"""
#20.08.19
a = int(input())
res = 0
res += a
while a != 0:
    a = int(input())
    res += a
print(res)