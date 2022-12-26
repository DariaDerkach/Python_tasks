class Human:
    age = 0
    name = None

    def __init__(self, name, age, money, house):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(self.name, self.age, self.__house, self.__money)

    @staticmethod
    def default_info():
        print(Human.age, Human.name)

    def earn_money(self, money):
        self.__money += money


Human.default_info()
chel = Human('Vasia', 18, 10, None)
chel.info()
chel.earn_money(1500)
chel.info()