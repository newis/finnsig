import base64

def obfuscate(string):
    """Apply a ROT13-like transformation to the input string."""
    obfuscated_chars = [
        chr(ord(char) + 13) if 'a' <= char < 'n' or 'A' <= char < 'N' else
        chr(ord(char) - 13) if 'n' <= char <= 'z' or 'N' <= char <= 'Z' else
        char
        for char in string
    ]
    return ''.join(obfuscated_chars)

def decode_hmac_key(encoded_key):
    """Decode the HMAC key by reversing obfuscation and Base64 decoding."""
    unobfuscated_string = obfuscate(encoded_key)
    decoded_bytes = base64.b64decode(unobfuscated_string)
    return decoded_bytes.decode('utf-8')
