"""
Дом. Класс House - файл house.py

Дом может:
1. Предоставлять информацию о себе
2. Изменять свою стоимость

Атрибуты:
- **address** - адрес дома
- **area** - площадь дома
- **cost** - стоимость дома

Методы:
- инициализатор **__init__**, который принимает адрес, площадь и начальную стоимость дома
- метод **increase_cost()**, который принимает значение, на которое нужно увеличить self.cost
- метод **decrease_cost()**, который принимает значение, на которое нужно уменьшить self.cost
"""


class House:
    address: str
    area: float
    cost: float

    def __init__(self, address: str, area: float, cost: float):
        self.address = address
        self.cost = cost
        self.area = area

    def increase_cost(self, value: float):
        self.cost += value

    def decrease_cost(self, value: float):
        self.cost -= value
