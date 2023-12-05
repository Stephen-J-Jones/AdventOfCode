from collections import defaultdict

from shared import SAMPLE, PUZZLE, read_lines


def game_points(line):
    no_card = [part.strip() for part in line.split(":")]
    numbers = [part.strip() for part in no_card[-1].split("|")]
    winning = {n.strip() for n in numbers[0].split(' ') if n}
    play = {n.strip() for n in numbers[1].split(' ') if n}
    return len(winning & play)


if __name__ == "__main__":
    card_copies = defaultdict(int)
    i = 0
    for line in read_lines(PUZZLE):
        card_copies[i] = card_copies.get(i, 0) + 1
        points = game_points(line)
        for c in range(i + 1, i + points + 1):
            card_copies[c] += card_copies[i]
        i += 1
    print(sum(card_copies.values()))
