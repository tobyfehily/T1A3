import functions
import pytest


# This test checks if the add book function is working as
# intended. It does so by populating a test book list,
# passing a test book to the add book function and then
# checking the book list again to see if the new test
# book has been added successfully. It also assesses
# whether all the passed arguments have been captured and
# whether all the default paramters have been preserved,
# while ensuring the function's updated local book list
# values have been applied globally.

def test_add_book():
    book_list = [
        {'title': 'test_title1', 'author': 'test_author1',
         'pages': 200, 'tags': ['test_tag1', 'test_tag2'],
         'currently_reading': True, 'pages_read': 100}]
    functions.add_book(
        book_list, "test_title2", "test_author2", 300, [
            "test_tag3", "test_tag4"])
    assert book_list == [
        {'title': 'test_title1', 'author': 'test_author1',
         'pages': 200, 'tags': ['test_tag1', 'test_tag2'],
         'currently_reading': True, 'pages_read': 100},
        {'title': 'test_title2', 'author': 'test_author2',
         'pages': 300, 'tags': ['test_tag3', 'test_tag4'],
         'currently_reading': False, 'pages_read': 0},
    ]

# This test checks if the set book percent function is
# working as intended. Because this function calls the
# reverse percentage and delete book functions, it checks
# those functions too. It populates a test book list with
# test pages and pages read values. The first subtest sets
# the book percent to 75%, then assesses whether the pages
# read value has been updated accordingly. Similarly, the
# second subtest sets the book percent to 0%, then assesses
# whether the pages read value has been updated accordingly.
# The third subtest sets the book percent to 100%, which is
# meant to call the delete book function, so it checks
# whether the test book has been removed from the test book
# list.


def test_set_book_percent():
    book_list = [
        {'title': 'test_title1', 'author': 'test_author1',
         'pages': 200, 'tags': ['test_tag1', 'test_tag2'],
         'currently_reading': True, 'pages_read': 100}]
    functions.set_book_percent(book_list, 1, 75)
    assert (book_list[0]['pages_read']) == 150
    functions.set_book_percent(book_list, 1, 0)
    assert (book_list[0]['pages_read']) == 0
    functions.set_book_percent(book_list, 1, 100)
    assert len(book_list) == 0
