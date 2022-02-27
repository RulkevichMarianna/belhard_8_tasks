""" Класс Person - файл person.py
Человек может:
1. Предоставить информацию о себе
2. Заработать деньги
3. Купить дом

Атрибуты:
- **name** - имя
- **age** - возраст
- **money** - количество денег
- **realty** - недвижимость (список домов)

Методы:
- инициализатор **__init__**, который принимает name и age, присваивает их
  self.name и self.age соответственно. self.cash присваивает 0, а self.realty присваивает пустой список
- метод **info()**, который будет выводить поля name, age, realty и money.
- метод **earn_money()**, который принимает значение, на которое нужно увеличить money
- метод **make_deal()**, который принимает объект класса House или Townhouse,
  и если у человека достаточно денег, то списывает их с money и добавляет объект дома к self.realty

"""


class Person:
    name: str
    age: int
    money: int
    realty: list

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(f"{self.name}, {self.age}, {self.realty}, {self.money}")

    def earn_money(self, value):
        self.money += value

    def make_deal(self, house):
        if self.money >= house.cost:
            self.money -= house.cost
            self.realty.append(house)
        else:
            print("Недостаточно денег")
