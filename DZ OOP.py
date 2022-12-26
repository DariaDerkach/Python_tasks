"""1. Придумайте по одному своему примеру на каждую из парадигм:
Абстракция
Полиморфизм
Инкапсуляция
Наследование
Продемонстрировать работу данных классов, отвечающих за примеры парадигм ООП"""

"""
2. Два метода в классе, один принимает в себя либо строку, либо число.

Если передают строку, то смотрим:
если произведение гласных и согласных букв меньше или равно
длине слова, выводить все гласные, иначе согласные;
Если передают число то находим, произведение суммы чётных цифр на длину числа.

Длину строки и числа искать во втором методе"""

class Call_number_str:

    def __init__(self,str_1):
        self.str_1 = str_1

    def make_str(self,):


"""
3. Исправьте ошибки, правильный результат работы описан в конце

class Class1:

    def __init__(self, value):
        self.__var = value


    def read_set_del(self):
        print('Прочтено')
        return self.__var


    def read_set_del(self, value):
        self.__var = value
        print('Изменено')


    def read_set_del(self):
        del self.__var
        print('Удалено')

c1 = Class1(5)
c1.read_set_del = 35
c1.read_set_del
del c1.read_set_del

# Если все ошибки исправлена, то на экран должно выводиться:
# Прочтено
# Изменено
# Удалено



***4. Напишите программу, которая будет рандомно генирировать от 2 до 5 объектов класса Human.
У каждого объекта этого класса рандомным образом должны определяться следующие свойства:
1) Пол: Мужчина или Женщина
2) Рандомное имя в зависимости от пола:
М(Lionel McCoy, Charles Cross, John Pitz, Jeffry Young, Johnathan Randall, Edward Townsend, Lewis Pope)
Ж(Aubrey Gilmore, Avice Reynolds, Theresa Bradford, Shonda Douglas, Karen Sanders, Ruby Rice, Ruth Rice)
Можно дополнить своими вариантами
3) Возраст: от 18 до 100 лет
4) Характер: холерик или сангвиник или меланхолик или флегматик
5) Место работы: Рабочий или Безработный
6) Рандомный капитал от 100$ до 10000$
7) Рандомный ежемесячный доход от 1000$ до 5000$, при наличии работы. Если работы нет, то от 100$ до 300$.
8) Рандомная дата рождения в формате xx.xx.xxxx(тип Protected)
9) Рандомная дата смерти в формате xx.xx.xxxx(тип Protected)
10) Наличие дома: Свой дом или Аренда
11) Наличие машины: Есть или нет
12) Семейное положение: Свободен или Женат/Замужем в зависимости от пола
13) Дата свадьбы, если статус Женат/Замужем присвоен сразу, то рандомная дата
в формате xx.xx.xxxx(тип Protected) в диапазоне от даты рождения +18 лет до текущего возраста
Если изначально статус свободен, то значение None
14) Ежемесячные расходы 30% от ежемесячного дохода

Создать метод info() с информацией о каждом объекте класса Human

Создать метод life() который ежегодно(1 итерация цикла) будет прибылвять 1 год объекту класса Human
Добавить шанс 1/30, что жизнь может оборваться преждевременно, в таком случае изменить дату смерти

Создать метод jobs() который ежегодно(1 итерация цикла) будет определять появиться ли работа у того,
у кого ее не было, или уволят ли того, у кого работа была и перезавписывать это свойство объекта.
Если характер "холерик", то шансы устроиться на работу 1/2, шансы быть уволеным 1/7
Если характер "сангвиник", то шансы устроиться на работу 1/3, шансы быть уволеным 1/10
Если характер "меланхолик", то шансы устроиться на работу 1/7, шансы быть уволеным 1/6
Если характер "флегматик", то шансы устроиться на работу 1/5, шансы быть уволеным 1/20
Добавить счётчик, который посчитает кол-во работ за всю жизнь.

Создать метод wedding() который ежегодно(1 итерация цикла) будет определять появиться ли вторая
половинка, если ее не было. От 18 до 30 лет шансы 1/4, от 31 до 45 шансы 1/7,
от 46 до 65 шансы 1/12, от 66+ шансы 1/20
Метод должен перезаписывать дату свадьбы

Создать метод salary() который ежегодно будет увеличивать капитал объекта согласно его доходу.
Добавить шанс 1/4 что доход может измениться в рандом диапазоне от 1000$ До 5000$.

Создать метод expenses() который ежегодно будет отнимать расходы от капитала
При наличии арендного жилья расходы должны увеличиваться на 15%, при собственном жилье только на 7%
При наличии авто расходы должны увеличиваться на 13%

Создать метод house() который ежегодно с шансом 1/4 будет определять, появиться ли у обекта свой
дом, если его еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
цену дома при покупке. Цена дома генирируется рандомно каждый год от 20000$ до 50000$

Создать метод car() который ежегодно с шансом 1/3 будет определять, появиться ли у обекта своя
машина, если ее еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
цену машины при покупке. Цена машины генирируется рандомно каждый год от 5000$ до 100000$


Как только все объекты умрут, добавить возможность выбора о каком объекте вывести информацию
на экран. Информация должна быть сначала изначальной, потом на конец жизни, чтобы можно было
сравнить данные.
"""
