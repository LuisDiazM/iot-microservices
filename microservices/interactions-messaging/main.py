import datetime
import json
import logging
import os
from pynats import NATSClient
from pynats.client import NATSMessage
from infraestructure import mongoImp

nats_URL = os.getenv("nats_URL")
subject_id = os.getenv("subject_id")

global mongo_client

with NATSClient(url=nats_URL) as client:
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # Connect
    client.connect()
    logging.info('NATS logged in')
    mongo_client = mongoImp.Connect.get_connection()
    # Subscribe

    def callback(msg: NATSMessage):
        try:
            payload = json.loads(msg.payload)
            logging.info(payload.__str__())
            localDateTime = datetime.datetime.now()
            payload.update(
                {"created_at": localDateTime, "device": msg.subject})
            db = mongo_client.iot_devices
            db.photo_resistence.insert_one(payload)
        except ValueError:
            logging.warning("payload not valid")

    client.subscribe(subject=subject_id, callback=callback)

    # wait for 1 message
    client.wait()
