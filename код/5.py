class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def title(self):
        print(f"Название книги: {self.name}\nАвтор: {self.author}\nГод публикации: {self.year}")


class FictionGenres(Book):
    def __init__(self, name, author, year, genre):
        super().__init__(name, author, year)
        self.genre = genre

    def info(self):
        print(f"Книга '{self.name}', {self.author} ({self.year}г.) находится в разделе '{self.genre}'")

class NonFictionGenres(Book):
    def __init__(self, name, author, year, genre):
        super().__init__(name, author, year)
        self.genre = genre

    def info(self):
        print(f"Книга '{self.name}', {self.author} ({self.year}г.) находится в разделе '{self.genre}'")

book_1 = FictionGenres("Жутко громко и запредельно близко", "Джонатан Сафран Фоер", 2005, "Романы")
book_1.info()
book_2 = NonFictionGenres("К себе нежно", "Ольга Примаченко", 2020, "Литература по саморазвитию")
book_2.info()


