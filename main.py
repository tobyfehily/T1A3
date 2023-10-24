import functions
import sys
import csv
import json

try:
    with open('book_list.json') as f:
        book_list = json.load(f)
except json.JSONDecodeError:
    book_list = []

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
                    if functions.check_book_dupes(
                            book_list, new_title, new_author):
                        print(functions.emoji.emojize(
                            f"You have already added :open_book: '{new_title}' by :writing_hand:  {new_author}."))
                        continue
                    else:
                        functions.add_book(
                            book_list,
                            new_title,
                            new_author,
                            functions.add_pages(),
                            functions.add_tags())
                        if functions.continue_prompt("add another book"):
                            continue
                        else:
                            break
            case 2:
                while True:
                    if functions.check_empty_book_list(book_list):
                        break
                    else:
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
                    if functions.check_empty_book_list(book_list):
                        break
                    else:
                        functions.get_book_list(book_list)
                        book_selection = functions.select_book(
                        book_list, "mark as reading")
                        if book_selection == '':
                            break
                        else:
                            functions.set_current_book(book_list, book_selection)
                            if functions.continue_prompt(
                                    "mark another book as reading"):
                                continue
                            else:
                                break
            case 4:
                while True:
                    if functions.check_empty_book_list(book_list):
                        break
                    else:
                        functions.get_book_list(book_list)
                        book_selection = functions.select_book(book_list, "update")
                        if book_selection == '':
                            break
                        else:
                            functions.set_book_progress(book_list, book_selection)
                            if functions.continue_prompt("update another book"):
                                continue
                            else:
                                break
            case 5:
                while True:
                    if functions.check_empty_book_list(book_list):
                            break
                    else:
                        functions.get_book_list(book_list)
                        quit_prompt = input("Press any key to exit")
            case 6:
                while True:
                    if functions.check_empty_book_list(book_list):
                        break
                    else:
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
                    if functions.check_empty_book_list(book_list):
                        break
                    else:
                        functions.get_random_book(book_list)                    
                        if functions.continue_prompt("get another random book"):
                            continue
                        else:
                            break
            case 0:
                try:
                    with open('book_list.csv', 'w') as f:
                        writer = csv.DictWriter(f, fieldnames=book_list[0].keys())
                        writer.writeheader()
                        writer.writerows(book_list)
                    with open('book_list.txt', 'w') as f:
                        for books in book_list:
                            for key, value in books.items():
                                f.write(f'{key}: {value}\n')
                            f.write("\n")
                    with open('book_list.json', 'w') as f:
                        json.dump(book_list, f, indent=2)
                except IndexError:
                    print("No books found, so no books saved.")
                sys.exit("Thanks for visiting! Happy reading.")
    except ValueError:
        print("Invalid input.")
