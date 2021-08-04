import os
from pymongo import MongoClient


def get_mongod_connection():
    try:
        print('Creating MongoDB connection.................................')
        CONN_STR = os.environ.get('DB_HOST')
        DATABASE_NAME = os.environ.get('db')
        client = MongoClient(CONN_STR)
        if os.environ.get('is_AUTH').upper() == 'TRUE':
            client.unificaterAuth.authenticate(os.environ.get('DB_User'), os.environ.get('DB_PWD'))
        db = client[DATABASE_NAME]
    except Exception as ex:
        print(f'Exception occurred while connection Mongo database: {ex}')
        raise Exception(ex)
    finally:
        print('MongoDB connection closed..............')
        if client: client.close()
    return db
