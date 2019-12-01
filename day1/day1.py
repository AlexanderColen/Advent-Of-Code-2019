import math


def get_fuel_required(number):
    return math.floor(int(number) / 3) - 2


def puzzle1():
    total = 0
    # Read inputs and loop over line by line.
    with open('input_day1', 'r') as f:
        for l in f:
            total += get_fuel_required(l)

    return total


def puzzle2():
    total = 0
    # Read inputs and loop over line by line.
    with open('input_day1', 'r') as f:
        for l in f:
            fuel = get_fuel_required(l)
            total += fuel
            while fuel > 0:
                fuel = get_fuel_required(fuel)
                if fuel > 0:
                    total += fuel

    return total


if __name__ == '__main__':
    print(f'Puzzle 1 fuel required: {puzzle1()}')
    print(f'Puzzle 2 fuel required: {puzzle2()}')
