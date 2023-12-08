from collections import defaultdict
from functools import cmp_to_key

from shared import SAMPLE, PUZZLE, read_lines

CARDS = "AKQJT98765432"[::-1]

FIVE = 1
FOUR = 2
FULL = 3
THREE = 4
PAIRS = 5
PAIR = 6
HIGH = 7

HAND_TYPES = [FIVE, FOUR, FULL, THREE, PAIRS, PAIR, HIGH]


def get_hand_type(cards):
    res = 0
    if is_five_of_kind(cards):
        res += FIVE
    if is_four_of_a_kind(cards):
        res += FOUR
    if is_full_house(cards):
        res += FULL
    if is_three_of_a_kind(cards):
        res += THREE
    if is_two_pair(cards):
        res += PAIRS
    if is_one_pair(cards):
        res += PAIR
    if is_high_card(cards):
        res += HIGH
    if res not in HAND_TYPES:
        raise Exception
    return res


def is_five_of_kind(cards):
    return len(set(cards)) == 1


def is_four_of_a_kind(cards):
    labels = set(cards)
    if len(labels) == 2:
        label_count = {}
        for l in labels:
            label_count[l] = cards.count(l)
        return set(label_count.values()) == {4, 1}


def is_full_house(cards):
    labels = set(cards)
    if len(labels) == 2:
        label_count = {}
        for l in labels:
            label_count[l] = cards.count(l)
        return set(label_count.values()) == {3, 2}


def is_three_of_a_kind(cards):
    labels = set(cards)
    if len(labels) == 3:
        label_count = {}
        for l in labels:
            label_count[l] = cards.count(l)
        return sorted(list(label_count.values())) == [1, 1, 3]


def is_two_pair(cards):
    labels = set(cards)
    if len(labels) == 3:
        label_count = {}
        for l in labels:
            label_count[l] = cards.count(l)
        return sorted(list(label_count.values())) == [1, 2, 2]


def is_one_pair(cards):
    labels = set(cards)
    if len(labels) == 4:
        label_count = {}
        for l in labels:
            label_count[l] = cards.count(l)
        return sorted(list(label_count.values())) == [1, 1, 1, 2]


def is_high_card(cards):
    return len(set(cards)) == len(cards)


def hand_compare(first, second):
    for i in range(len(first[0])):
        idx1 = CARDS.index(first[0][i])
        idx2 = CARDS.index(second[0][i])
        if idx1 > idx2:
            return 1
        if idx1 < idx2:
            return -1
    return 0


def sort_hands(hands):
    sorted_hands = []
    for type in HAND_TYPES:
        sorted_type = sorted(hands[type], key=cmp_to_key(hand_compare), reverse=True)
        sorted_hands += sorted_type
    return sorted_hands


if __name__ == "__main__":
    hands = defaultdict(list)
    for hand in read_lines(PUZZLE):
        cards = hand[:5]
        bid = hand[5:]
        hands[get_hand_type(cards)].append((cards, bid))
    s = sort_hands(hands)[::-1]
    total_winnings = 0
    for i in range(len(s)):
        total_winnings += (i + 1) * int(s[i][1])
    print(total_winnings)
