
'''The following function (library_seed) instantiates a library catalogue with
a few books, each containing a title and author
'''


from libraryBook import LibraryBook
from libraryCatalogue import LibraryCatalogue


def library_seed():
    book1 = LibraryBook("English Year 12", "Robert Beardwood")
    book2 = LibraryBook("Great Breakthroughs in Mathematics", "Robert Snedden")
    book3 = LibraryBook("Introducing Arabic", "Michael Mumisa")

    return LibraryCatalogue([book1, book2, book3])
