"""
Задача.

В блоке
```python
if __name__ == '__main__':
    pass
```
выполнить следующие задания:
1. Создать несколько объектов класса TomatoBush,
   в каждом из которых будет минимум по 2 помидора
2. Создайте объект Gardener, в который передать объекты, созданные в п.1
3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
4. Попробуйте собрать урожай
5. Если томаты еще не дозрели, продолжайте ухаживать за ними
6. Соберите урожай
7. Вывести сообщение о том, сколько томатов собрали
"""
from gardener import Gardener
from tomato import Tomato
from tomato_bush import TomatoBush

if __name__ == '__main__':
    tomato_1 = Tomato(1)
    tomato_2 = Tomato(2)
    tomato_3 = Tomato(3)
    tomato_4 = Tomato(4)
    bush_1 = TomatoBush(tomato_1, tomato_2)
    bush_2 = TomatoBush(tomato_3, tomato_4)
    gardener = Gardener('Marko', bush_1, bush_2)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    print(f"Собрано {len(gardener.harvest())} томатов")
