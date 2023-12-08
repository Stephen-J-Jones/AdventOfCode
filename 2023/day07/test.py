from collections import defaultdict
from functools import cmp_to_key
from unittest import TestCase
from part1 import (
    is_five_of_kind, is_four_of_a_kind, is_three_of_a_kind, is_full_house, is_two_pair, is_one_pair,
    is_high_card, hand_compare, sort_hands, HIGH, FIVE, )


class TestHands(TestCase):
    def test_5_of_kind(self):
        cards = '22222'
        self.assertTrue(is_five_of_kind(cards))

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


class TestComparer(TestCase):
    def test_simple_sort(self):
        first = ('Q',)
        second = ('3',)
        third = ('A',)
        self.assertEqual([second, first, third], sorted([first, second, third], key=cmp_to_key(hand_compare)))

    def test_first_different(self):
        first = ('23456',)
        second = ('Q3456',)
        result = hand_compare(first, second)
        self.assertEqual(-1, result)

    def test_last_different(self):
        first = ('23456',)
        second = ('2345A',)
        result = hand_compare(first, second)
        self.assertEqual(-1, result)

    def test_same(self):
        first = ('AKQJT',)
        self.assertEqual(0, hand_compare(first, first))

    def test_from_input(self):
        first = ('23A49',)
        second = ('23846',)
        result = hand_compare(first, second)
        self.assertEqual(1, result)