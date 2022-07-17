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
