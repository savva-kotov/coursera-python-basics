"""
Дано число N. С начала суток прошло N минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент.

Формат ввода
Вводится число N — целое, положительное, не превышает 10⁷.

Формат вывода
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).

Учтите, что число N может быть больше, чем количество минут в сутках.

Тест 1
Входные данные:
150

Вывод программы:
2 30
"""
t = int(input())
h = t // 60
print(h % 24, t % 60)
'''
Тут заковырка в том что нужно узнать не количество часов в t, а сколько будут показывать
циферблат если пройдет h часов. Например если пройдет 30 часов, то на часах будет
6 (1 круг циферблата + 6 часов). Поэтому необходимо разделить h по основанию 24
(количество часов в сутках) и взять остаток, это и будет час на циферблате. И добавить минуты.
'''