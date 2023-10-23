book_list = [{'title': 'title', 'author': 'author'}, {'title': 'title2', 'author': 'author2'}]

def add_book(title, author):
    new_book = dict(title = title, author = author)
    book_list.append(new_book)

def remove_book(index):
    del book_list[index - 1]

def list_books():
    for i, book in enumerate(book_list):
        print(f"{i + 1}: '{book['title']}' by {book['author']}")



new_title = input("Enter book title: ").lower()
new_author = input("Enter author: ").lower()
for book in book_list:
    if book['title'] == new_title and book['author'] == new_author:
        print(f"You have already added '{new_title}' by {new_author}.")

add_book(new_title, new_author)

print(book_list)

list_books()

remove_book(3)

list_books()