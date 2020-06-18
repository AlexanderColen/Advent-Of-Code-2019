import math


def read_input():
    with open('input_day14', 'r') as f:
        return [x.strip() for x in f.readlines()]


def split_reaction(reaction):
    inputs = {}
    output = {}

    front, back = reaction.split(' => ')
    front = front.split(', ')
    back = back.split(' ')
    output[back[1]] = int(back[0])

    if len(front) > 1:
        for item in front:
            amount, ingredient = item.split(' ')
            inputs[ingredient] = int(amount)
    else:
        amount, ingredient = front[0].split(' ')
        inputs[ingredient] = int(amount)

    return inputs, output


def puzzle1(reactions):
    excess = {}
    required = {}

    # Find basic requirements for FUEL.
    for reaction in reactions:
        inputs, output = split_reaction(reaction=reaction)
        if 'FUEL' in output:
            required = inputs
            print(reaction)

    # Loop until required only has ORE.
    # while len(required) != 1 and 'ORE' not in required:
    for req in required:
        new_dict = required.copy()
        for reaction in reactions:
            inputs, output = split_reaction(reaction=reaction)
            if req in output:
                times = math.ceil(required[req] / output[req])
                print(f'Required: {req} - Reaction: {reaction} - Times: {times}')
                for i in inputs:
                    new_dict[i] = inputs[i]
                new_dict.pop(req)
        required = new_dict
        print(required)

    return None


def puzzle2():

    return None


if __name__ == '__main__':
    data = read_input()

    data = ['9 ORE => 2 A',
            '8 ORE => 3 B',
            '7 ORE => 5 C',
            '3 A, 4 B => 1 AB',
            '5 B, 7 C => 1 BC',
            '4 C, 1 A => 1 CA',
            '2 AB, 3 BC, 4 CA => 1 FUEL']
    print(f'Puzzle 1 outcome: {puzzle1(reactions=data)}')
    print(f'Puzzle 2 outcome: {puzzle2()}')

# Test Data
"""
data = ['9 ORE => 2 A',
        '8 ORE => 3 B',
        '7 ORE => 5 C',
        '3 A, 4 B => 1 AB',
        '5 B, 7 C => 1 BC',
        '4 C, 1 A => 1 CA',
        '2 AB, 3 BC, 4 CA => 1 FUEL']
165 ORE for 1 FUEL
"""
