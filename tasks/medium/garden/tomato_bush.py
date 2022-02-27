"""
Куст с помидорами. Класс TomatoBush.

Куст с помидорами может:
1. Расти вместе с томатами
2. Предоставлять информацию о зрелости всех томатов
3. Предоставлять урожай

Атрибуты:
- **tomato_list** - список всех томатов

Методы:
- инициализатор **\_\_init\_\_**, который принимает args - произвольное количество томатов
  и сохраняет их в self.tomato_list
- метод **grow_all()**, который будет переводить все объекты из списка томатов на следующий этап созревания
- метод **all_are_ripe()**, который будет возвращать True, если все томаты из списка стали спелыми, False, если нет
- метод **give_away_all()**, который будет возвращать список томатов и очищать его на кусте томатов после сбора урожая

"""

class TomatoBush:
    tomato_list: list

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow()

    def all_are_ripe(self):
        all_tomato = 0
        for tomato in self.tomato_list:
            if tomato.is_ripe():
                all_tomato += 1
        if all_tomato == len(self.tomato_list):
            return True
        else:
            return False

    def give_away_all(self):
        give_away_tomato = self.tomato_list.copy()
        self.tomato_list.clear()
        return give_away_tomato


