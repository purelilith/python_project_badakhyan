# Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
# расставлены правильно (то есть каждой открывающей соответствует одна
# закрывающая), то вывести число 0. В противном случае вывести или номер
# позиции, в которой расположена первая ошибочная закрывающая скобка,
# или, если закрывающих скобок не хватает, число -1.

text = input("Введите строку (латинские буквы и скобки): ")

while not all((ch.isascii() and ch.isalpha()) or ch in "()" for ch in text):
    print("Неправильно ввели!")
    text = input("Введите строку (латинские буквы и скобки): ")

balance = 0
result = 0
for position, char in enumerate(text, 1):
    if char == "(":
        balance += 1
    elif char == ")":
        if balance == 0:
            result = position
            break
        balance -= 1
else:
    if balance > 0:
        result = -1

print(result)