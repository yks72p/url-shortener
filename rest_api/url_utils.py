import base64
from flask import current_app
from rest_api import db

INSTANCE_ID_MASK = 255
INSTANCE_ID_NUM_BITS = 8

cache = {}

def get_a_new_id():
    instance_id = current_app.config['INSTANCE_ID']
    current_id = cache.get("id", db.get_current_id(instance_id)) + 1
    cache["id"] = current_id

    db.upsert_current_id(instance_id, current_id)
    return concatenate_instance(instance_id, current_id)


def concatenate_instance(instance_id: int, current_id: int):
    return (instance_id & INSTANCE_ID_MASK) + (current_id << INSTANCE_ID_NUM_BITS)


def encode_short_id(short_id: int):
    short_id_as_byte_array = short_id.to_bytes((short_id.bit_length() + 7) // 8, byteorder='little')
    return base64.b64encode(short_id_as_byte_array).decode("utf-8")


def decode_short_id(short_id_encoded: str):
    return int.from_bytes(base64.b64decode(short_id_encoded.encode("utf-8")), 'little')
