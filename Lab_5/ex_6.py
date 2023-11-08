# 6.Design a library catalog system with a base class
# LibraryItem and subclasses for different types of
# items like Book, DVD, and Magazine. Include methods
# to check out, return, and display information about each item.


class LibraryItem:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def get_year(self):
        return self.year

    def __str__(self):
        return f"\tTitle: {self.title}\n\tAuthor: {self.author}\n\tGenre: {self.genre}\n\tYear: {self.year}"


class Book(LibraryItem):
    def __init__(self, title, author, genre, year, ISBN, pages):
        super().__init__(title, author, genre, year)
        self.ISBN = ISBN
        self.pages = pages

    def get_pages(self):
        return self.pages

    def get_ISBN(self):
        return self.ISBN

    def __str__(self):
        return "Type BOOK\n" + super().__str__() + f"\n\tISBN: {self.ISBN}\n\tPages: {self.pages}"


class DVD(LibraryItem):
    def __init__(self, title, author, genre, year, length, rating):
        super().__init__(title, author, genre, year)
        self.length = length
        self.rating = rating

    def get_length(self):
        return self.length

    def get_rating(self):
        return self.rating

    def __str__(self):
        return "Type DVD\n " + super().__str__() + f"\n\tLength: {self.length}\n\tRating: {self.rating}"


class Magazine(LibraryItem):
    def __init__(self, title, author, genre, year, pages):
        super().__init__(title, author, genre, year)
        self.pages = pages

    def get_pages(self):
        return self.pages

    def __str__(self):
        return "Type MAGAZINE\n" + super().__str__() + f"\n\tPages: {self.pages}"


book = Book("Sharp Objects", "Gilian Flynn", "Thriller", 2013, "9780753822210", 336)
print(book)

dvd = DVD("The Godfather", "Francis Ford Coppola", "Crime", 1972, 175, "9.2/10")
print(dvd)

magazine = Magazine("National Geographic", "Various", "Science", 2019, 100)
print(magazine)
