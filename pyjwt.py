import hmac
import hashlib
import binascii
import base64

import json

from datetime import datetime

key = "E49756B4C8FAB4E48222A3E7F3B97CC3"
byte_key = binascii.unhexlify(key)

def create_jwt(exp = 5 * 60 * 1000) -> dict:
    jwt: dict = {}
    jwt["header"]: dict = {}
    jwt["header"]["alg"] = "HS256"
    jwt["header"]["typ"] = "JWT"
    jwt["payload"]: dict = {}
    jwt["payload"]["exp"] = datetime.now().timestamp() + exp
    return jwt

jwt = create_jwt()

def add_expiration(jwt: dict, interval_milliseconds: int):
    jwt["payload"]["exp"] = datetime.now().timestamp() + interval_milliseconds

def add_claim(jwt: dict, claim: str, value):
    jwt["payload"][claim] = value

add_claim(jwt, "id", 12)

def sign_jwt(jwt: dict) -> str:
    header_string = json.dumps(jwt["header"]) 
    header_bytes = header_string.encode('utf8')
    header_encoded = base64.b64encode(header_bytes)

    payload_string = json.dumps(jwt["payload"]) 
    payload_bytes = payload_string.encode('utf8')
    payload_encoded = base64.b64encode(payload_bytes)

    signature = hmac.new(byte_key, (header_encoded.decode('utf8') + "." + payload_encoded.decode('utf8')).encode('utf8'), hashlib.sha256).hexdigest().upper()
    return header_encoded.decode('utf8') + "." + payload_encoded.decode('utf8') + "." + signature


def verify_jwt(token) -> bool:
    [header_part, payload_part, signature_part] = token.split(".")
    header_encoded = header_part.encode('utf8')
    header_bytes = base64.b64decode(header_encoded)
    header_string = header_bytes.decode('utf8')
    
    payload_encoded = payload_part.encode('utf8')
    payload_bytes = base64.b64decode(payload_encoded)
    payload_string = payload_bytes.decode('utf8')

    signature = hmac.new(byte_key, (header_encoded.decode('utf8') + "." + payload_encoded.decode('utf8')).encode('utf8'), hashlib.sha256).hexdigest().upper()
    
    if signature_part != signature:
        return False
    
    payload: dict = json.loads(payload_string)
    if payload["exp"] < datetime.now().timestamp():
        return False
    else:
        return True

def extract_jwt(token) -> dict:
    [header_part, payload_part, signature_part] = token.split(".")
    header_encoded = header_part.encode('utf8')
    header_bytes = base64.b64decode(header_encoded)
    header_string = header_bytes.decode('utf8')
    
    payload_encoded = payload_part.encode('utf8')
    payload_bytes = base64.b64decode(payload_encoded)
    payload_string = payload_bytes.decode('utf8')

    jwt: dict = {}
    jwt["header"] = json.loads(header_string)
    jwt["payload"] = json.loads(payload_string)
    return jwt
    
def extract_claim(token, claim: str):
    [header_part, payload_part, signature_part] = token.split(".")
    header_encoded = header_part.encode('utf8')
    header_bytes = base64.b64decode(header_encoded)
    header_string = header_bytes.decode('utf8')
    
    payload_encoded = payload_part.encode('utf8')
    payload_bytes = base64.b64decode(payload_encoded)
    payload_string = payload_bytes.decode('utf8')

    payload: dict = json.loads(payload_string)
    if claim in payload:
        return payload[claim]
    else:
        raise Exception("Claim " + claim + " is not set")





