import random

book_list = [
    {'title': 'title', 'author': 'author', 'pages': 200, 'currently_reading': False, 'progress': 0},
    {'title': 'title2', 'author': 'author2', 'pages': 300, 'currently_reading': False, 'progress': 0}, 
    {'title': 'title3', 'author': 'author3', 'pages': 500, 'currently_reading': False, 'progress': 0},
    ]

def add_book(new_title, new_author, new_pages, currently_reading = False, progress = 0):
    new_book = dict(title = new_title, author = new_author, pages = new_pages, currently_reading = currently_reading, progress = progress)
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

def delete_book(index):
    del book_list[index - 1]

def set_current_book(index):
    book_list[index -1]["currently_reading"] = True
    print(f"Enjoy reading {book_list[index - 1]['title']} by {book_list[index - 1]['author']}!")

def get_random_book():
    random_book = random.choice(book_list)
    print(f"Why not try {random_book['title']} by {random_book['author']}?")

def set_book_progress(index, new_progress):
    if new_progress > book_list[index - 1]["pages"]:
        print(f"{book_list[index - 1]['title']} by {book_list[index - 1]['author']} is only {book_list[index - 1]['pages']} pages long.")
    else:
        book_list[index - 1]['progress'] = new_progress
        print(f"Only {book_list[index - 1]['pages'] - book_list[index - 1]['progress']} pages to go!")


# while True:
#     new_title = input("Enter book title: ").lower()
#     new_author = input("Enter author: ").lower()
#     if check_book_dupes(new_title, new_author):
#         print(f"You have already added '{new_title}' by {new_author}.")
#         continue
#     else:
#         new_pages = int(input("Enter book pages: "))
#         add_book(new_title, new_author, new_pages)

#     continue_prompt = input("Would you like to add another book (y/n)?: ").lower()
#     while continue_prompt not in ["y", "n"]:
#         continue_prompt = input("Please enter 'y' to continue adding books or 'n' to stop: ").lower()
#     else:
#         if continue_prompt == 'n':
#             break
#         else:
#             continue


get_book_list()
set_book_progress(2, 250)
print(book_list)