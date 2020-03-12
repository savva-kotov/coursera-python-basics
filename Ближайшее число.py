"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.

Формат ввода
В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива. Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000). В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.

Формат вывода
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.

Тест 1
Входные данные:
5
1 2 3 4 5
6
Вывод программы:
5

Тест 2
Входные данные:
5
5 4 3 2 1
3
Вывод программы:
3
"""
# 10.09.19
ll = int(input())
a = list(map(int, input().split()))
n = int(input())

ll += 1
b = [abs(i - n) for i in a]
print(a[b.index(min(b))])