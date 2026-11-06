# Из текстового файла (writer.txt) выбрать фамилии писателей и годы
# жизни, а также произведения ими написанные. Посчитать общее количество
# произведений в данном файле.

try:
    with open("writer.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()
except FileNotFoundError:
    print("Файл writer.txt не найден!")
else:
    total = 0
    for line in lines:
        if ":" not in line:
            continue
        author, works_text = line.split(":", 1)
        works = []
        for work in works_text.split(","):
            if work.strip() != "":
                works.append(work.strip())
        print("Писатель и годы жизни:", author.strip())
        print("Произведения:", ", ".join(works))
        total += len(works)
    print("Общее количество произведений:", total)