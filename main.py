import random

book_list = [
    {'title': 'title', 'author': 'author', 'pages': 200, 'currently_reading': False, 'pages_read': 0},
    {'title': 'title2', 'author': 'author2', 'pages': 300, 'currently_reading': False, 'pages_read': 0}, 
    {'title': 'title3', 'author': 'author3', 'pages': 500, 'currently_reading': False, 'pages_read': 0},
    ]

def add_book(new_title, new_author, new_pages, currently_reading = False, pages_read = 0):
    new_book = dict(title = new_title, author = new_author, pages = new_pages, currently_reading = currently_reading, pages_read = pages_read)
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
    print(f"{book_list[index - 1]['title']} by {book_list[index - 1]['author']} has been deleted.")
    del book_list[index - 1]


def set_current_book(index):
    book_list[index -1]["currently_reading"] = True
    print(f"Enjoy reading {book_list[index - 1]['title']} by {book_list[index - 1]['author']}!")

def get_random_book():
    random_book = random.choice(book_list)
    print(f"Why not try {random_book['title']} by {random_book['author']}?")

def set_book_pages(index, new_pages):
    if new_pages > book_list[index - 1]["pages"]:
        print(f"{book_list[index - 1]['title']} by {book_list[index - 1]['author']} is only {book_list[index - 1]['pages']} pages long.")
    elif new_pages == book_list[index - 1]["pages"]:
        print("You're all finished!")
        delete_book(index)
    else:
        book_list[index - 1]['pages_read'] = new_pages
        print(f"Only {book_list[index - 1]['pages'] - book_list[index - 1]['pages_read']} pages to go!")

def set_book_percent(index, new_percent):
    while new_percent < 0 or new_percent > 100:
        new_percent = input("Please enter a valid percentage between 0 and 100.")
    else:
        book_list[index - 1]["pages_read"] = round((float(new_percent) * float(book_list[index - 1]["pages"])) / 100) 

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
set_book_percent(2, 89)
print(book_list)