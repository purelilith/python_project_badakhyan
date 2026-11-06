# Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
# информацию из строки в словарь, найти среднее арифметическое оценок,
# результаты вывести на экран.

text = input("Введите строку (фамилия имя группа оценки): ")
parts = text.split()

while (len(parts) < 4
       or not all(part.isdecimal() and 2 <= int(part) <= 5
                  for part in parts[3:])):
    print("Неправильно ввели!")
    text = input("Введите строку (фамилия имя группа оценки): ")
    parts = text.split()

grades = []
for grade in parts[3:]:
    grades.append(int(grade))

student = {
    "фамилия": parts[0],
    "имя": parts[1],
    "группа": parts[2],
    "оценки": grades,
}

average = sum(grades) / len(grades)

print(student)
print("Среднее арифметическое оценок:", round(average, 2))