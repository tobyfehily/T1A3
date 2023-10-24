import random, emoji

book_list = [
    {'title': 'Doppelganger', 'author': 'Naomi Klein', 'pages': 416, 'tags': ['non-fiction'], 'currently_reading': True, 'pages_read': 0},
    {'title': 'I, Claudius', 'author': 'Robert Graves', 'pages': 468, 'tags': ['non-fiction', 'ancient rome'], 'currently_reading': True, 'pages_read': 0}, 
    {'title': 'Python for Dummies', 'author': 'Stef Maruch', 'pages': 432, 'tags': ['non-fiction', 'python'], 'currently_reading': False, 'pages_read': 0},
    {'title': 'Short book', 'author': 'Short author', 'pages': 100, 'tags': ['non-fiction', 'python'], 'currently_reading': False, 'pages_read': 0},
    {'title': 'Long book', 'author': 'Long author', 'pages': 600, 'tags': ['non-fiction', 'python'], 'currently_reading': False, 'pages_read': 0},
    ]

def add_book(new_title, new_author, new_pages, new_tags = [], currently_reading = False, pages_read = 0):
    new_book = dict(title = new_title, author = new_author, pages = new_pages, tags = new_tags, currently_reading = currently_reading, pages_read = pages_read)
    book_list.append(new_book)
    print(emoji.emojize(f":open_book: {new_title} by :writing_hand:  {new_author} has been added."))

def check_book_dupes(new_title, new_author):
    for book in book_list:
        if book['title'] == new_title and book['author'] == new_author:
            return True
    return False

def get_tags(tags_list):
    unique_tags = []
    for i in tags_list:
        unique_tags.extend(i['tags'])
    print("Current tags:")
    for i in set(unique_tags):
        print(emoji.emojize(f":label:  {i}"))

def get_book_list(list):
    for i, book in enumerate(list):
        print(emoji.emojize(f"[{i + 1}] :open_book: {book['title']} | :writing_hand:  {book['author']} | :page_facing_up: {book['pages']}"))
        for i in book['tags']:
            print(emoji.emojize(f"    :label:  {i}"))

def get_sorted_book_list(sorting_choice):
    currently_reading_book_list = []
    to_be_read_book_list = []
    for book in book_list:
        if book['currently_reading']:
            currently_reading_book_list.append(book)
        else:
            to_be_read_book_list.append(book)
    match sorting_choice:
        case "currently reading":
            get_book_list(currently_reading_book_list)
        case "to be read":
            get_book_list(to_be_read_book_list)

def get_tag_book_list(tag):
    tag_book_list = []
    for book in book_list:
        if tag in book['tags']:
            tag_book_list.append(book)
    if tag_book_list == []:
        print("No matching books")
    else:
        get_book_list(tag_book_list)

def get_random_book():
    to_be_read_book_list = []
    for book in book_list:
        if not book['currently_reading']:
            to_be_read_book_list.append(book)
    random_book = random.choice(to_be_read_book_list)
    print(emoji.emojize(f"Why not try :open_book: {random_book['title']} by :writing_hand:  {random_book['author']}?"))

def delete_book(index):
    try:
        print(emoji.emojize(f":open_book: {book_list[index - 1]['title']} by :writing_hand:  {book_list[index - 1]['author']} has been deleted."))
        del book_list[index - 1]
    except IndexError:
        print("Selection out of range")

def set_current_book(index):
    try:
        if book_list[index -1]["currently_reading"]:
            print(emoji.emojize(f"You're already reading :open_book: {book_list[index - 1]['title']} by :writing_hand:  {book_list[index - 1]['author']}"))
        else:
            book_list[index -1]["currently_reading"] == True
            print(emoji.emojize(f"Enjoy reading :open_book: {book_list[index - 1]['title']} by :writing_hand: {book_list[index - 1]['author']}!"))
    except IndexError:
        print("Selection out of range")

def set_book_pages(index, new_pages):
    try:
        if new_pages > book_list[index - 1]["pages"]:
            print(emoji.emojize(f":open_book: {book_list[index - 1]['title']} by :writing_hand:  {book_list[index - 1]['author']} is only {book_list[index - 1]['pages']} pages long."))
        elif new_pages == book_list[index - 1]["pages"]:
            print("You're all finished!")
            delete_book(index)
        else:
            book_list[index - 1]['pages_read'] = new_pages
            print(emoji.emojize(f"Only :page_facing_up: {book_list[index - 1]['pages'] - book_list[index - 1]['pages_read']} pages to go!"))
    except ValueError:
        print("Please enter a number.")

def set_book_percent(index, new_percent):
    try:
        while new_percent < 0 or new_percent > 100:
            new_percent = int(input("Please enter a valid percentage between 0 and 100: "))
        else:
            book_list[index - 1]["pages_read"] = round((float(new_percent) * float(book_list[index - 1]["pages"])) / 100) 
            if book_list[index - 1]["pages"] == book_list[index - 1]["pages_read"]:
                print("You're all finished!")
                delete_book(index)
            else:
                print(emoji.emojize(f"Only :page_facing_up: {book_list[index - 1]['pages'] - book_list[index - 1]['pages_read']} pages to go!"))
    except (ValueError):
        print("Please enter a number.")
    