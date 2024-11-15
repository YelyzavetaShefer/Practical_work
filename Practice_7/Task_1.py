library = {
    "1984": {
        "author": "George Orwell",
        "year": 1949,
        "available": True,
        "borrower": None
    },
    "Kobzar": {
        "author": "Taras Shevchenko",
        "year": 1840,
        "available": True,
        "borrower": None
    },
    "The Goldfinch": {
        "author": "Donna Tartt",
        "year": 2013,
        "available": False,
        "borrower": "Yelyzaveta Shefer"
    },
    "The Secret History": {
        "author": "Donna Tartt",
        "year": 1992,
        "available": True,
        "borrower": None
    }
}
def add_book(title, author, year):
    library[title] = {
        "author": author,
        "year": year,
        "available": True,
        "borrower": None
    }
title = input("Please,enter the title of the book: ")
author = input("Please, enter the author of the book: ")
year = input("Please, enter the year the book was published: ")
add_book(title, author, year)
print(library)

def borrow_book(title, borrower):
    if title in library.keys():
        if library[title]["available"]:
            library[title]["available"] = False
            library[title]["borrower"] = borrower
        else:
            print("Sorry, this book is borrowed.")
    else:
        print("Sorry, we don't have this book in our library.")
title = input("Please, enter title: ")
borrower = input("Please, enter your name: ")
borrow_book(title, borrower)
print(library)

def return_book(title):
    if title in library.keys():
        if library[title]["available"] == False:
            library[title]["available"] = True
            library[title]["borrower"] = None
    else:
        print("Sorry, we don't have this book in our library.")
title = input("Please, enter title: ")
return_book(title)
print(library)

