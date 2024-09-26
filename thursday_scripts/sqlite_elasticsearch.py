#!/bin/env python3

'''
Example functions for SQLite, ElasticSearch
Ensure Elasticsearch project installed first via package managers
Then create an Python VENV to install python package to:
pip install elasticsearch
'''

# Python standard library
import os
import sys
import random
import sqlite3
import datetime

# External packages
from elasticsearch import Elasticsearch # type: ignore

# Set up MySQL database
DBASE = './api/books.db'
CONNECT = sqlite3.connect(DBASE)
CONNECT.execute('CREATE TABLE IF NOT EXISTS DOWNLOADS (fpath TEXT, fname TEXT, status TEXT, date_stamp TEXT)')

# Set up Elasticsearch
ES = Elasticsearch(['http://localhost:9200'])
if not ES.ping():
    print("Something's broken with your path: 'http://localhost:9200'")
    sys.exit()


### SQLITE3 functions
def create_database_content(target_path) -> None:
    '''
    Get some data from folder of media, and populate new database
    with the name, filepath, status and time
    '''

    if not os.path.exists(target_path):
        print(f"Supplied path is not recognised: {target_path}")
        return None

    for root, _, files in os.walk(target_path):
        for file in files:
            date_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            fpath = os.path.join(root, file)
            fname = file
            status = random.choice(['Not processed', 'Complete', 'In Progress', 'Transcoding']) 
            with sqlite3.connect(DBASE) as users:
                cursor = users.cursor()
                cursor.execute("INSERT INTO DOWNLOADS (fpath,fname,status,date_stamp) VALUES (?,?,?,?)", (fpath, fname, status, date_stamp))
                users.commit()


def fetch_all() -> list:
    '''
    Retrieve all items in a database to view
    '''
    all = []
    connect = sqlite3.connect(DBASE)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM DOWNLOADS')
    for c in cursor:
        print(c)
        all.append(c)
    return all


def fetch_database_content(field, arg) -> list:
    '''
    Pull data from SQL database for test
    '''
    connect = sqlite3.connect(DBASE)
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM DOWNLOADS where {field} = {arg})")
    data = cursor.fetchall()
    print(data)
    if isinstance(data, dict):
        return list(data)
    return data


def change_status(fname, status, new_status) -> None:
    '''
    Update specific row with new
    data, for fname match
    '''
    try:
        sqlite_connection = sqlite3.connect(DBASE)
        cursor = sqlite_connection.cursor()

        # Update row with new status
        sql_query = '''UPDATE DOWNLOADS SET status = ? WHERE fname = ? AND status = ?'''
        data = (new_status, fname, status)
        cursor.execute(sql_query, data)
        sqlite_connection.commit()
        print(f"Record updated with new status {new_status}")
        cursor.close()
    except sqlite3.Error as err:
        print(err)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


### Elasticsearch functions
def create_index() -> None:
    '''
    Create the new elasticsearch index
    and define how data is mapped
    '''
    index_name = 'file_metadata'
    mapping = {
        'properties': {
            'filepath': {'type': 'keyword'},
            'name': {'type': 'keyword'},
            'status': {'type': 'keyword'},
            'timestamp': {'type': 'date'}
        }
    }

    if not ES.indices.exists(index=index_name):
        ES.indices.create(index=index_name, body={'mappings': mapping})
        print(f"Index '{index_name}' created.")
    else:
        print(f"Index '{index_name}' already exists.")


def populate_elasticsearch(target_path) -> None:
    '''
    Populate elasticsearch with data
    '''
    if not os.path.exists(target_path):
        print(f"Supplied path is not recognised: {target_path}")
        return None

    for root, _, files in os.walk(target_path):
        for file in files:
            date_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            fpath = os.path.join(root, file)
            fname = file
            status = random.choice(['Not processed', 'Complete', 'In Progress', 'Transcoding']) 

            ES.index(index='file_metadata', document={
                "filepath": fpath,
                "name": fname,
                "status": status,
                "timestamp": date_stamp
            })


def search_status(status) -> list:
    '''
    Search for specifics within the index
    '''
    requested_data = []
    search_results = ES.search(index='file_metadata', query={'term': {'status': {'value': status}}}, size=200)
    for row in search_results['hits']['hits']:
        get_id = [row['_id']]
        record = [(value) for _, value in row['_source'].items()]
        all_items = tuple(record) + tuple(get_id)
        requested_data.append(all_items)
    return requested_data


def update_status(fname, status, new_status) -> None:
    '''
    Match all statuses, and where fname matches
    update status with new status
    '''
    update_request = {
        "properties": {
            "status": new_status
        }
    }
    search = ES.search(index='file_metadata', query={'term': {'status': {'value': status}}}, size=100)
    data = search['hits']['hits']
    print(f"Matches found:\n{data}")

    data = [x for x in data if fname in str(x)]
    if len(data) == 0:
        print(f"No match found: {fname}, {status}")
        return None

    id = data[0]['_id']
    index = ES.update(index='file_metadata', id=f"{id}", body=update_request)
    if index['result'] == 'udpated':
        print(f"Record updated for row {data[0]}")
        
