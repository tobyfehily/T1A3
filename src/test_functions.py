import functions
import pytest


# To run this test, enter 'python -m pytest'.
# This test checks if the check book dupes is working 
# as intended. It does this by populating a test book
# list, then running the check_book_dupes function on
# a series of arguments. The function is meant to
# return a True value if *both* the title and author 
# match the title and author of a book in the book list.
# If neither title nor author match, or if only the title
# or only the author match, the function should return a 
# False value. 

def test_check_book_dupes():
    book_list = [
    {'title': 'test_title1', 'author': 'test_author1',
     'pages': 200, 'tags': ['test_tag1', 'test_tag2'],
     'currently_reading': True, 'pages_read': 100},
    {'title': 'test_title2', 'author': 'test_author2',
     'pages': 300, 'tags': ['test_tag3', 'test_tag4'],
     'currently_reading': False, 'pages_read': 0}]
    assert functions.check_book_dupes(book_list, "test_title1", "test_author1")
    assert not functions.check_book_dupes(book_list, "test_title3", "test_author3")
    assert not functions.check_book_dupes(book_list, "test_title3", "test_author1")
    assert not functions.check_book_dupes(book_list, "test_title1", "test_author3")


# To run this test, enter 'python -m pytest'.
# This test checks if the add book function is working as
# intended. It does this by populating a test book list,
# passing a test book to the add book function and calling
# that function to append the test book to the book list,
# then checking the book list again to see if the test
# book has been added successfully. It also assesses
# whether all the passed arguments have been captured and
# whether all the default paramters have been preserved.

def test_add_books():
    book_list = [
        {'title': 'test_title1', 'author': 'test_author1',
         'pages': 200, 'tags': ['test_tag1', 'test_tag2'],
         'currently_reading': True, 'pages_read': 100},
    ]
    book_list.append(functions.add_book("test_title2", "test_author2", 300,
        ["test_tag3", "test_tag4"]))
    assert book_list == [
        {'title': 'test_title1', 'author': 'test_author1',
         'pages': 200, 'tags': ['test_tag1', 'test_tag2'],
         'currently_reading': True, 'pages_read': 100},
        {'title': 'test_title2', 'author': 'test_author2',
         'pages': 300, 'tags': ['test_tag3', 'test_tag4'],
         'currently_reading': False, 'pages_read': 0}]


