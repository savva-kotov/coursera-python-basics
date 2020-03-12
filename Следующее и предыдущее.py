"""
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (важно в точности соблюдать вывод программы: обратите внимание на пробелы и на точки). Нельзя пользоваться конкатенацией строк, используйте print с несколькими параметрами.

Формат ввода
Вводится целое число (гарантируется, что число находится в диапазоне от -1000 до +1000).

Формат вывода
Выведите две строки, согласно образцу.

Тест 1
Входные данные:
179

Вывод программы:
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
"""
a = input()
print('The next number for the number {} is {}.'.format(a, int(a)+1))
print('The previous number for the number {} is {}.'.format(a, int(a)-1))