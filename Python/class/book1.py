

class Book:
    
    title = "Book title"
    author = "Abir"
    genre = "Ram ram"
    
    def value(self):
        return f"Book Author: {self.author}, and genre of book is {self.genre}"
    

book = Book()
print(book.title)
print(book.author)

print()

print(book.value())