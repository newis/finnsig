import hmac
import hashlib
import base64
from .obfuscation import decode_hmac_key

def generate_hmac(key, method, path, query_string="", service="", body=""):
    """Calculate the FINN-GW-KEY using HMAC-SHA512, including the request body if present."""
    method = method.upper()
    path = "" if path == "/" else path
    query_string = f"?{query_string}" if query_string else ""
    
    message = f"{method};{path}{query_string};{service};"
    message_bytes = message.encode('utf-8')
    
    if body:
        message_bytes += body.encode('utf-8')

    hmac_hash = hmac.new(key.encode('utf-8'), message_bytes, hashlib.sha512)
    return base64.b64encode(hmac_hash.digest()).decode('utf-8')

def finn_hmac(method, path, query_string, service_header, body=""):
    """Generate the FINN-GW-KEY for a given HTTP method, path, query string, service header, and body."""
    encoded_hmac_key = 'MQD1MzLjZ2ZgLwp4Zl00ATD5YJV5ATRgLzVlBTEvLmNkAzR2'
    decoded_hmac_key = decode_hmac_key(encoded_hmac_key)
    return generate_hmac(decoded_hmac_key, method, path, query_string, service_header, body)
