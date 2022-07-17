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


def rent_book(book_being_rented):
    for book in catalogue.catalogue_items:
        if book.title.lower() == book_being_rented.lower():
            rented_books.insert(len(rented_books),
                                catalogue.catalogue_items.pop(catalogue.catalogue_items.index(book)))

            return f"{book_being_rented.title()} has been rented."
    return f"{book_being_rented.title()} is not in the catalogue."


def rent_a_book():
    # Show the current list of books
    for book in catalogue.catalogue_items:
        print(book.title)
    # Ask which book you want deleted from the catalogue
    book_being_rented = input("\nWhich book would you like to rent? ")
    print(rent_book(book_being_rented))


def print_rented_books():
    system("clear")
    print("\n\nHere are the books you're currently renting:\n")
    for book in rented_books:
        book.show_book()


option = ""

while option != "6":
    system("clear")
    option = print_options()
    system("clear")
    if option == "1":
        catalogue.print_catalogue()
    elif option == "2":
        add_new_book()
    elif option == "3":
        delete_a_book()
    elif option == "4":
        rent_a_book()
    elif option == "5":
        print_rented_books()
    elif option == "6":
        continue
    else:
        print("Invalid operation, please try again!")

    input("\npress Enter to continue...")
    system("clear")

print("Enjoy your day!")
