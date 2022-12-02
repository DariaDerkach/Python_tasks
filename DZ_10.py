"""1. Написать функцию season, принимающую 1 аргумент — номер
месяца (от 1 до 12), и возвращающую время года, которому этот
месяц принадлежит (зима, весна, лето или осень). Номер месяца
вводить с клавиатуры"""


def season(num):
    if num == 12 or 1 <= num <= 2:
        return print("Зима")
    elif 3 <= num <= 5:
        return print("Весна")
    elif 6 <= num <= 8:
        return print("Лето")
    elif 9 <= num <= 11:
        return print("Осень")
    else:
        return print("Неверно введён номер месяца!")


season(int(input("Введите номер месяца (1-12): ")))

"""
2. Простейший калькулятор c введёнными двумя числами вещественного типа.
Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
Обработать ошибку: “Деление на ноль”
Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
"""


def calculate():
    operation = input(
        f'Пожалуйста выберите матемачискую операцию:\n+ для сложения\n- для вычитания\n* для умножения\n/ для деления\n0 для выхода из программы\n')
    if operation == "0":
        return print("Программа завершена")
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2), end="")
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2), end="")
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2), end="")
        print(number_1 * number_2)
    elif operation == '/':
        if number_2 != 0:
            print('{} / {} = '.format(number_1, number_2), end="")
            print(number_1 / number_2)
        else:
            print(f"На ноль делить нельзя, попробуйте еще раз")
            return calculate()
    elif operation == '0':
        return print("Программа завершена")

    else:
        print(f'Вы ввели неправильный оператор, попробуйте сначала')
        return calculate()


calculate()
"""
3. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
Если список, то посчитать кол-во букв и чисел в нём.
Число – кол-во нечётных цифр.
Строка – количество букв.
Сделать проверку со всеми этими случаями"""


def check(x):
    length = 0
    if isinstance(x, tuple):
        for i in x:
            i = str(i)
            length = length + len(i)
        print(length)
    if isinstance(x, list):
        str_l = list(filter(lambda i: type(i) == str, x))
        count_leters = len(''.join(str_l))
        print(count_leters)
        str_dig = list(filter(lambda i: type(i) == int, x))
        count_digit = len("".join(map(str, str_dig)))
        print(count_digit)

    if isinstance(x, int) or isinstance(x, float):
        x = list(str(x))
        print(*list(filter(lambda i: int(i) % 2 != 0, x)))

    if isinstance(x, str):
        print(len(x))


tuple_x = (1, 2, 3, "ghtf", "ggfgd")
list_x = [1, 25, 3, "ghtf", "ggfgd"]
digit_x = 125689
str_x = "fsedfsdf"
check(tuple_x)
check(list_x)
check(digit_x)
check(str_x)
