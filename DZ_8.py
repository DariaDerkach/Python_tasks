"""1. Программа принимает на вход две строки и находит в них
общие буквы. Решить через множества"""

set_1 = set(input())
set_2 = set(input())
print(set_1 & set_2)

"""
2. Программа принимает на вход две строки и выводит на экран
все буквы из первой строки, которые отсутствуют во второй строке.
Решить через множества"""

set_3 = set(input())
set_4 = set(input())
print(set_3 - set_4)

"""
3. Муж решил дарить своей жене каждый день цветы, но так чтобы в
течении недели не повторяться. Он знает, что ей нравятся:
розы, тюльпаны, ромашки, нарциссы, васильки, хлопок и амариллис.

Напишите программу, которая будет принимать на вход с клавиатуры
день недели и название цветка. В подсказке при вводе с клавиатуры
должны выводиться цветы, которые муж еще не дарил на этой недели.
(Использовать множества)
Если цветок был подарен, то на следующей день(следующая итерация)
он не должен выдаваться в подсказке, но если пользователь введет
название этого цветка, который он уже дарил на этой неделе, то ему
на экран должна вывестись информация о том в какой день он дарил
этот цветок(хранить эту инфу в словаре)
Подаренные цветы и полный список цветов, которые нравятся жене
хранить во множествах. 
По истечении 7 дней(7 итераций) список
цветов(который пишется в подсказке) из которых можно выбирать
подарок должен сбрасываться.
Также добавьте возможность добавлять и удалять цветы введеные с
клавиатуры при желании пользователя."""

# flower_all = {'розы', 'тюльпаны', 'ромашки', 'нарциссы', 'васильки', 'хлопок', 'амариллис'}
# week = {"понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"}
# flower_gift = set()
# dict_fl = {}
# a = 0
# while a <= 7:
#     fl = input("Введите название цветка:")
#     flower_gift.add(fl)
#     day = input("Введите день недели:")
#     dict_fl[fl] = day
#     a += 1
#     print(flower_gift)
#     print(dict_fl)

""""
4. Напишите программу, которая будет принимать на вход название двух городов и запрашивать
расстояние из одного города в другой, а также кол-во населенных пунктов на этом пути,
после чего программа должна запрашивать их названия, максимально допустимую в них скрость
и их протяжонность в км. Всю эту информацию сохранять в файле. Если маршрут был уже сохранен
до этого, то программа должна пропускать этот шаг и сразу переходить к следующему.

После чего программа должна запрашивать время, за которое пользователь хочет добраться
из одного города в другой и выдавть среднюю скорость с которой пользователю нужно будет
проезжать участки, которые не относятся к населенным пунктам, чтобы успеть добраться за
отведенное время.

Добавьте также возможность вводить пользователю среднюю скорость, с которой он хочет
проезжать участки, которые не относятся к населенным пунктам и в таком случае программа
должна выдавать время, за которое он сможет добраться с такой скорость из одного города в другой.

Добавте возможность сохранять данные о своем автомобиле (расход топлива на 100км и обем бака),
чтобы после этого программа смогла воспользоваться этими данными и выполнить следующий шаг

**Добавтье возможность пользователю вводить сколько литров у него есть в баке, а также
информацию о заправках(название АЗС, например "№1", "№2" и т.д. и на каком километраже
они распалагаются, например весь маршрут будет 300км, а заправки №1 и №2 располагаются на
101-ом км и 230-ом км, а также цену на топливо) После программа должна определять нужно ли
пользователю дозаправлться в пути, на каких заправках это нужно сделать, чтобы кол-во остановок
было минимальным в пути. Пользователь не может заправить больше, чем объем его бака, это нужно
учитывать, а также нужно учитывать кол-во топлива в баке, которое останется с начала пути на
момент приезда на запраку.

*** Сделайте так, чтобы программа определяла самые оптимальные точки для остановок на дозаправку,
чтобы пользователь платил, как можно меньше за топливо. И программа дожна выдавать на экран
на каких заправках, сколько и на какую сумму нужно будет дозаправить
"""

"""
5. Джон решил изучать язык Python. Он знает, что для его освоения
ему нужно изучить следующие темы: Базовые типы данных, Строки,
Переменные, Условные операторы, Циклы, Списки, Кортежи, Словари,
Множества, Файлы, Функции и ООП.

Напишите программу, которая будет выводить по запросу с клавиатуры
следующее:
1) Все темы, которые необходимо изучить
2) Темы которые еще не изучены (Использовать множества)
3) Темы которые уже изучены (Использовать множества)
4) Прогресс в % сколько уже пройдено"""

tems = {"Базовые типы данных", "Строки",
        "Переменные", "Условные операторы", "Циклы", "Списки", "Кортежи", "Словари",
        "Множества", "Файлы", "Функции", "ООП"}
tems_learnd = set()
while True:
    a = input(
        f'Если хочешь посмотреть все темы(Нажми all)\nЕсли хочешь посмотреть темы которые еще не изучены(Нажми nl)\nЕсли хочешь посмотреть темы которые уже изучены(нажми l)\nЕсли хочешь посмотреть прогресс в процентах(нажми p)\nЕсли хочешь отметить изученную тему(нажми ad)\n')
    if a == "all":
        for i in tems:
            print(i)
        print()
        b = input(f"Хочешь выполнить еще какую нибудь операцию(Нажми yes -да,no -нет)\n")
        if b == "yes":
            continue
        else:
            break
    if a == "nl":
        if len(tems - tems_learnd) == 0:
            print("Вы выучили все темы")
            b = input(f"Хочешь выполнить еще какую нибудь операцию(Нажми yes -да,no -нет)\n")
            if b == "yes":
                continue
            else:

                break
        else:
            print(tems - tems_learnd)
            b = input(f"Хочешь выполнить еще какую нибудь операцию(Нажми yes -да,no -нет)\n")
            if b == "yes":
                continue
            else:
                break
    if a == "l":
        if len(tems_learnd) == 0:
            print("Еще ни одна тема не выучена")
            b = input(f"Хочешь выполнить еще какую нибудь операцию(Нажми yes -да,no -нет)\n")
            if b == "yes":
                continue
            else:
                break
        else:
            print(tems_learnd)
            b = input(f"Хочешь выполнить еще какую нибудь операцию(Нажми yes -да,no -нет)\n")
            if b == "yes":
                continue
            else:
                break
    if a == "ad":
        tems_learnd.add(input(f'Напиши какую тему изучил:'))
        b = input(f"Хочешь выполнить еще какую нибудь операцию(Нажми yes -да,no -нет)\n")
        if b == "yes":
            continue
        else:
            break
