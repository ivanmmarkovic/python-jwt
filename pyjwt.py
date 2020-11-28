
import hmac
import hashlib
import binascii
import base64

import json

from datetime import datetime

key = "E49756B4C8FAB4E48222A3E7F3B97CC3"
byte_key = binascii.unhexlify(key)


# creates dictionary object
def create_jwt(exp: int = 60 * 60 * 1000) -> dict:
    return {
        "header": {
            "alg": "HS256",
            "typ": "JWT"
        },
        "payload": {
            "exp": datetime.now().timestamp() + exp
        }
    }


def add_expiration_time(jwt: dict, interval_milliseconds: int = 60 * 60 * 1000):
    jwt["payload"]["exp"] = datetime.now().timestamp() + interval_milliseconds


def add_claim(jwt: dict, claim, value):
    jwt["payload"][claim] = value


# use this to encode header and payload
def encode_jwt_part(jwt_part: dict) -> bytes:
    jwt_part_string: str = json.dumps(jwt_part)
    bytes_object: bytes = jwt_part_string.encode('utf-8')
    return base64.b64encode(bytes_object)


def sign_jwt(jwt: dict) -> str:
    header_encoded: bytes = encode_jwt_part(jwt["header"])
    payload_encoded: bytes = encode_jwt_part(jwt["payload"])

    header_decoded: str = header_encoded.decode('utf-8')
    payload_decoded: str = payload_encoded.decode('utf-8')

    signature: str = hmac.new(byte_key, (header_decoded + "." + payload_decoded).encode('utf-8'), hashlib.sha256)\
        .hexdigest().upper()
    return header_decoded + "." + payload_decoded + "." + signature


def verify_jwt(token: str) -> bool:
    [header_decoded, payload_decoded, signature_part] = token.split(".")
    signature: str = hmac.new(byte_key, (header_decoded + "." + payload_decoded).encode('utf-8'), hashlib.sha256) \
        .hexdigest().upper()
    if signature != signature_part:
        return False
    payload_dict: dict = decode_jwt_part(payload_decoded)
    if payload_dict["exp"] < datetime.now().timestamp():
        return False
    else:
        return True


# use this to decode payload or header from token to dictionary
def decode_jwt_part(jwt_part: str) -> dict:
    payload_encoded: bytes = jwt_part.encode('utf-8')
    payload_bytes: bytes = base64.b64decode(payload_encoded)
    payload_string: str = payload_bytes.decode('utf-8')
    return json.loads(payload_string)


def extract_jwt_dictionary_from_token(token: str) -> dict:
    [header_decoded, payload_decoded, signature_part] = token.split(".")
    header_dict: dict = decode_jwt_part(header_decoded)
    payload_dict: dict = decode_jwt_part(payload_decoded)
    return {
        "header": header_dict,
        "payload": payload_dict
    }


def extract_claim(token: str, claim):
    [header_decoded, payload_decoded, signature_part] = token.split(".")
    payload_dict: dict = decode_jwt_part(payload_decoded)
    if claim not in payload_dict:
        raise Exception("Claim " + claim + " is not set")
    else:
        return payload_dict[claim]



