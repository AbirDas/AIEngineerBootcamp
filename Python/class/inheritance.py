from book2 import Book


class EBook(Book):
    
    def __init__(self, title, author, genre, filesize, format_):
        super().__init__(title, author, genre)
        self.filesize = filesize
        self.format = format_
    
    def download_book(self):
        print(f"Downloading {self.title} in format {self.format}, file_size is :{self.filesize}MB")
        
ebook = EBook(title="my life".title(), author="Abir", genre="software developer", filesize=100, format_="pdf")

print()
ebook.read_book();
print(str(ebook))

print()
ebook.download_book()