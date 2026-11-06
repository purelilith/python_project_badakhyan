# Составить функцию, которая напечатает сорок любых символов.

def print_forty(symbol):
    print(symbol * 40)

symbol = input("Введите один символ: ")

while len(symbol) != 1:
    print("Неправильно ввели!")
    symbol = input("Введите один символ: ")

print_forty(symbol)