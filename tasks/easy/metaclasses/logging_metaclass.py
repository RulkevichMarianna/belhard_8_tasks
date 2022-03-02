"""
Написать логгирующий декоратор log_decorator, который будет логгировать
вызов функции. До выполнения функции необходимо вывести в консоль строку
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}". А после вывести
строку "Выполнено {func.__name__}".

Написать логгирующий метакласс LogMeta, который ко всем методам класса добавляет
функционал декоратора log_decorator.
"""


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result

    return wrapper


class LogMeta(type):
    def __new__(mcs, name, bases, attrs):
        functions = {
            name: value for name, value
            in attrs.__dict__.items()
            if callable(value) and not name.startswith("_")}
        for name, func in functions.items():
            func_with_decor = log_decorator(func)
            attrs[name] = func_with_decor
        new_class = super().__new__(mcs, name, bases, attrs)
        return new_class
