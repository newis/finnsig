## Overview

`finnsig` is a Python package used to generate the `FINN-GW-KEY` HTTP header, which is essential for authenticating requests to certain APIs used by the FINN.no service. This package handles the obfuscation and decoding of the HMAC key, constructs the necessary message components, and calculates the HMAC-SHA512 hash required for the `FINN-GW-KEY` header.

## Purpose

The `finnsig` package was created to simplify the process of generating the `FINN-GW-KEY` header, which is required for making authenticated API requests to FINN.no. This is particularly useful for developers, security researchers, and bug bounty hunters who need to interact with FINN.no's API in a programmatic or automated way, ensuring that their requests are properly authenticated.

## Features

- **Obfuscation and Decoding:** The package includes functionality to reverse the obfuscation applied to the HMAC key and decode it from Base64 format.
- **HMAC Generation:** It calculates the `FINN-GW-KEY` by constructing a message from the HTTP method, path, query string, and service header, then applying HMAC-SHA512 and encoding the result in Base64.
- **Modular Design:** The package is designed to be easily integrated into other scripts or applications that need to generate the `FINN-GW-KEY`.

## How It Works

1. **Obfuscation Reversal:** The HMAC key, which is provided in an obfuscated and Base64-encoded format, is first de-obfuscated using a ROT13-like cipher and then decoded from Base64.

2. **Message Construction:** The HTTP method, path, query string, and service header are used to construct a message in a specific format required for generating the `FINN-GW-KEY`.

3. **HMAC Calculation:** The package calculates an HMAC-SHA512 hash of the constructed message using the decoded HMAC key, and then encodes this hash in Base64.

4. **Key Output:** The final output is the `FINN-GW-KEY`, which can be used as an HTTP header in API requests to authenticate them.

## Example Usage

```python
from finnsig import finn_hmac

http_method = "GET"
path = "/ui/objectpage"
query_string = "adId=12345678&previewMode=false"
service_header = "TJT-API"

finn_gw_key = finn_hmac(http_method, path, query_string, service_header)
print(f"FINN-GW-KEY: {finn_gw_key}")
```

## Installation

Clone the repository using `git clone https://github.com/newis/finnsig` and install the package with `pip install .`

## Related Tools

For those who are using Burp Suite for security testing, a Burp Suite extension has been created to automatically update the FINN-GW-KEY header based on modified requests. You can find the extension [here](https://gist.github.com/newis/89d162558086d0dd82ecc15c4f88aa6d).