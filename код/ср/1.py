class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year


first_book = Book('Стрелок', 'Стивен Кинг', 1982)
print(first_book.name)
print(first_book.author)
print(first_book.year)
