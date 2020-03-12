"""
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, или же если он кратен 400.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
4

Вывод программы:
YES
"""
a = int(input())
if ((a % 4 == 0) and (a % 100 != 0)) or a % 400 == 0:
    print('YES')
else:
    print('NO')