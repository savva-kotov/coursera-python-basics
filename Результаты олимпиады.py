"""
В олимпиаде участвовало N человек. Каждый получил определенное количество баллов, при этом оказалось, что у всех участников разное число баллов. Упорядочите список участников олимпиады в порядке убывания набранных баллов.

Формат ввода
Программа получает на вход число участников олимпиады N. Далее идет N строк, в каждой строке записана фамилия участника, затем, через пробел, набранное им количество баллов.

Формат вывода
Выведите список участников (только фамилии) в порядке убывания набранных баллов.

Тест 1
Входные данные:
3
Ivanov 15
Petrov 10
Sidorov 20
Вывод программы:
Sidorov
Ivanov
Petrov

Тест 2
Входные данные:
3
Ivanov 15
Petrov 20
Sidorov 10
Вывод программы:
Petrov
Ivanov
Sidorov

Тест 3
Входные данные:
3
Ivanov 10
Petrov 15
Sidorov 20
Вывод программы:
Sidorov
Petrov
Ivanov
"""
# 19.09.19
a = int(input())
res = [input().split() for i in range(a)]

for i in sorted(res, key=lambda x: int(x[1]))[::-1]:
    print(i[0])