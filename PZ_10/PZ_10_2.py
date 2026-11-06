# Из предложенного текстового файла (text18-2.txt) вывести на экран его
# содержимое, количество знаков препинания. Сформировать новый файл, в
# который поместить текст в стихотворной форме выводя строки в обратном
# порядке.

punctuation = ".,!?;:-—–…'\"«»()"

try:
    with open("text18-2.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()
except FileNotFoundError:
    print("Файл text18-2.txt не найден!")
else:
    count = 0
    for line in lines:
        print(line)
        for char in line:
            if char in punctuation:
                count += 1
    print("Количество знаков препинания: ", count)

    with open("reversed.txt", "w", encoding="utf-8") as file:
        for line in reversed(lines):
            file.write(line + "\n")