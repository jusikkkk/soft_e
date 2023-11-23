class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def title(self):
        print(f"Название книги: {self.name}\nАвтор: {self.author}\nГод публикации: {self.year}")


first_book = Book('Стрелок', 'Стивен Кинг', 1982)
first_book.title()