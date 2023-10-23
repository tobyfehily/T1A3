import random

book_list = [
    {'title': 'Doppelganger', 'author': 'Naomi Klein', 'pages': 416, 'tags': ['non-fiction'], 'currently_reading': True, 'pages_read': 0},
    {'title': 'I, Claudius', 'author': 'Robert Graves', 'pages': 468, 'tags': ['non-fiction', 'ancient rome'], 'currently_reading': True, 'pages_read': 0}, 
    {'title': 'Python for Dummies', 'author': 'Stef Maruch', 'pages': 432, 'tags': ['non-fiction', 'python'], 'currently_reading': False, 'pages_read': 0},
    ]

def add_book(new_title, new_author, new_pages, new_tags = [], currently_reading = False, pages_read = 0):
    new_book = dict(title = new_title, author = new_author, pages = new_pages, tags = new_tags, currently_reading = currently_reading, pages_read = pages_read)
    book_list.append(new_book)
    print(f"{new_title} by {new_author} has been added.")

def check_book_dupes(new_title, new_author):
    for book in book_list:
        if book['title'] == new_title and book['author'] == new_author:
            return True
    return False

def get_tags(tags_list):
    unique_tags = []
    for i in tags_list:
        unique_tags.extend(i['tags'])
    for x in set(unique_tags):
        print(x)

def get_book_list():
    for i, book in enumerate(book_list):
        print(f"{i + 1}: '{book['title']}' by {book['author']}")

def get_random_book():
    random_book_list = []
    for book in book_list:
        if not book['currently_reading']:
            random_book_list.append(book)
    random_book = random.choice(random_book_list)
    print(f"Why not try '{random_book['title']}' by {random_book['author']}?")

def delete_book(index):
    try:
        print(f"{book_list[index - 1]['title']} by {book_list[index - 1]['author']} has been deleted.")
        del book_list[index - 1]
    except IndexError:
        print("Selection out of range")

def set_current_book(index):
    try:
        if book_list[index -1]["currently_reading"]:
            print(f"You're already reading {book_list[index - 1]['title']} by {book_list[index - 1]['author']}")
        else:
            book_list[index -1]["currently_reading"] == True
            print(f"Enjoy reading {book_list[index - 1]['title']} by {book_list[index - 1]['author']}!")
    except IndexError:
        print("Selection out of range")

def set_book_pages(index, new_pages):
    try:
        if new_pages > book_list[index - 1]["pages"]:
            print(f"{book_list[index - 1]['title']} by {book_list[index - 1]['author']} is only {book_list[index - 1]['pages']} pages long.")
        elif new_pages == book_list[index - 1]["pages"]:
            print("You're all finished!")
            delete_book(index)
        else:
            book_list[index - 1]['pages_read'] = new_pages
            print(f"Only {book_list[index - 1]['pages'] - book_list[index - 1]['pages_read']} pages to go!")
    except ValueError:
        print("Please enter a number.")

def set_book_percent(index, new_percent):
    try:
        while new_percent < 0 or new_percent > 100:
            new_percent = input("Please enter a valid percentage between 0 and 100.")
        else:
            book_list[index - 1]["pages_read"] = round((float(new_percent) * float(book_list[index - 1]["pages"])) / 100) 
    except ValueError:
        print("Please enter a number.")