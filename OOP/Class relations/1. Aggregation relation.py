# Aggregation vs Composition
# ------------------------------------------------------------
# 1. Aggregation = "Has-A" relationship
#   - The containing object has references to other INDEPENDENT objects
#   - The parts (objects) can outlive the whole
#
# One object (the "whole") contains references 
# to one or more independent objects (the "parts").
#
# Key point: The "parts" can exist independently 
# of the "whole". 
# For example, books exist even without a library.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # collection of Book objects

    def add_book(self, book):       # 'book' is now a variable, but it will contain objects
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
      # ['Harry Potter... by J.K. Rowling', 'The Hobbit by J. R. R. Tolkien', 'The Colour of Magic by Terry Pratchett']
# -------------------------------------------------------------------------- #


# Creating books (they exist independently of any library)
book1 = Book("Harry Potter...", "J.K. Rowling")
book2 = Book("The Hobbit", "J. R. R. Tolkien")
book3 = Book("The Colour of Magic", "Terry Pratchett")

# Creating a library and aggregating books into it
library = Library("Alexandria Library:")

# Passing in objects
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display library and its books
print(library.name)
for book in library.list_books():
    print(book)

# Proving independence: books still exist outside the library
print("\nBooks still exist independently:")
print(book1.title)
print(book2.title)


# https://www.youtube.com/watch?v=caXOUnQkD1o&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=55