# 1. В матрице найти минимальный и максимальные элементы.
# 2. В матрице найти сумму отрицательных элементов в первой трети матрицы.

rows = input("Введите количество строк: ")

while type(rows) != int:
    try:
        rows = int(rows)
        if rows < 1:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        rows = input("Введите количество строк: ")

cols = input("Введите количество столбцов: ")

while type(cols) != int:
    try:
        cols = int(cols)
        if cols < 1:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        cols = input("Введите количество столбцов: ")

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = input(f"Введите элемент [{i + 1}][{j + 1}]: ")
        while type(value) != int:
            try:
                value = int(value)
            except ValueError:
                print("Неправильно ввели!")
                value = input(f"Введите элемент [{i + 1}][{j + 1}]: ")
        row.append(value)
    matrix.append(row)

smallest = matrix[0][0]
largest = matrix[0][0]
for row in matrix:
    for value in row:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

limit = rows * cols // 3
passed = 0
total = 0
for row in matrix:
    for value in row:
        if passed < limit and value < 0:
            total += value
        passed += 1

for row in matrix:
    print(*row)
print("Минимальный элемент:", smallest)
print("Максимальный элемент:", largest)
print("Сумма отрицательных элементов в первой трети:", total)