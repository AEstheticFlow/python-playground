# ---------- Magic (Dunder) Methods ----------
# Magic methods = Special methods in Python with double underscores (__method__)
#                Automatically called by Python in certain operations
#                Allow developers to customize how objects behave with:
#                - Initialization
#                - String & Debug representation
#                - Comparisons
#                - Arithmetic operations
#                - Membership tests
#                - Indexing
#                - Length, Callable behavior, and more

class Book:
    # ---------- Object Initialization ----------
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # ---------- Representation ----------
    def __str__(self):
        """Human-readable string (user-friendly output, e.g., print(book))"""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Unambiguous developer/debugging string (e.g., in a list of objects)"""
        return f"Book(title='{self.title}', author='{self.author}', num_pages={self.num_pages})"

    # ---------- Comparisons ----------
    def __eq__(self, other):
        """Checks if two books are equal (same title and author)"""
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        """Checks if this book has fewer pages than another"""
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        """Checks if this book has more pages than another"""
        return self.num_pages > other.num_pages

    # ---------- Arithmetic ----------
    def __add__(self, other):
        """Combines page counts of two books"""
        return f"{self.num_pages + other.num_pages} pages"

    # ---------- Membership ----------
    def __contains__(self, keyword):
        """Allows 'in' keyword search in title or author"""
        return keyword in self.title or keyword in self.author

    # ---------- Indexing ----------
    def __getitem__(self, key):
        """Allows dictionary-like access to attributes"""
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

    # ---------- Length ----------
    def __len__(self):
        """Allows use of len(book) to get number of pages"""
        return self.num_pages

    # ---------- Callable ----------
    def __call__(self):
        """Allows the object itself to be called like a function"""
        return f"Reading '{self.title}' by {self.author}..."


# ---------- Example Usage ----------
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# Demonstrating Magic Methods in Action
print(book1)                        # __str__: Human-readable
print(repr(book1))                  # __repr__: Debug/developer-friendly
print(book1 == book3)              # __eq__: Equality comparison
print(book1 < book2)               # __lt__: Less-than comparison
print(book2 > book3)               # __gt__: Greater-than comparison
print(book1 + book2)               # __add__: Add page counts
print("Lion" in book3)             # __contains__: 'in' keyword
print(book3['title'])              # __getitem__: Dictionary-like indexing
print(len(book1))                  # __len__: Number of pages
print(book2())                     # __call__: Object behaves like a function


# https://www.youtube.com/watch?v=NwjSP1_WEfE&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=60