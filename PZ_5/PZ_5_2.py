# Описать функцию Mean(параметры), вычисляющую среднее арифметическое
# AMean = (X+Y)/2 и среднее геометрическое GMean = √(X*Y) двух
# положительных чисел X и Y. С помощью этой функции найти среднее
# арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D),
# если даны A, B, C, D.

from math import sqrt


def mean(x, y):
    amean = (x + y) / 2
    gmean = sqrt(x * y)
    return amean, gmean


a = input("Введите положительное число A: ")
b = input("Введите положительное число B: ")
c = input("Введите положительное число C: ")
d = input("Введите положительное число D: ")

while type(a) != float:
    try:
        a = float(a)
        if not a > 0:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите положительное число A: ")

while type(b) != float:
    try:
        b = float(b)
        if not b > 0:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите положительное число B: ")

while type(c) != float:
    try:
        c = float(c)
        if not c > 0:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите положительное число C: ")

while type(d) != float:
    try:
        d = float(d)
        if not d > 0:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        d = input("Введите положительное число D: ")

for name, value in (("B", b), ("C", c), ("D", d)):
    amean, gmean = mean(a, value)
    print(f"Пара (A, {name}): среднее арифметическое = {amean}, "
          f"среднее геометрическое = {gmean}")