# Х шоколадных конфет стоят А рублей
# Y ирисок стоит В рублей
# Определить сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок

while True:
    try:
        X = float(input("Введите вес шоколадных конфет (кг): "))
        if X <= 0:
            print("Ошибка: Вес должен быть больше 0.")
            continue
        break
    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числовые значения.")

while True:
    try:
        A = float(input("Введите стоимость шоколадных конфет (руб): "))
        if A < 0:
            print("Ошибка: Стоимость не может быть меньше 0.")
            continue
        break
    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числовые значения.")

while True:
    try:
        Y = float(input("Введите вес ирисок (кг): "))
        if Y <= 0:
            print("Ошибка: Вес должен быть больше 0.")
            continue
        break
    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числовые значения.")

while True:
    try:
        B = float(input("Введите стоимость ирисок (руб): "))
        if B < 0:
            print("Ошибка: Стоимость не может быть меньше 0.")
            continue
        break
    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числовые значения.")

price_chocolate = A / X
price_iris = B / Y

print("Цена шоколадных конфет:", price_chocolate)
print("Цена ирисок:", price_iris)

if price_iris == 0:
    print(
        "Невозможно вычислить, во сколько раз конфеты дороже, "
        "так как цена ирисок 0."
    )
else:
    times = price_chocolate / price_iris
    print(f"Шоколадные конфеты в {times} раза дороже ирисок")