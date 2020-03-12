"""
Дана строка, в которой буква h встречается минимум два раза.Удалите из этой строки первое и последнее вхождение буквы h,а также все символы, находящиеся между ними.

Формат ввода
Вводится строка.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
In the hole in the ground there lived a hobbit
Вывод программы:
In tobbit

Тест 2
Входные данные:
qwertyhasdfghzxcvb
Вывод программы:
qwertyzxcvb

Тест 3
Входные данные:
asdfghhzxcvb
Вывод программы:
asdfgzxcvb
"""
# 27.08.19
s = input()
sub = 'h'
res = []
pos = s.find(sub)
while pos != -1:
    res.append(pos)
    pos = s.find(sub, pos + 1)
ans = s[:res[0]]+s[res[-1]+1:]
print(ans)