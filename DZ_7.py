"""1. Напишите программу, которая принимает аргумент в виде списка
и возвращает словарь, в котором каждый элемент списка является
и ключом и значением. Предполагается, что элементы списка будут
соответствовать правилам задания ключей в словарях."""


def dict_from_list(list1: list) -> dict:
    return dict(zip(list1, list1))


my_list = [1, 2, 3, 4, 5, 6, 8]
my_dict = dict_from_list(my_list)
print(my_dict)

"""
2. Есть словарь песен группы Depeche Mode

songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
Выведите общее время звучания всех песен.

Создайте список песен, время звучаниях которых больше 5 минут.

Создайте новый словарь тех песен, название которых 
состоит из одного слова."""

songsdict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
list_keys = list(songsdict.keys())
list_val = list(songsdict.values())
print(sum(list_val))

list_song = []
for i in list_val:
    if i > 5:
        list_song.append(list_keys[list_val.index(i)])
print(list_song)

for i in list_keys:
    if len(i.split()) != 1:
        songsdict.pop(i)
print(songsdict)

"""
3. В настольной игре Скрабл (Scrabble) каждая буква имеет 
определенную ценность. Очки распределяются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного 
пользователем слова. Будем считать, что на вход подается только 
одно слово, которое содержит только русские буквы.
Решить через словарь.
"""
# на вход подаются только большие буквы

dict_scrable = {"А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1, "Д": 2, "К": 2, "Л": 2, "М": 2,
                "П": 2, "У": 2, "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3, "Й": 4, "Ы": 4, "Ж": 5, "З": 5, "Х": 5, "Ц": 5,
                "Ч": 5, "Ш": 8, "Э": 8, "Ю": 8, "Ф": 10, "Щ": 10, "Ъ": 10}

word = list(input())
cost = 0
for i in word:
    cost = cost + dict_scrable[i]
print(cost)

"""
4. Данные об email-адресах студентов хранятся в словаре:
{'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

Нужно дополнить код таким образом, чтобы он вывел все адреса 
в алфавитном порядке и в формате имя_пользователя@домен."""

student = {'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
           'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
           'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

a, b, c = student.items()
student_sort = []
for i in a[1]:
    student_sort.append(i + "@" + a[0])
for i in b[1]:
    student_sort.append(i + "@" + b[0])
for i in c[1]:
    student_sort.append(i + "@" + c[0])

print(*sorted(student_sort))

"""5. Напишите программу, которая будет генирировать словарь
в котором ключами будут числа от 1 до 5, 
а значениями будут элементы списка: 
['orange', 'apple', 'mango', 'banana', 'fruits']"""

list_5 = ['orange', 'apple', 'mango', 'banana', 'fruits']
print({x: y for x, y in zip(range(5), list_5)})
