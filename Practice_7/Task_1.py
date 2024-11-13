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
    }
}
def add_book(title, author, year):
    library[title] = {
        "author": author,
        "year": year
    }

