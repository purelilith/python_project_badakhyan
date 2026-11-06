# Из словаря my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York',
# 'profession': 'Doctor'} удалить 'profession', вывести все пары
# ключ-значение и проверить наличие 'age'.

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York',
           'profession': 'Doctor'}

if 'profession' in my_dict:
    del my_dict['profession']

for key, value in my_dict.items():
    print(f"{key}: {value}")

if 'age' in my_dict:
    print("Ключ 'age' есть в словаре")
else:
    print("Ключа 'age' нет в словаре")