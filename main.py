import functions, sys, csv, json

book_list = [
    {'title': 'doppelganger', 'author': 'naomi klein', 'pages': 416, 'tags': ['non-fiction'], 'currently_reading': True, 'pages_read': 0},
    {'title': 'i, claudius', 'author': 'robert graves', 'pages': 468, 'tags': ['non-fiction', 'ancient rome'], 'currently_reading': True, 'pages_read': 0}, 
    {'title': 'python for dummies', 'author': 'stef maruch', 'pages': 432, 'tags': ['non-fiction', 'python'], 'currently_reading': False, 'pages_read': 0},
    {'title': 'short book', 'author': 'test author', 'pages': 100, 'tags': ['non-fiction', 'python'], 'currently_reading': False, 'pages_read': 0},
    {'title': 'long book', 'author': 'test author', 'pages': 600, 'tags': ['non-fiction', 'python'], 'currently_reading': False, 'pages_read': 0},
    ]

while True:
    menu_choice = input(("""\nWelcome! Select an option from below:\n
    1. Add book
    2. Remove book
    3. Mark book as currently reading
    4. Update book progress
    5. List currently reading books
    6. List to be read books
    7. List books by tag                     
    8. Pick a random to be read book\n
    0. Save books and quit\n\n"""))
    try:
        match int(menu_choice):
            case 1:
                while True:
                    while True:
                        new_title = input("Enter book title: ").lower()
                        if new_title != "":
                            break
                        else:
                            print("You need to enter a book title.")
                    while True:
                        new_author = input("Enter author: ").lower()
                        if new_author != "":
                            break
                        else:
                            print("You need to enter an author.")
                    if functions.check_book_dupes(new_title, new_author, book_list):
                        print(functions.emoji.emojize(f"You have already added :open_book: '{new_title}' by :writing_hand:  {new_author}."))
                        continue
                    else:
                        while True:
                            try:
                                new_pages = int(input("Enter book pages: "))
                                break
                            except ValueError:
                                print("Please enter a number.")      
                    new_tags = input("Enter tags separated by a comma, or press Enter to skip: ")
                    unique_new_tags = set([x.strip() for x in new_tags.split(',')])
                    if new_tags == '':
                        unique_new_tags = new_tags
                    functions.add_book(book_list, new_title, new_author, new_pages, unique_new_tags)
                    continue_prompt = input("Would you like to add another book (y/n)?: ").lower()
                    while continue_prompt not in ["y", "n"]:
                        continue_prompt = input("Please enter 'y' to continue adding books or 'n' to stop: ").lower()
                    else:
                        if continue_prompt == 'n':
                            break
                        else:
                            continue
            case 2:
                while True:
                    functions.get_book_list(book_list)
                    try:
                        book_choice = int(input("Enter the number of the book to delete, or enter 0 to quit: ")) 
                        if book_choice == 0:
                            break
                        elif book_choice < 0:
                            print("Must be a positive integer.")
                        else:
                            functions.delete_book(book_list, book_choice)
                    except ValueError:
                        print("You did not enter a number.")
            case 3:
                while True:
                    functions.get_book_list(book_list)
                    try:
                        book_choice = int(input("Enter the number of the book to mark as currently reading, or enter 0 to quit: ")) 
                        if book_choice == 0:
                            break
                        elif book_choice < 0:
                            print("Must be a positive integer.")
                        else:
                            functions.set_current_book(book_list, book_choice)
                    except ValueError:
                        print("You did not enter a number.")
            case 4:
                while True:
                    functions.get_book_list(book_list)
                    try:
                        book_choice = int(input("Enter the number of the book to update, or enter 0 to quit: ")) 
                        if book_choice == 0:
                            break
                        elif book_choice < 0:
                            print("Must be a positive integer.")
                        else:
                            while True:
                                try:
                                    update_value = int(input("Enter the current page or percent: "))
                                    while True:
                                        pages_or_percent = input("Enter 'pages' to update by pages or 'percent' to update by percent: ").lower()
                                        match pages_or_percent:
                                            case "pages":
                                                    functions.set_book_pages(book_list, book_choice, update_value)
                                                    break
                                            case "percent":
                                                    functions.set_book_percent(book_list, book_choice, update_value)
                                                    break
                                            case _:
                                                print("Invalid input")
                                    break
                                except ValueError:
                                    print("You did not enter a number")
                    except ValueError:
                        print("You did not enter a number.")
            case 5:
                functions.get_sorted_book_list(book_list, "currently reading")
            case 6:
                functions.get_sorted_book_list(book_list, "to be read")
            case 7:
                functions.get_tags(book_list)
                tag_choice = input("Choose a tag, or press Enter to cancel: ").lower()
                if tag_choice != '':
                    functions.get_tag_book_list(tag_choice)
                    quit_prompt = input("Press any key to exit")
            case 8:
                functions.get_random_book(book_list)
                quit_prompt = input("Press any key to exit")
            case 0:
                with open('book_list.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames=book_list[0].keys())
                    writer.writeheader()
                    writer.writerows(book_list)
                with open('book_list.txt', 'w') as f:
                    for books in book_list:
                        for key, value in books.items():
                            f.write(f'{key}: {value}\n')
                        f.write("\n")
                sys.exit("Thanks for visiting! Happy reading.")
            case _:
                print("Invalid input.")
    except ValueError:
        print("Invalid input.")
