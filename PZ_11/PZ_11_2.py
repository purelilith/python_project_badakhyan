# Составить список, в который будут включены только согласные буквы и
# привести их к верхнему регистру.
# Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир'].

cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
consonants = "бвгджзйклмнпрстфхцчшщ"

result = []
for city in cities:
    letters = ""
    for char in city:
        if char.lower() in consonants:
            letters += char.upper()
    result.append(letters)

print(result)