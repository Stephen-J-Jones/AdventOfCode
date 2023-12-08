from collections import defaultdict
from functools import cmp_to_key
from unittest import TestCase
from part2 import (
    is_five_of_kind, is_four_of_a_kind, is_three_of_a_kind, is_full_house, is_two_pair, is_one_pair,
    is_high_card, )


class TestHands(TestCase):
    def test_5_of_kind(self):
        cards = '22222'
        self.assertTrue(is_five_of_kind(cards))

    def test_JJJJ2(self):
        self.assertTrue(is_five_of_kind('JJJJ2'))

    def test_4_kind(self):
        cards = 'AAAAK'
        self.assertTrue(is_four_of_a_kind(cards))

    def test_3_kind(self):
        cards = '11123'
        self.assertTrue(is_three_of_a_kind(cards))

    def test_full_house(self):
        cards = '23332'
        self.assertTrue(is_full_house(cards))

    def test_2_pair(self):
        cards = '23432'
        self.assertTrue(is_two_pair(cards))

    def test_one_pair(self):
        cards = 'A23A4'
        self.assertTrue(is_one_pair(cards))

    def test_high_card(self):
        cards = '23456'
        self.assertTrue(is_high_card(cards))

    def test_fh_2(self):
        cards = 'aabbJ'
        self.assertTrue(is_full_house(cards))

    def test_QJJQ2(self):
        cards='QJJQ2'
        self.assertTrue(is_four_of_a_kind(cards))
