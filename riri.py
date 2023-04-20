class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author}"

class FictionBook(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn, genre)

    def __str__(self):
        return f"{self.title} by {self.author} (Fiction)"

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn, genre)

    def __str__(self):
        return f"{self.title} by {self.author} (Non-fiction)"

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to inventory.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"{book.title} removed from inventory.")
                return
        print(f"No book found with ISBN {isbn}.")

    def search_books(self, title=None, author=None, isbn=None, genre=None):
        search_results = []
        for book in self.books:
            if title and title.lower() not in book.title.lower():
                continue
            if author and author.lower() not in book.author.lower():
                continue
            if isbn and isbn != book.isbn:
                continue
            if genre and genre.lower() != book.genre.lower():
                continue
            search_results.append(book)
        return search_results

    def display_inventory(self):
        print("Inventory:")
        for book in self.books:
            print(f"\t{book}")
inventory = LibraryInventory()

# Adding books to the inventory
inventory.add_book(FictionBook("The Catcher in the Rye", "J.D. Salinger", "9780316769174", "Drama"))
inventory.add_book(NonFictionBook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "9780062316110", "History"))

# Displaying the inventory
inventory.display_inventory()

# Searching for a book
book = inventory.search_books(isbn="9780316769174")
print("\nSearch result: ")
print(book[0])

# Removing a book
inventory.remove_book("9780316769174")

# Displaying the inventory after removal
print("\nInventory after removal: ")
inventory.display_inventory()