from shared import read_lines

ELF_ROCK = 'A'
ELF_PAPER = 'B'
ELF_SCISSORS = 'C'
ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

ELF_SCORES = {ELF_ROCK: 1, ELF_PAPER: 2, ELF_SCISSORS: 3}
SCORES = {ROCK: 1, PAPER: 2, SCISSORS: 3}

WIN_SCORE = 6
DRAW_SCORE = 3

WIN = 'win'
LOSE = 'lose'
DRAW = 'draw'


def is_win_lose_draw(elf_throw, throw):
    if ELF_ROCK == elf_throw:
        if throw == ROCK: return DRAW
        if throw == PAPER: return WIN
        if throw == SCISSORS: return LOSE
    if ELF_PAPER == elf_throw:
        if throw == ROCK: return LOSE
        if throw == PAPER: return DRAW
        if throw == SCISSORS: return WIN
    if ELF_SCISSORS == elf_throw:
        if throw == ROCK: return WIN
        if throw == PAPER: return LOSE
        if throw == SCISSORS: return DRAW


if __name__ == '__main__':
    lines = read_lines('puzzle_input.txt')
    elf_total = 0
    total = 0
    for line in lines:
        elf_throw = line[0]
        throw = line[2]
        elf_score = ELF_SCORES[elf_throw]
        score = SCORES[throw]
        win_lose_draw = is_win_lose_draw(elf_throw, throw)
        if win_lose_draw == WIN:
            score += WIN_SCORE
        if win_lose_draw == DRAW:
            score += DRAW_SCORE
            elf_score += DRAW_SCORE
        if win_lose_draw == LOSE:
            elf_score += WIN_SCORE
        elf_total += elf_score
        total += score

    print(total)
