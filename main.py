import functions, sys, csv

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
    5. List all books
    6. List books by tag                     
    7. Pick a random to be read book\n
    0. Save books and quit\n\n"""))
    try:
        match int(menu_choice):
            case 1:
                while True:
                    new_title = functions.add_book_info("book title")
                    new_author = functions.add_book_info("author")
                    if functions.check_book_dupes(book_list, new_title, new_author):
                        print(functions.emoji.emojize(f"You have already added :open_book: '{new_title}' by :writing_hand:  {new_author}."))
                        continue        
                    else:
                        functions.add_book(book_list, new_title, new_author, functions.add_pages(), functions.add_tags())
                        if functions.continue_prompt("add another book"):
                            continue
                        else:
                            break
            case 2:
                while True:
                    functions.get_book_list(book_list)
                    book_selection = functions.select_book(book_list, "delete")
                    if book_selection == '':
                        break
                    else:
                        functions.delete_book(book_list, book_selection)
                        if functions.continue_prompt("remove another book"):
                            continue
                        else:
                            break
            case 3:
                while True:
                    functions.get_book_list(book_list)
                    book_selection = functions.select_book(book_list, "mark as reading")
                    if book_selection == '':
                        break
                    else:
                        functions.set_current_book(book_list, book_selection)
                        if functions.continue_prompt("mark another book as reading"):
                                continue
                        else:
                            break
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
                functions.get_book_list(book_list)
                quit_prompt = input("Press any key to exit")            
            case 6:
                while True:
                    functions.get_tags(book_list)
                    tag_selection = functions.select_tags(book_list)
                    if tag_selection == '':
                        break
                    else:
                        if functions.continue_prompt("get more books by tag"):
                                continue
                        else:
                            break
            case 7:
                while True:
                    functions.get_random_book(book_list)
                    if functions.continue_prompt("get another random book"):
                        continue
                    else:
                        break
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
