"""
 Помидоры. Класс Tomato.

Помидор может:
1. Расти (переходить на следующую стадию созревания)
2. Предоставлять информацию о своей зрелости

Атрибуты:
- **index** - номер
- **ripeness** - стадия зрелости (Отсутствует, Цветение, Зеленый, Красный)
- **states** - атрибут класса, в котором кортеж со стадиями зрелости (Отсутствует, Цветение, Зеленый, Красный)

Методы:
- инициализатор **\_\_init\_\_**, который принимает index и присваивает его self.index,
  а self.ripeness устанавливается первым значением из self.states
- метод **grow()**, который будет переводить томат на следующую стадию созревания
- метод **is_ripe()**, который будет проверять, что томат созрел (достиг последней стадии созревания).
  Должен возвращать True или False
"""


class Tomato:
    index: int
    ripeness: str
    states: tuple = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index: int):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        if self.ripeness != self.states[3]:
            self.ripeness = self.states[self.states.index(self.ripeness) + 1]
            return self.ripeness

    def is_ripe(self):
        if self.ripeness == self.states[3]:
            return True
        else:
            return False
