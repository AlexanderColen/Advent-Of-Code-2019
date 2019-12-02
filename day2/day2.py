def run_intcode(noun, verb):
    with open('input_day2', 'r') as f:
        intcode = [int(x) for x in f.readlines()[0].split(',')]

    intcode[1] = noun
    intcode[2] = verb

    for i in range(0, len(intcode), 4):
        if intcode[i] == 1:
            intcode[intcode[i + 3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        elif intcode[i] == 2:
            intcode[intcode[i + 3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        elif intcode[i] == 99:
            return intcode[0]

    return None


def puzzle1():
    return run_intcode(noun=12, verb=2)


def puzzle2():
    for noun in range(0, 99):
        for verb in range(0, 99):
            if run_intcode(noun=noun, verb=verb) == 19690720:
                return 100 * noun + verb

    return None


if __name__ == '__main__':
    print(f'Puzzle 1 outcome: {puzzle1()}')
    print(f'Puzzle 2 outcome: {puzzle2()}')
