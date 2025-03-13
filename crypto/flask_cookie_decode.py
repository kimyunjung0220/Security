from itsdangerous import base64_decode
import zlib

def decode(cookie):
    payload = cookie
    if payload.startswith('.'):
        return zlib.decompress(base64_decode(payload[1:])).decode('utf-8')
    else:
        return base64_decode(payload).encode('utf-8')
