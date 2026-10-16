# Даны два целых числа A и B (A < B).
# Вывести в порядке убывания все целые числа,
# расположенные между A и B (не включая числа A и B),
# а также количество N этих чисел.

a, b = input("Введите целое число A: "), input("Введите целое число B: ")

while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите целое число A: ")

while type(b) != int: # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите целое число B: ")

count = 0
for num in range(b - 1, a, -1):
    print(num, end=" ")
    count += 1
print("Количество чисел: ", count)