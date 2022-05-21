import io
import os
import unittest
from unittest.mock import patch

import counter
import requests
from dotenv import load_dotenv


class TestBitLy(unittest.TestCase):

    def setUp(self):
        load_dotenv()

    def test_can_obtain_short_link(self):
        url = 'https://google.ru'
        token = os.getenv("BITLY_TOKEN")
        shortened_link = counter.shorten_link(token, url)['link']
        self.assertIn("bit.ly", shortened_link)
        print(shortened_link)

    def test_connect_to_bitly(self):
        token = os.getenv("BITLY_TOKEN")
        url = "https://api-ssl.bitly.com/v4/user"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        self.assertIn("login", response.json())

    def test_get_shorten_link_for_url_from_stdin(self):
        with patch('sys.stdin', io.StringIO('https://google.com\n')) as stdin, \
                patch('sys.stdout', new_callable=io.StringIO) as stdout:
            counter.main()
            self.assertIn("bitly", stdout.getvalue())



if __name__ == '__main__':
    unittest.main()
