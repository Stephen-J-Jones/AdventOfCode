from collections import defaultdict
from functools import cmp_to_key

from shared import SAMPLE, PUZZLE, read_lines
from collections import Counter

CARDS = "AKQT98765432J"[::-1]

FIVE = 7
FOUR = 6
FULL = 5
THREE = 4
PAIRS = 3
PAIR = 2
HIGH = 1

HAND_TYPES = [FIVE, FOUR, FULL, THREE, PAIRS, PAIR, HIGH]


def get_hand_type(cards):
    if is_five_of_kind(cards):
        return FIVE
    if is_four_of_a_kind(cards):
        return FOUR
    if is_full_house(cards):
        return FULL
    if is_three_of_a_kind(cards):
        return THREE
    if is_two_pair(cards):
        return PAIRS
    if is_one_pair(cards):
        return PAIR
    if is_high_card(cards):
        return HIGH
    raise Exception


def is_five_of_kind(cards):
    labels = set(cards)
    for l in labels:
        new_cards = cards.replace('J', l)
        count = Counter(new_cards)
        if set(count.values()) == {5}:
            return True


def is_four_of_a_kind(cards):
    labels = set(cards)
    for l in labels:
        new_cards = cards.replace('J', l)
        count = Counter(new_cards)
        if set(count.values()) == {4, 1}:
            return True


def is_full_house(cards):
    labels = set(cards)
    for l in labels:
        new_cards = cards.replace('J', l)
        count = Counter(new_cards)
        if set(count.values()) == {3, 2}:
            return True


def is_three_of_a_kind(cards):
    labels = set(cards)
    for l in labels:
        new_cards = cards.replace('J', l)
        count = Counter(new_cards)
        if sorted(list(count.values())) == [1, 1, 3]:
            return True


def is_two_pair(cards):
    labels = set(cards)
    for l in labels:
        new_cards = cards.replace('J', l)
        count = Counter(new_cards)
        if sorted(list(count.values())) == [1, 2, 2]:
            return True


def is_one_pair(cards):
    labels = set(cards)
    for l in labels:
        new_cards = cards.replace('J', l)
        count = Counter(new_cards)
        if sorted(list(count.values())) == [1, 1, 1, 2]:
            return True


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
