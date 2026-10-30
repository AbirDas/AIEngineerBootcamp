
class Book:
    """ A Class to model a book"""
    
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.num_pages = 230
        
    def read_book(self):
        print(f"Reading {self.title} by {self.author}, contains pages: {self.num_pages}")
        
    def describe_book(self):
        print(f"{self.title} by {self.author}, gerne: {self.genre}")
        
    def update_book_detail(self, pages):
        self.num_pages = pages
        
    def __str__(self):
        return f"Book Title: {self.title}, writen by {self.author}, Gerne of this book is: {self.genre}"
        
    
book = Book("Bhagavad Gita", "Veda Vyasa", "Scripture")

book.describe_book()

print()

book.read_book()

print()
book.num_pages = 1008
book.read_book()

print()
book.update_book_detail(802)
book.read_book()

print()
print(str(book))