import random, emoji

def add_book_info(prompt):
    while True:
        info = input(f"Enter your {prompt}: ").lower()
        if info != "":
            return info
        else:
            print(f"You need to enter your {prompt}.")

def check_book_dupes(book_list, new_title, new_author):
    for book in book_list:
        if book['title'] == new_title and book['author'] == new_author:
            return True
    return False

def add_pages():
    while True:
        try:
            new_pages = int(input("Enter book pages: "))
            return new_pages
        except ValueError:
            print("Please enter a number.")

def add_tags():
    new_tags = input("Enter tags separated by a comma, or press Enter to skip: ")
    unique_new_tags = set([x.strip() for x in new_tags.split(',')])
    if new_tags == '':
        return new_tags
    return unique_new_tags

def add_book(old_book_list, new_title, new_author, new_pages, new_tags = [], currently_reading = False, pages_read = 0):
    new_book = dict(title = new_title, author = new_author, pages = new_pages, tags = new_tags, currently_reading = currently_reading, pages_read = pages_read)
    global book_list
    book_list = old_book_list.append(new_book)
    print(emoji.emojize(f":open_book: {new_title} by :writing_hand:  {new_author} has been added."))

def continue_prompt(prompt):
    continue_prompt = input(f"Would you like to {prompt} another book (y/n)?: ").lower()
    while continue_prompt not in ["y", "n"]:
        continue_prompt = input(f"Please enter 'y' to {prompt} another books or 'n' to stop: ").lower()
    else:
        if continue_prompt == 'n':
            return False
        else:
            return True

def percentage(portion, whole):
    return round((float(portion) / float(whole)) * 100)

def get_book_list(list):
    for i, book in enumerate(list):
        print(emoji.emojize(f"[{i + 1}] :open_book: {book['title']} | :writing_hand:  {book['author']} | :page_facing_up: {book['pages']} pages total | :check_mark_button: {book['pages_read']} pages / {percentage((book['pages_read']), (book['pages']))} percent read{' | :thumbs_up: now reading' if book['currently_reading'] else ''}"))
        for i in book['tags']:
            print(emoji.emojize(f"    :label:  {i}"))

def select_book(book_list, prompt):
    while True:
        book_selection = input(prompt)
        if book_selection == "":
            return book_selection
        else:
            try:
                book_selection = int(book_selection)
                if int(book_selection) <= 0:
                    print("Must be a positive integer.")
                elif int(book_selection) > len(book_list):
                    print("Out of range.")
                else:
                    return book_selection
            except ValueError:
                print("You did not enter a number.")

def delete_book(book_list, index):
    print(emoji.emojize(f":open_book: {book_list[index - 1]['title']} by :writing_hand:  {book_list[index - 1]['author']} has been deleted."))
    del book_list[index - 1]

def get_sorted_book_list(book_list, sorting_choice):
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
    quit_prompt = input("Press any key to exit")

def get_tags(book_list):
    unique_tags = []
    for i in book_list:
        unique_tags.extend(i['tags'])
    print("Current tags:")
    for i in set(unique_tags):
        print(emoji.emojize(f":label:  {i}"))


def get_tag_book_list(book_list, tag):
    tag_book_list = []
    while True:
        for book in book_list:
            if tag in book['tags']:
                tag_book_list.append(book)
        if tag_book_list == []:
            tag = input("No matching books. Enter a different tag, or press Enter to cancel: ")
            if tag != '':
                continue
            else:    
                break
        else:
            get_book_list(tag_book_list)
            break

def get_random_book(book_list):
    to_be_read_book_list = []
    for book in book_list:
        if not book['currently_reading']:
            to_be_read_book_list.append(book)
    random_book = random.choice(to_be_read_book_list)
    print(emoji.emojize(f"Why not try :open_book: {random_book['title']} by :writing_hand:  {random_book['author']}?"))



def set_current_book(old_book_list, index):
    try:
        if old_book_list[index -1]["currently_reading"]:
            print(emoji.emojize(f"You're already reading :open_book: {old_book_list[index - 1]['title']} by :writing_hand:  {old_book_list[index - 1]['author']}"))
            quit_prompt = input("Press any key to exit")
        else:
            old_book_list[index -1]["currently_reading"] = True
            print(emoji.emojize(f"Enjoy reading :open_book: {old_book_list[index - 1]['title']} by :writing_hand:  {old_book_list[index - 1]['author']}!"))
            global book_list
            book_list = old_book_list
            quit_prompt = input("Press any key to exit")
    except IndexError:
        print("Selection out of range")

def set_book_pages(book_list, index, new_pages):
    try:
        if new_pages > book_list[index - 1]["pages"]:
            print(emoji.emojize(f":open_book: {book_list[index - 1]['title']} by :writing_hand:  {book_list[index - 1]['author']} is only {book_list[index - 1]['pages']} pages long."))
            quit_prompt = input("Press any key to exit")
        elif new_pages == book_list[index - 1]["pages"]:
            print(emoji.emojize(":party_popper: You're all finished!"))
            delete_book(book_list, index)
        else:
            book_list[index - 1]['pages_read'] = new_pages
    except ValueError:
        print("Please enter a number.")

def set_book_percent(book_list, index, new_percent):
    try:
        while new_percent < 0 or new_percent > 100:
            new_percent = int(input("Please enter a valid percentage between 0 and 100: "))
        else:
            book_list[index - 1]["pages_read"] = round((float(new_percent) * float(book_list[index - 1]["pages"])) / 100) 
            if book_list[index - 1]["pages"] == book_list[index - 1]["pages_read"]:
                print(emoji.emojize(":party_popper: You're all finished!"))
                delete_book(book_list, index)
    except (ValueError):
        print("Please enter a number.")
