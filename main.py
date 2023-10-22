# import gc

book_list = []

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

# def add_book(title, author):
#     new_book = dict(title = title, author = author)
#     book_list.append(new_book)

book1 = Book("title", "author")
book_list.append(book1)

title = input("Enter book title: ").lower()
author = input("Enter author: ").lower()
new_book = Book(title, author)
if new_book in book_list:
    del new_book
    print("We got it!")

# for ob in gc.get_objects():
#     if isinstance(ob, Book):
#         print(ob.title, ob.author)