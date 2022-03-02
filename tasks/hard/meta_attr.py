"""
Предположим, нас утомило задание атрибутов в конструкторе init(self, *args,
**kwargs). Хотелось бы ускорить этот процесс таким образом, чтобы была
возможность задавать атрибуты прямо при создании объекта класса.

class Man:
    pass

me = Man(height = 180, weight = 80)
TypeError: Man() takes no arguments

Сделать возможным данный механизм с помощью метакласса DynamicInitMeta
"""


class DynamicInitMeta(type):
    def __call__(cls, *args, **kwargs):
        new_object = type.__call__(cls, *args)
        for name in kwargs:
            setattr(new_object, name, kwargs[name])
        return new_object
