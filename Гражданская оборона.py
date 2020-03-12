"""
Штаб гражданской обороны Тридесятой области решил обновить план спасения на случай ядерной атаки. Известно, что все n селений Тридесятой области находятся вдоль одной прямой дороги. Вдоль дороги также расположены m бомбоубежищ, в которых жители селений могут укрыться на случай ядерной атаки.
Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее, необходимо для каждого селения определить ближайшее к нему бомбоубежище.

Формат ввода
В первой строке вводится число n - количество селений (1 <= n <= 100000). Вторая строка содержит n различных целых чисел, i-е из этих чисел задает расстояние от начала дороги до i-го селения. В третьей строке входных данных задается число m - количество бомбоубежищ (1 <= m <= 100000). Четвертая строка содержит m различных целых чисел, i-е из этих чисел задает расстояние от начала дороги до i-го бомбоубежища. Все расстояния положительны и не превышают 10⁹. Селение и убежище могут располагаться в одной точке.

Формат вывода
Выведите n чисел - для каждого селения выведите номер ближайшего к нему бомбоубежища. Бомбоубежища пронумерованы от 1 до m в том порядке, в котором они заданы во входных данных.

Указание
Создайте список кортежей из пар (позиция селения, его номер в исходном списке), а также аналогичный список для бомбоубежищ. Отсортируйте эти списки.
Перебирайте селения в порядке возрастания.
Для селения ближайшими могут быть два соседних бомбоубежища, среди них надо выбрать ближайшее. При переходе к следующему селению не обязательно искать ближайшее бомбоубежище с самого начала. Его можно искать начиная с позиции, найденной для предыдущего города. Аналогично, не нужно искать подходящее бомбоубежище до конца списка бомбоубежищ: достаточно найти самое близкое. Если Вы неэффективно реализуете эту часть, то решение тесты не пройдет.
Для хранения ответа используйте список, где индекс будет номером селения, а по этому индексу будет запоминаться номер бомбоубежища.

Тест 1
Входные данные:
4
1 2 6 10
2
7 3
Вывод программы:
2 2 1 1 

Тест 2
Входные данные:
1
1
1
2
Вывод программы:
1 

Тест 3
Входные данные:
10
79 64 13 8 38 29 58 20 56 17
10
53 19 20 85 82 39 58 46 51 69
Вывод программы:
5 10 2 2 6 3 7 3 7 2
"""
# 17.09.19
a = int(input())
vil = [int(i) for i in input().split()]
b = int(input())
cov = [int(i) for i in input().split()]
res = []


def dist(vil, cov):
    res = [abs(i - vil) for i in cov]
    return res.index(min(res)) + 1


for i in vil:
    res.append(dist(i, cov))
print(*res)
# это не сработало, а жаль =(

# и это не сработало
a = int(input())
vil = [int(i) for i in input().split()]
b = int(input())
cov = [int(i) for i in input().split()]
res = []
maxx = [vil, cov]


def moveR(vil, cov):
    while vil > 0 and vil not in cov:
        vil -= 1
    return vil


def moveL(vil, cov, maxx):
    xam = max(max(maxx[0]), max(maxx[1]))
    while vil < xam and vil not in cov:
        vil += 1
    if vil == xam:
        vil = max(maxx[1])
    return vil


for i in vil:
    r = moveR(i, cov)
    L = moveL(i, cov, maxx)
    if r == 0 or L == 0:
        res.append(cov.index(r + L) + 1)
    elif r == L:
        res.append(cov.index(r) + 1)
    elif r > 0 and L > 0:
        if abs(i - L) < abs(i - r):
            res.append(cov.index(L) + 1)
        else:
            res.append(cov.index(r) + 1)
    else:
        print('lol')
print(*res)


# и еще вариант, тоже не сработал
import copy as c

a = int(input())
vil = [int(i) for i in input().split()]
b = int(input())
cov = [int(i) for i in input().split()]

res = []
back = c.deepcopy(cov)


def move(vil, cov):
    cov.append(vil)
    cov.sort()
    ans = 0
    if cov.index(vil) == 0:
        ans = cov[1]
    elif cov.index(vil) == len(cov) - 1:
        ans = cov[-2]
    elif abs(vil - (cov[cov.index(vil) - 1])) <\
            abs(vil - (cov[cov.index(vil) + 1])):
        ans = cov[cov.index(vil) - 1]
    else:
        ans = cov[cov.index(vil) + 1]
    cov.remove(vil)
    return ans


res = [back.index(move(i, cov)) + 1 for i in vil]
print(' '.join(map(str, res)))

# а вот так сработало, взял из инета
n = int(input())
a = map(int, input().split())
m = int(input())
b = list(map(int, input().split()))

for i in range(len(b)):
    b[i] = [i + 1, b[i]]
b.sort(key=lambda x: x[1])


def find_value(x):
    if(x < b[0][1]):
        return b[0][0]
    if(x > b[-1][1]):
        return b[-1][0]
    L = 0
    r = len(b) - 1
    while(r - L > 1):
        m = (r + L) >> 1
        if(b[m][1] < x):
            L = m
        else:
            r = m
    if(x - b[L][1] < b[r][1] - x):
        return b[L][0]
    else:
        return b[r][0]


print(*[find_value(v) for v in a])