import random


class Human:
    sex: str
    name: str
    age: int
    character: str
    job: str
    capital: int
    monthly_income: int
    _date_of_birth: str
    _date_of_death: str
    house: str
    car: str
    family_status: str
    wedding_date: str
    monthly_expenses: float

    sex_human = ["man", "woman"]
    man = ["Lionel McCoy", "Charles Cross", "John Pitz", "Jeffry Young", "Johnathan Randall", "Edward Townsend",
           "Lewis Pope"]
    woman = ["Aubrey Gilmore", "Avice Reynolds", "Theresa Bradford", "Shonda Douglas", "Karen Sanders", "Ruby Rice",
             "Ruth Rice"]
    character_human = ["choleric", "sanguine", "phlegmatic", "melancholic"]
    job_human = ["employed", "unemployed"]
    house_human = ["own", "rental"]
    car_human = ["yes", "no"]
    family_status_human = ["married", "single"]

    def __init__(self):

        self.sex = random.choice(self.sex_human)
        if self.sex == "man":
            self.name = random.choice(self.man)
        else:
            self.name = random.choice(self.woman)
        self.age = random.randint(18, 100)
        self.character = random.choice(self.character_human)
        self.job = random.choice(self.job_human)
        self.capital = random.randint(100, 10000)
        if self.job == "employed":
            self.monthly_income = random.randint(1000, 5000)
        else:
            self.monthly_income = random.randint(100, 300)
        day_of_birth = random.randint(0, 31)
        if day_of_birth < 10:
            day_of_birth = "0" + str(day_of_birth)
        else:
            day_of_birth = str(day_of_birth)
        month_of_birth = random.randint(1, 12)
        if month_of_birth < 10:
            month_of_birth = "0" + str(month_of_birth)
            if month_of_birth == "02":
                day_of_birth = random.randint(0, 28)
                if day_of_birth < 10:
                    day_of_birth = "0" + str(day_of_birth)
                else:
                    day_of_birth = str(day_of_birth)
        else:
            month_of_birth = str(month_of_birth)
        year_of_birth = 2023 - self.age
        self._date_of_birth = day_of_birth + "." + month_of_birth + "." + str(year_of_birth)

        day_of_death = random.randint(0, 31)
        if day_of_death < 10:
            day_of_death = "0" + str(day_of_death)
        else:
            day_of_death = str(day_of_death)
        month_of_death = random.randint(1, 12)
        if month_of_death < 10:
            month_of_death = "0" + str(month_of_death)
            if month_of_death == "02":
                day_of_death = random.randint(0, 28)
                if day_of_death < 10:
                    day_of_death = "0" + str(day_of_death)
                else:
                    day_of_death = str(day_of_death)
        else:
            month_of_death = str(month_of_death)
        year_of_death = 2023 + (100 - self.age)
        self._date_of_death = day_of_death + "." + month_of_death + "." + str(year_of_death)
        self.house = random.choice(self.house_human)
        self.car = random.choice(self.car_human)
        self.family_status = random.choice(self.family_status_human)

        day_of_married = random.randint(0, 31)
        if day_of_married < 10:
            day_of_married = "0" + str(day_of_married)
        else:
            day_of_married = str(day_of_married)
        month_of_married = random.randint(1, 12)
        if month_of_married < 10:
            month_of_married = "0" + str(month_of_married)
            if month_of_married == "02":
                day_of_married = random.randint(0, 28)
                if day_of_married < 10:
                    day_of_married = "0" + str(day_of_married)
                else:
                    day_of_married = str(day_of_married)
        else:
            month_of_married = str(month_of_married)
        year_of_married = random.randint((2023 - self.age + 18), 2023)
        if self.family_status == "married":
            self.wedding_date = day_of_married + "." + month_of_married + "." + str(year_of_married)
        else:
            self.wedding_date = "None"
        self.monthly_expenses = self.monthly_income * 0.3

    def info(self):
        print(f"Sex:{self.sex}   Name:{self.name}   Age:{self.age}  Character:{self.character}   Job:{self.job} "
              f"   Capital:{self.capital}   Monthly income:{self.monthly_income} Date of birth:{self._date_of_birth}"
              f"   Date of death:{self._date_of_death}   House:{self.house}   Car:{self.car}   "
              f"   Family status:{self.family_status}  Wedding date:{self.wedding_date}  "
              f"Monthly_expenses:{self.monthly_expenses}\n")

    def life(self):
        self.age += 1
        print(self.age)


if __name__ == '__main__':

    h1 = Human()
    h1.info()
    #
    # h2 = Human()
    # h3 = Human()

    while h1.age < 100:

        h1.life()


    # h2.life()
    # h2.info()
    # h3.info()
