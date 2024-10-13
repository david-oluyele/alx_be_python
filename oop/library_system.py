# Base Class - Book
class Book:
    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a user-friendly string representation of the Book."""
        return f"Book: {self.title} by {self.author}"

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the eBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a user-friendly string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a user-friendly string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library's collection."""
        for book in self.books:
            print(book)
