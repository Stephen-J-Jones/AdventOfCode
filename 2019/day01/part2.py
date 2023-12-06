from shared import SAMPLE, PUZZLE, read_lines


def module_mass():
    total = 0
    for line in read_lines(PUZZLE):
        module_fuel = calc_fuel_required_for_mass(line)
        fuel_list = [module_fuel]
        fuel_mass(fuel_list)
        total += sum(fuel_list)
    return total


def calc_fuel_required_for_mass(line):
    return max(0, int(line) // 3 - 2)


def fuel_mass(fuel_list: list):
    if fuel_list[-1] > 0:
        new_fuel = calc_fuel_required_for_mass(fuel_list[-1])
        fuel_list.append(new_fuel)
        fuel_mass(fuel_list)


if __name__ == "__main__":
    print(module_mass())
