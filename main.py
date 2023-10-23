import functions

while True:
    new_title = input("Enter book title: ").lower()
    new_author = input("Enter author: ").lower()
    if functions.check_book_dupes(new_title, new_author):
        print(f"You have already added '{new_title}' by {new_author}.")
        continue
    else:
        while True:
            try:
                new_pages = int(input("Enter book pages: "))
                break
            except ValueError:
                print("Please enter a number.")      
        functions.add_book(new_title, new_author, new_pages)
    continue_prompt = input("Would you like to add another book (y/n)?: ").lower()
    while continue_prompt not in ["y", "n"]:
        continue_prompt = input("Please enter 'y' to continue adding books or 'n' to stop: ").lower()
    else:
        if continue_prompt == 'n':
            break
        else:
            continue

functions.get_book_list()
functions.get_random_book()