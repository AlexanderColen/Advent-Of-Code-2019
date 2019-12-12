import copy


def read_input():
    moons = {'Io': {'Position': {'x': 0, 'y': 0, 'z': 0}, 'Velocity': {'x': 0, 'y': 0, 'z': 0}},
             'Europa': {'Position': {'x': 0, 'y': 0, 'z': 0}, 'Velocity': {'x': 0, 'y': 0, 'z': 0}},
             'Ganymede': {'Position': {'x': 0, 'y': 0, 'z': 0}, 'Velocity': {'x': 0, 'y': 0, 'z': 0}},
             'Callisto': {'Position': {'x': 0, 'y': 0, 'z': 0}, 'Velocity': {'x': 0, 'y': 0, 'z': 0}}}
    with open('input_day12', 'r') as f:
        for num, l in enumerate(f):
            moon = moons[[key for idx, key in enumerate(moons) if idx == num][0]]
            positions = [pos.strip() for pos in l.replace('<', '').replace('>', '').replace('x=', '').replace('y=', '').replace('z=', '').split(',')]
            moon['Position']['x'] = int(positions[0])
            moon['Position']['y'] = int(positions[1])
            moon['Position']['z'] = int(positions[2])

    return moons


def move_moons(moons):
    for moon1 in moons:
        for moon2 in moons:
            if moon1 != moon2:
                x_change = 0
                y_change = 0
                z_change = 0

                if moons[moon1]['Position']['x'] > moons[moon2]['Position']['x']:
                    x_change -= 1
                elif moons[moon1]['Position']['x'] < moons[moon2]['Position']['x']:
                    x_change += 1

                if moons[moon1]['Position']['y'] > moons[moon2]['Position']['y']:
                    y_change -= 1
                elif moons[moon1]['Position']['y'] < moons[moon2]['Position']['y']:
                    y_change += 1

                if moons[moon1]['Position']['z'] > moons[moon2]['Position']['z']:
                    z_change -= 1
                elif moons[moon1]['Position']['z'] < moons[moon2]['Position']['z']:
                    z_change += 1

                moons[moon1]['Velocity']['x'] += x_change
                moons[moon1]['Velocity']['y'] += y_change
                moons[moon1]['Velocity']['z'] += z_change

    # Apply all the velocity changes.
    for moon in moons:
        moons[moon]['Position']['x'] += moons[moon]['Velocity']['x']
        moons[moon]['Position']['y'] += moons[moon]['Velocity']['y']
        moons[moon]['Position']['z'] += moons[moon]['Velocity']['z']

    return moons


def puzzle1(moons):
    print('Puzzle 1 start...')
    step = 0
    while step != 1000:
        # Calculate the gravity into the velocity.
        moons = move_moons(moons=moons)

        step += 1

    # Calculate total energy.
    energy = 0
    for moon in moons:
        pot_energy = abs(moons[moon]['Position']['x']) + abs(moons[moon]['Position']['y']) + abs(moons[moon]['Position']['z'])
        kin_energy = abs(moons[moon]['Velocity']['x']) + abs(moons[moon]['Velocity']['y']) + abs(moons[moon]['Velocity']['z'])
        energy += pot_energy * kin_energy

    return energy


def check_zero_velocities(moons):
    zeroes = [False, False, False, False]

    for num, moon in enumerate(moons):
        if moons[moon]['Velocity']['x'] == 0 and moons[moon]['Velocity']['y'] == 0 and moons[moon]['Velocity']['z'] == 0:
            zeroes[num] = True

    return zeroes[0] and zeroes[1] and zeroes[2] and zeroes[3]


def puzzle2(moons):
    print('Puzzle 2 start...')
    zero_velocities = False
    step = 0

    while not zero_velocities:
        # Calculate the gravity into the velocity.
        moons = move_moons(moons=moons)
        step += 1
        if check_zero_velocities(moons=moons):
            zero_velocities = True

    return step * 2


if __name__ == '__main__':
    data = read_input()
    print(f'Puzzle 1 outcome: {puzzle1(moons=data)}')
    print(f'Puzzle 2 outcome: {puzzle2(moons=data)}')
