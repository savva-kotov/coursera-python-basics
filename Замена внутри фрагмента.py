"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

Формат ввода
Вводится строка.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
In the hole in the ground there lived a hobbit
Вывод программы:
In the Hole in tHe ground tHere lived a hobbit

Тест 2
Входные данные:
qwertyhahsdhfghzxcvb
Вывод программы:
qwertyhaHsdHfghzxcvb

Тест 3
Входные данные:
asdfghhzxcvb
Вывод программы:
asdfghhzxcvb
"""
# 30.08.19
s = input()
sub = 'h'
c = s.count('h')
s = s.replace('h', 'H', c)
s = s.replace('H', 'h', 1)
s = s[::-1].replace('H', 'h', 1)
print(s[::-1])