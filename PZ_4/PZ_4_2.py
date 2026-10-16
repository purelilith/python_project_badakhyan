# Дано целое число N (N > 0).
# С помощью операций деления нацело
# и взятия остатка от деления определить,
# имеются ли в записи числа N нечетные цифры.
# Если имеются, то вывести TRUE, если нет — вывести FALSE.

N = input("Введите целое число: ")

while type(N) != int:
    try:
        N = int(N)
        if N <= 0:
            print("Число должно быть больше 0!")
            N = input("Введите целое число: ")
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите целое число: ")

has_odd = False

while N > 0:
    digit = N % 10
    if digit % 2 != 0:
        has_odd = True
        break
    N = N // 10

if has_odd:
    print("TRUE")
else:
    print("FALSE")