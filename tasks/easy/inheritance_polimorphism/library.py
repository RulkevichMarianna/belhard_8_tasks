"""
Определить класс Person:

- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone

Описать класс LibraryReader, который наследуется от Person:

- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены

Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""


class Person:
    fullname: str
    phone: str

    def __init__(self, fullname: str, phone: str):
        self.fullname = fullname.title()
        self.phone = phone


class LibraryReader(Person):
    uid: int
    books: set

    def __init__(self, fullname: str, phone: str, uid: int, books: set = set()):
        super().__init__(fullname, phone)
        self.uid = uid
        self.books = books

    def take_books(self, *args):
        self.books.update(args)
        if len(args) <= 3:
            return f"{self.fullname} взял(а) книги: {', '.join(sorted(self.books))}"
        else:
            return f"{self.fullname} взял(а) 4 книги"

    def return_book(self, *args):
        return_books = set(args)
        lost_books = return_books.difference(self.books)
        if not lost_books:
            if len(return_books) <= 3:
                self.books = self.books.difference(args)
                return f"{self.fullname} вернул(а) книги: {', '.join(sorted(return_books))}"
            else:
                self.books = self.books.difference(args)
                return f"{self.fullname} вернул(а) 4 книги"
        else:
            raise ValueError(f"{self.fullname} не брал(а): {', '.join(sorted(lost_books))}")
