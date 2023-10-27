import random
import emoji


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
            if new_pages <= 0:
                print("Number must be more than zero.")
                continue
            return new_pages
        except ValueError:
            print("Please enter a number.")


def add_tags():
    new_tags = input(
        "Enter tags separated by a comma, or press Enter to skip: ")
    if new_tags == '':
        return new_tags
    else:
        return set([x.strip() for x in new_tags.split(',')])


def add_book(
        new_title,
        new_author,
        new_pages,
        new_tags=[],
        currently_reading=False,
        pages_read=0):
    new_book = dict(
        title=new_title,
        author=new_author,
        pages=new_pages,
        tags=new_tags,
        currently_reading=currently_reading,
        pages_read=pages_read)
    print(emoji.emojize(
        f":open_book: {new_title} by :writing_hand:  {new_author} has been added."))
    return new_book


def continue_prompt(prompt):
    continue_prompt = input(f"Would you like to {prompt} (y/n)?: ").lower()
    while continue_prompt not in ["y", "n"]:
        continue_prompt = input(
            f"Please enter 'y' to {prompt} or 'n' to stop: ").lower()
    else:
        if continue_prompt == 'n':
            return False
        else:
            return True


def percentage(portion, whole):
    try:
        return round((portion / whole) * 100)
    except ZeroDivisionError:
        print("Cannot divide by zero.")


def reverse_percentage(portion, whole):
    try:
        return round((portion * whole) / 100)
    except ZeroDivisionError:
        print("Cannot divide by zero.")


def get_book_list(list):
    for i, book in enumerate(list):
        print(emoji.emojize(f"[{i + 1}] :open_book: {book['title']} | :writing_hand:  {book['author']} | :page_facing_up: {book['pages']} pages total | :check_mark_button: {book['pages_read']} pages / {percentage((book['pages_read']), (book['pages']))} percent read{' | :thumbs_up: now reading' if book['currently_reading'] else ''}"))
        for i in book['tags']:
            print(emoji.emojize(f"    :label:  {i}"))


def select_book(book_list, prompt):
    while True:
        book_selection = input(
            f"Enter the number of the book to {prompt}, or press Enter to cancel: ")
        if book_selection == "":
            return book_selection
        else:
            try:
                book_selection = int(book_selection)
                if book_selection <= 0:
                    print("Must be more than zero.")
                    continue
                book_list[book_selection - 1]
                return book_selection
            except IndexError:
                print("Out of range.")
            except ValueError:
                print("You did not enter a number.")


def get_tags(book_list):
    tag_list = list(set(x for tags in book_list for x in tags['tags']))
    print("Current tags:\n")
    for tags in tag_list:
        print(emoji.emojize(f":label:  {tags}"))


def select_tags(book_list):
    tag_book_list = []
    while True:
        tag = input("\nType a tag, or press Enter to cancel: ").lower()
        if tag == "":
            return tag
        else:
            for book in book_list:
                if tag in book['tags']:
                    tag_book_list.append(book)
            if tag_book_list == []:
                print("No matching books.")
                continue
            else:
                get_book_list(tag_book_list)
                break


def set_current_book(old_book_list, index):
    if old_book_list[index - 1]["currently_reading"]:
        print(emoji.emojize(
            f"You're already reading :open_book: {old_book_list[index - 1]['title']} by :writing_hand:  {old_book_list[index - 1]['author']}!"))
    else:
        old_book_list[index - 1]["currently_reading"] = True
        print(emoji.emojize(
            f"Enjoy reading :open_book: {old_book_list[index - 1]['title']} by :writing_hand:  {old_book_list[index - 1]['author']}!"))
        global book_list
        book_list = old_book_list


def set_book_progress(book_list, index):
    while True:
        try:
            update_value = int(input("Enter current pages or percent: "))
            while True:
                pages_or_percent = input(
                    "Enter 'pages' to update by pages or 'percent' to update by percent: ").lower()
                match pages_or_percent:
                    case "pages":
                        set_book_pages(book_list, index, update_value)
                        break
                    case "percent":
                        set_book_percent(book_list, index, update_value)
                        break
                    case _:
                        print("Invalid input. Type 'pages' or 'percent': ")
                        continue
            break
        except ValueError:
            print("You did not enter a number")


def set_book_pages(book_list, index, new_pages):
    while True:
        if new_pages > book_list[index - 1]["pages"]:
            print(emoji.emojize(
                f":open_book: {book_list[index - 1]['title']} by :writing_hand:  {book_list[index - 1]['author']} is only {book_list[index - 1]['pages']} pages long."))
            break
        elif new_pages == book_list[index - 1]["pages"]:
            delete_book(book_list, index)
            break
        else:
            print(emoji.emojize(
                f"Only :open_book: {book_list[index - 1]['pages'] - new_pages} pages to go!"))
            book_list[index - 1]['pages_read'] = new_pages
            break


def set_book_percent(book_list, index, new_percent):
    while True:
        while new_percent < 0 or new_percent > 100:
            new_percent = int(
                input("Please enter a valid percentage between 0 and 100: "))
        else:
            if new_percent == 100:
                delete_book(book_list, index)
                break
            else:
                book_list[index - 1]["pages_read"] = reverse_percentage(
                    new_percent, book_list[index - 1]["pages"])
                print(emoji.emojize(
                    f"Only :open_book: {book_list[index - 1]['pages'] - book_list[index - 1]['pages_read']} pages to go!"))
                break


def get_random_book(book_list):
    random_book = random.choice(book_list)
    print(emoji.emojize(
        f"Why not read :open_book: {random_book['title']} by :writing_hand:  {random_book['author']}?"))


def check_empty_book_list(book_list):
    if book_list == []:
        cancel_prompt = input(
            "No books found. Press Enter to return to menu: ")
        return True
