"""
Для данного числа n<100 закончите фразу “На лугу пасется...” одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

Формат ввода
Вводится натуральное число.

Формат вывода
Программа должна вывести введенное число n и одно из слов: korov, korova или korovy. Между числом и словом должен стоять ровно один пробел.

Тест 1
Входные данные:
1
Вывод программы:
1 korova

Тест 2
Входные данные:
2
Вывод программы:
2 korovy

Тест 3
Входные данные:
3
Вывод программы:
3 korovy
"""
#20.08.19
a = int(input())
res = ''
if a >= 0:
    if a == 0:
        res += str(a) + ' korov'
    elif a % 100 >= 10 and a % 100 <= 20:
        res += str(a) + ' korov'
    elif a % 10 == 1:
        res += str(a) + ' korova'
    elif a % 10 >= 2 and a % 10 <= 4:
        res += str(a) + ' korovy'
    else:
        res += str(a) + ' korov'
print(res)