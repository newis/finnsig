## Overview

`finnsig` is a Python package used to generate the `FINN-GW-KEY`, a signature required for certain APIs on FINN.no. This key is used to sign HTTP requests sent to these APIs. The package handles obfuscating and decoding the HMAC key, constructs the necessary message, and generates the `FINN-GW-KEY`.

The package simplifies the process of generating the `FINN-GW-KEY` signature, which developers, security researchers, and bug bounty hunters need to include in their requests when interacting with FINN.no’s APIs.

## How It Works

1. **Decode the Key**: The HMAC key is decoded using a combination of obfuscation reversal and Base64 decoding.
2. **Build the Message**: The message to be signed is constructed from the HTTP method, path, query string, service header, and the request body.
3. **Generate the Signature**: The HMAC-SHA512 signature is created and Base64 encoded, resulting in the `FINN-GW-KEY` header.

## Example Usage

Here’s how you can use `finnsig` to sign a request:

```python
from finnsig import finn_hmac

# Request details
http_method = "PUT"
path = "/ad/bap/12345678/update"
query_string = ""
service_header = "APPS-ADINPUT"
body = '{"description": "Testannonse", "title": "Testannonse", "location": [{"country": "NO", "postal-code": "1337"}]}'

# Generate the FINN-GW-KEY
finn_gw_key = finn_hmac(http_method, path, query_string, service_header, body)
print(f"FINN-GW-KEY: {finn_gw_key}")
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/newis/finnsig
   ```

2. Install the package:
   ```bash
   pip install .
   ```

## Related Tools

For Burp Suite users, there’s an extension available that automatically updates the `FINN-GW-KEY`. [Get it here](https://gist.github.com/newis/89d162558086d0dd82ecc15c4f88aa6d).