book_list = []

def add_book(title, author):
    new_book = dict(title = title, author = author)
    book_list.append(new_book)

title = input("Enter book title: ")
author = input("Enter author: ")
add_book(title, author)
