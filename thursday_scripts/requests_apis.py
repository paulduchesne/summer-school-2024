#!/bin/env python3

'''
To be used with script './api/launch_api.py'
Example functions for querying, writing to and
deleting from our test book database
'''

import json
import requests

URL = "http://127.0.0.1:5000/api/v1/resources/books"
HEADERS = {'Content-Type': 'application/json'}


def get_books() -> list:
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


def get_specific_book(key, arg) -> list:
    '''
    Use requests to retrieve specific book
    from books.db
    key = title/author/published
    arg = matching value for key
    '''
    query = {
        key: arg
    }

    try:
        book = requests.get(URL, params=query, verify=False)
        book_dct = json.loads(book.text)
        if isinstance(book_dct, dict):
            return list(book_dct)
        return book_dct
    except Exception as err:
        print(err)


def post_new_book(query) -> dict:
    '''
    Post your book to the base with sample query:
    data = {
        "author": "Ursula K. Le Guin",
        "title": "The Left Hand of Darkness",
        "first_sentence": "I'll make my report as if I told a story, for I was taught as a child on my homeworld that Truth is a matter of the imagination.",
        "published": 1969
    }
    '''

    try:
        response = requests.post(URL, headers=HEADERS, data=json.dumps(query))
        print(response.json())
    except Exception as err:
        print(err)


def delete_book(query) -> dict:
    '''
    Requests function to delete a book entry
    data = {
        "title": "The Left Hand of Darkness",
        "author": "Ursula K. Le Guin"
    }
    '''

    response = requests.delete(URL, headers=HEADERS, data=json.dumps(query))
    print(response.json())
