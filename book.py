'''The following class (Book) creates an individual entry, 
containing both a title and author name'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Book Title: {self.title},\nAuthor: {self.author}\n")
