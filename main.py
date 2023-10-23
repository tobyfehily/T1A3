import random

book_list = [
    {'title': 'title', 'author': 'author', 'pages': 200},
    {'title': 'title2', 'author': 'author2', 'pages': 300}, 
    {'title': 'title3', 'author': 'author3', 'pages': 500}
    ]

def add_book(new_title, new_author, new_pages):
    new_book = dict(title = new_title, author = new_author, pages = new_pages)
    book_list.append(new_book)
    print(f"{new_title} by {new_author} has been added.")

def check_book_dupes(new_title, new_author):
    for book in book_list:
        if book['title'] == new_title and book['author'] == new_author:
            return True
    return False

def get_book_list():
    for i, book in enumerate(book_list):
        print(f"{i + 1}: '{book['title']}' by {book['author']}")

def remove_book(index):
    del book_list[index - 1]

def get_random_book():
    random_book = random.choice(book_list)
    print(f"Why not try {random_book['title']} by {random_book['author']}?")




while True:
    new_title = input("Enter book title: ").lower()
    new_author = input("Enter author: ").lower()
    if check_book_dupes(new_title, new_author):
        print(f"You have already added '{new_title}' by {new_author}.")
        continue
    else:
        new_pages = int(input("Enter book pages: "))
        add_book(new_title, new_author, new_pages)

    continue_prompt = input("Would you like to add another book (y/n)?: ").lower()
    while continue_prompt not in ["y", "n"]:
        continue_prompt = input("Please enter 'y' to continue adding books or 'n' to stop: ").lower()
    else:
        if continue_prompt == 'n':
            break
        else:
            continue


get_book_list()
print(book_list)
