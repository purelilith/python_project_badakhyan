# Дан список размера N. Найти номера тех элементов списка, которые больше
# своего левого соседа, и количество таких элементов. Найденные номера
# выводить в порядке их убывания.

n = input("Введите размер списка N: ")

while type(n) != int:
    try:
        n = int(n)
        if n < 1:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер списка N: ")

numbers = []
for i in range(n):
    value = input(f"Введите элемент {i + 1}: ")
    while type(value) != int:
        try:
            value = int(value)
        except ValueError:
            print("Неправильно ввели!")
            value = input(f"Введите элемент {i + 1}: ")
    numbers.append(value)

count = 0
for i in range(n - 1, 0, -1):
    if numbers[i] > numbers[i - 1]:
        print(i + 1, end=" ")
        count += 1
print("Количество элементов: ", count)