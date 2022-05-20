import unittest
import counter


class TestBitLy(unittest.TestCase):
    def test_can_obtain_short_link(self):
        url = 'www.yandex.ru'
        shortened_url = counter.shorten(url)
        self.assertIn("bit.ly", shortened_url)


if __name__ == '__main__':
    unittest.main()
