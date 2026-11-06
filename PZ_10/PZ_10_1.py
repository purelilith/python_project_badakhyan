# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно
# выполнив требуемую обработку элементов:
#
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Произведение элементов меньших 0 в первой половине:

from random import randint

n = input("Введите количество чисел: ")

while type(n) != int:
    try:
        n = int(n)
        if n < 1:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите количество чисел: ")

with open("numbers.txt", "w", encoding="utf-8") as file:
    for i in range(n):
        file.write(f"{randint(-50, 50)} ")

numbers = []
with open("numbers.txt", encoding="utf-8") as file:
    for item in file.read().split():
        numbers.append(int(item))

product = 1
found = False
for number in numbers[:n // 2]:
    if number < 0:
        product *= number
        found = True

with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Исходные данные: ")
    for number in numbers:
        file.write(f"{number} ")
    file.write("\n")
    file.write(f"Количество элементов: {len(numbers)}\n")
    file.write(f"Максимальный элемент: {max(numbers)}\n")
    if found:
        file.write(f"Произведение элементов меньших 0 в первой половине: "
                   f"{product}\n")
    else:
        file.write("Произведение элементов меньших 0 в первой половине: "
                   "таких элементов нет\n")