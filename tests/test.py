import unittest
from finn_hmac.obfuscation import obfuscate, decode_hmac_key
from finn_hmac.hmac_generator import generate_hmac, finn_hmac

class TestObfuscation(unittest.TestCase):
    def test_obfuscate(self):
        self.assertEqual(obfuscate("Hello"), "Uryyb")
        self.assertEqual(obfuscate("Uryyb"), "Hello")

    def test_decode_hmac_key(self):
        encoded_key = obfuscate("c2VjcmV0X2tleQ==")
        self.assertEqual(decode_hmac_key(encoded_key), "secret_key")

class TestHMACGenerator(unittest.TestCase):
    def test_generate_hmac(self):
        key = "secret_key"
        method = "GET"
        path = "/api/data"
        query_string = "user_id=123"
        service = "ExampleService"
        expected_output = "zGpjJC+h7n5uYOw6Y7lKjmRGvjB+BqrGXaqsVIjCajfyv2nX3wwDkwvRJFfB8Cuj6qwPQ9+GYSwcSO2AVUXWmw=="
        self.assertEqual(generate_hmac(key, method, path, query_string, service), expected_output)

    def test_finn_hmac(self):
        method = "POST"
        path = "/transaction/submit"
        query_string = "amount=100&currency=USD"
        service_header = "PaymentGateway"
        expected_output = "d1CfDEQmgNzoYiPJJ+cHai3BvGWPFYA8WPN2l7r31irFsM1ayWA4Z/A9K6/Vgbpiw+OdvmsnPJzYEOrZNnVHgg=="
        self.assertEqual(finn_hmac(method, path, query_string, service_header), expected_output)

if __name__ == '__main__':
    unittest.main()
