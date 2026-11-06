# Организовать и вывести последовательность A из n чисел (n - четное).
# Из последовательности A получить две последовательности B и C: в
# последовательности B - первая половина элементов A, в C - вторая
# половина элементов A. Найти произведение соответствующих элементов
# последовательностей B и C. Найти среднее арифметическое полученной
# последовательности.

n = input("Введите четное количество элементов n: ")

while type(n) != int:
    try:
        n = int(n)
        if n < 2 or n % 2 != 0:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите четное количество элементов n: ")

a = []
for i in range(n):
    value = input(f"Введите элемент {i + 1}: ")
    while type(value) != int:
        try:
            value = int(value)
        except ValueError:
            print("Неправильно ввели!")
            value = input(f"Введите элемент {i + 1}: ")
    a.append(value)

b = a[:n // 2]
c = a[n // 2:]

products = []
for i in range(n // 2):
    products.append(b[i] * c[i])

average = sum(products) / len(products)

print("Последовательность A:", a)
print("Последовательность B:", b)
print("Последовательность C:", c)
print("Произведения соответствующих элементов:", products)
print("Среднее арифметическое:", average)