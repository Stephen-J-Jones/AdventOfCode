from collections import defaultdict
from functools import cmp_to_key

from shared import SAMPLE, PUZZLE, read_lines

CARDS = "AKQJT98765432"[::-1]

FIVE = 7
FOUR = 6
FULL = 5
THREE = 4
PAIRS = 3
PAIR = 2
HIGH = 1

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


def get_strength(cards):
    strength = str(get_hand_type(cards))
    for c in cards:
        strength += f"{CARDS.index(c):02}"
    return strength


if __name__ == "__main__":
    hands = []
    for hand in read_lines(PUZZLE):
        cards = hand[:5]
        bid = hand[5:]
        strength = get_strength(cards)
        hands.append((strength, cards, bid))
    total_winnings = 0
    sorted_hands = sorted(hands, key=lambda x: x[0])
    for idx, s in enumerate(sorted_hands):
        total_winnings += (idx + 1) * int(s[2])
    print(total_winnings)
