import os
from pymongo import MongoClient
import logging

class Connect(object):
    @staticmethod    
    def get_connection():
        mongo_URL = os.getenv("MONGO_URL")
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('mongodb logged in')
        return MongoClient(mongo_URL)