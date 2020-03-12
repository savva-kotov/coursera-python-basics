"""
Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂. Определите, можно ли разместить одну из этих коробок внутри другой, при условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.

Формат ввода
Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.

Формат вывода
Программа должна вывести одну из следующих строчек:

Boxes are equal, если коробки одинаковые,
The first box is smaller than the second one, если первая коробка может быть положена во вторую,
The first box is larger than the second one, если вторая коробка может быть положена в первую,
Boxes are incomparable, во всех остальных случаях.

Тест 1
Входные данные:
1
2
3
3
2
1
Вывод программы:
Boxes are equal

Тест 2
Входные данные:
2
2
3
3
2
1
Вывод программы:
The first box is larger than the second one
"""
#20.08.19
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if sorted([a1, b1, c1]) == sorted([a2, b2, c2]):
    print('Boxes are equal')
elif (a1 >= a2 and b1 >= b2 and c1 >= c2) or \
     (a1 >= a2 and b1 >= c2 and c1 >= b2) or \
     (a1 >= b2 and b1 >= a2 and c1 >= c2) or \
     (a1 >= b2 and b1 >= c2 and c1 >= a2) or \
     (a1 >= c2 and b1 >= a2 and c1 >= b2) or \
     (a1 >= c2 and b1 >= b2 and c1 >= a2):
    print('The first box is larger than the second one')
elif (a1 <= a2 and b1 <= b2 and c1 <= c2) or \
     (a1 <= a2 and b1 <= c2 and c1 <= b2) or \
     (a1 <= b2 and b1 <= a2 and c1 <= c2) or \
     (a1 <= b2 and b1 <= c2 and c1 <= a2) or \
     (a1 <= c2 and b1 <= a2 and c1 <= b2) or \
     (a1 <= c2 and b1 <= b2 and c1 <= a2):
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')