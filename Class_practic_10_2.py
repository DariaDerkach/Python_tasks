class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        self.discount = discount
        self._price -= discount
        print(self._price)


class SmallHouse(House):
    def __init__(self, area, price):
        super().__init__(area, price)
        self.area = 40

house_1 = House(20,2000)
print(house_1)

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

    def __make_deal(self,money,h=House()):
       self.__money = money - House.final_price
       self.__house = h

    def buy_house(self,money,House.final_price)

# Human.default_info()
# chel = Human('Vasia', 18, 10, None)
# chel.info()
# chel.earn_money(1500)
# chel.info()