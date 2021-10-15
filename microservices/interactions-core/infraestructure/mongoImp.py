import os
from pymongo import MongoClient
import logging
import pymongo
from bson.json_util import dumps
import json
from typing import Any, Iterable
from domain.helpers.tracing import _tracer

class MongoImplementation(object):

    def __init__(self) -> None:
        logging.basicConfig(
            format='%(asctime)s - %(message)s', level=logging.INFO)
        super().__init__()
        self.client = self.get_connection()

    @staticmethod
    def get_connection() -> MongoClient:
        trace = _tracer.start_span("connection", tags={"type":"mongodb"})
        mongo_URL = os.getenv("MONGO_URL")
        client = MongoClient(mongo_URL)
        logging.info(' * Mongodb logged in')
        trace.finish()
        return client

    def find_last_iot_registers(self, collection_name: str, sorting_field: str) -> Iterable:
        trace = _tracer.start_span("get devices", tags={"type":"mongodb"})
        db = self.client[collection_name]
        cursor = db.photo_resistence.find({}).sort(
            sorting_field, pymongo.DESCENDING).limit(50)
        trace.finish()
        return json.loads(dumps(cursor))

    def insert_document(self, database: str, collection_name: str, obj_to_insert: object) -> Any:
        trace = _tracer.start_span("insert document", tags={"type":"mongodb"})
        db = self.client[database]
        cursor = db[collection_name].insert_one(
            obj_to_insert)
        trace.finish()
        return cursor.inserted_id.__str__()


if __name__ == "__main__":
    mongo = MongoImplementation()
    documents = mongo.find_last_iot_registers("iot_devices", "created_at")
