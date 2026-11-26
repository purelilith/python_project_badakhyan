import random

# Дан список размера N. Обнулить элементы списка, расположенные между его
# минимальным и максимальным элементами (не включая минимальный и
# максимальный элементы).

n = input("Введите размер списка N: ")

while type(n) != int:
    try:
        n = int(n)
        if n < 1:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер списка N: ")

# диапазон от -50 до 50
numbers = []
for i in range(n):
    numbers.append(random.randint(-50, 50))
print("Исходный список:", numbers)

index_min = numbers.index(min(numbers))
index_max = numbers.index(max(numbers))

for i in range(min(index_min, index_max) + 1, max(index_min, index_max)):
    numbers[i] = 0

print("Изменённый список:", numbers)