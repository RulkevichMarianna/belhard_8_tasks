"""
Задача. Файл main.py

В блоке
```python
if __name__ == '__main__':
    pass
```
выполнить следующие задания:
1. Создать несколько объектов классов House и Townhouse
2. Создайте объект Person
3. Используя объект класса Person, увеличить количество денег
4. Попробуйте купить дома
5. Если денег не достаточно, то продолжить увеличивать количество денег
"""
from house import House
from person import Person
from townhouse import Townhouse

if __name__ == '__main__':
    house_1 = House("Minsk", 70, 80000)
    house_2 = House('Minsk', 40, 50000)
    townhouse_1 = Townhouse("Minsk", 70000)
    townhouse_2 = Townhouse('Minsk', 90000)
    person = Person("Ivan", 40)
    person.earn_money(40000)
    person.make_deal(house_1)
    person.earn_money(40000)
    person.make_deal(house_1)
    person.earn_money(90000)
    person.make_deal(townhouse_1)
