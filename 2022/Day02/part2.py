from shared import read_lines

ELF_ROCK = 'A'
ELF_PAPER = 'B'
ELF_SCISSORS = 'C'
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

ELF_SCORES = {ELF_ROCK: 1, ELF_PAPER: 2, ELF_SCISSORS: 3}

WIN_SCORE = 6
DRAW_SCORE = 3


def which_throw(elf_throw, throw):
    if throw == DRAW:
        return elf_throw
    if throw == WIN:
        if elf_throw == ELF_ROCK: return ELF_PAPER
        if elf_throw == ELF_PAPER: return ELF_SCISSORS
        if elf_throw == ELF_SCISSORS: return ELF_ROCK
    if throw == LOSE:
        if elf_throw == ELF_ROCK: return ELF_SCISSORS
        if elf_throw == ELF_PAPER: return ELF_ROCK
        if elf_throw == ELF_SCISSORS: return ELF_PAPER


if __name__ == '__main__':
    total = 0
    lines = read_lines('puzzle_input.txt')
    for line in lines:
        score = 0
        elf_throw = line[0]
        throw = line[2]
        if throw == WIN:
            score += WIN_SCORE
        if throw == DRAW:
            score += DRAW_SCORE
        score += ELF_SCORES[which_throw(elf_throw, throw)]
        total += score
    print(total)
