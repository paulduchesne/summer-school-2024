#!/bin/env python3

'''
Example functions for building and running FFmpeg commands
'''

import json
import requests

URL = "http://127.0.0.1:5000/api/v1/resources/books"


def get_books() -> dict:
    '''
    Use requests to call all books
    from books.db
    '''
    try:
        books_all = requests.get(f"{URL}/all", verify=False)
        book_data = json.loads(books_all.text)
        return book_data
    except Exception as err:
        print(err)


def get_specific_book(key, arg) -> dict:
    '''
    Use requests to retrieve specific book
    from books.db
    '''
    query = {
        key: arg
    }

    try:
        book = requests.get(URL, params=query, verify=False)
        book_dct = json.loads(book.text)
        return book_dct
    except Exception as err:
        print(err)

