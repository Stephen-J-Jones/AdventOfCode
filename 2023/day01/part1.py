from shared import read_lines, SAMPLE, PUZZLE, find_all_digits_in_string

if __name__ == "__main__":
    result = 0
    for line in read_lines(PUZZLE):
        numbers = find_all_digits_in_string(line)
        result += 10 * numbers[0] + numbers[-1]
    print(result)
