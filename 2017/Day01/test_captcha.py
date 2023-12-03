from unittest import TestCase
from part1 import sum_captcha


class TestCapcha(TestCase):
    def test_one(self):
        input = '1122'
        expected = 3
        self.assertEqual(sum_captcha(input), expected)

    def test_two(self):
        input = '1111'
        expected = 4
        self.assertEqual(sum_captcha(input), expected)

    def test_three(self):
        input = '1234'
        expected = 0
        self.assertEqual(sum_captcha(input), expected)

    def test_four(self):
        input = '91212129'
        expected = 9
        self.assertEqual(sum_captcha(input), expected)
