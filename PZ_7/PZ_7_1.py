# Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N.

n = input("Введите целое число N (32 < N < 126): ")

while type(n) != int:
    try:
        n = int(n)
        if not 32 < n < 126:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число N (32 < N < 126): ")

print(chr(n))