class Book:
    def __init__(self, name, author, year):
        self.name = name
        self._author = author
        self.__year = year

    def title(self):
        print(f"Название книги: {self.name}\nАвтор: {self._author}\nГод публикации: {self.__year}")

privat_book = Book('Стрелок', 'Стивен Кинг', 1982)
privat_book.title()
print(privat_book._author)
print(privat_book.__year)