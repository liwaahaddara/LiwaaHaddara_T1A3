from os import system
import sys
from librarySeed import library_seed

catalogue = library_seed()
rented_books = []


def print_options():
    print(f"""
Welcome to Liwaa's Library! Please select an option
from the following menu:

1. Show Current Book Catalogue
2. Add book to the Catalogue
3. Delete a book
4. Rent a book from the Catalogue
5. Show books I'm currently renting
6. Exit
    """)
    opt = input("Select your option (1-6): ")

    return opt


def add_new_book():
    book_title = input("What's the title of the new book? ").title()
    book_author = input(f"\nWho is the author of {book_title}? ").title()

    if (len(book_title) != 0) and (len(book_author) != 0):
        catalogue.add_book(book_title, book_author)
        print(f"\n{book_title} has been added to the catalogue....")

    else:
        print("You need to include BOTH a title AND author name, try again!")


def delete_a_book():
    # Show the current list of books
    for book in catalogue.catalogue_items:
        print(book.title)
    # Ask which book you want deleted from the catalogue
    name = input("\nWhich book would you like deleted? ")
    response = catalogue.delete_book(name)

    print(response)
