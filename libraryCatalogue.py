import imp
from libraryBook import LibraryBook
from os import system


class LibraryCatalogue():
    # a list of books in the catalogue
    def __init__(self, catalogue_items):
        self.catalogue_items = catalogue_items

    # prints the current catalogue
    def print_catalogue(self):
        system("clear")
        print("\n\nHere is our catalogue:\n")
        for book in self.catalogue_items:
            book.show_book()

    # this function adds a book to the catalogue
    def add_book(self, title, author):
        new_book = LibraryBook(title, author)
        self.catalogue_items.append(new_book)
