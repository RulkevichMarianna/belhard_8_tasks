""" Таунхаус. Класс Townhouse - подкласс House, файл townhouse.py

Типовой дом

Методы:
- инициализатор **__init__**, который принимает адрес и начальную стоимость дома.
  self.area по умолчанию присваиваем 60
"""
from house import House


class Townhouse(House):

    def __init__(self, address: str, cost: float):
        super().__init__(address, 60, cost)
