import functions
import pytest


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
