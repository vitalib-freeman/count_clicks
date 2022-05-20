import os
import unittest
import counter
import requests
from dotenv import load_dotenv


class TestBitLy(unittest.TestCase):
    def test_can_obtain_short_link(self):
        url = 'www.yandex.ru'
        shortened_url = counter.shorten(url)
        self.assertIn("bit.ly", shortened_url)

    def test_connect_to_bitly(self):
        load_dotenv()
        token = os.getenv("BITLY_TOKEN")
        url = "https://api-ssl.bitly.com/v4/user"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.text)
        self.assertIn("login", response.json())


if __name__ == '__main__':
    unittest.main()
