from collections import namedtuple
import timeit


def get_grid_namedtuple(directions):
    print('Namedtuples grid...')
    Point = namedtuple('Point', 'x y steps')

    points = {0: [], 1: []}

    for num, wire_direction in enumerate(directions):
        x = 0
        y = 0
        steps = 0

        points[num].append(Point(x=x, y=y, steps=steps))

        for instruction in wire_direction:
            # Split instruction into direction (R/L/U/D) and steps.
            d = [instruction[0], int(instruction.lstrip(instruction[0]))]

            steps += d[1]
            # Increment correct coordinate.
            if d[0] == 'R':
                x += d[1]
                points[num].append(Point(x=x, y=y, steps=steps))
            elif d[0] == 'L':
                x -= d[1]
                points[num].append(Point(x=x, y=y, steps=steps))
            elif d[0] == 'U':
                y += d[1]
                points[num].append(Point(x=x, y=y, steps=steps))
            elif d[0] == 'D':
                y -= d[1]
                points[num].append(Point(x=x, y=y, steps=steps))

    return points


def get_grid_points_with_steps(directions):
    print('Alternative grid...')

    points = {0: {'x': [], 'y': [], 'steps': []}, 1: {'x': [], 'y': [], 'steps': []}}

    for num, wire_instructions in enumerate(directions):
        points[num]['x'] = []
        points[num]['y'] = []
        points[num]['steps'] = []
        x = 0
        y = 0
        steps = 0
        for instruction in wire_instructions:
            # Split instruction into direction (R/L/U/D) and steps.
            d = [instruction[0], int(instruction.lstrip(instruction[0]))]

            # Increment correct coordinate.
            if d[0] == 'R':
                for i in range(d[1]):
                    x += 1
                    steps += 1
                    points[num]['x'].append(x)
                    points[num]['y'].append(y)
                    points[num]['steps'].append(steps)
            elif d[0] == 'L':
                for i in range(d[1]):
                    x -= 1
                    steps += 1
                    points[num]['x'].append(x)
                    points[num]['y'].append(y)
                    points[num]['steps'].append(steps)
            elif d[0] == 'U':
                for i in range(d[1]):
                    y += 1
                    steps += 1
                    points[num]['x'].append(x)
                    points[num]['y'].append(y)
                    points[num]['steps'].append(steps)
            elif d[0] == 'D':
                for i in range(d[1]):
                    y -= 1
                    steps += 1
                    points[num]['x'].append(x)
                    points[num]['y'].append(y)
                    points[num]['steps'].append(steps)

    return points


def get_grid_points(directions):
    print('Regular grid...')
    points = {}
    index = 0

    for wire in directions:
        current_x = 0
        current_y = 0
        wire_points = []
        for num, d in enumerate(wire):
            # Right
            if d.startswith('R'):
                for x in range(current_x, current_x + int(d.lstrip('R'))):
                    current_x += 1
                    wire_points.append(tuple([current_x, current_y]))
            # Left
            elif d.startswith('L'):
                for x in range(current_x, current_x + int(d.lstrip('L'))):
                    current_x -= 1
                    wire_points.append(tuple([current_x, current_y]))
            # Up
            elif d.startswith('U'):
                for x in range(current_x, current_x + int(d.lstrip('U'))):
                    current_y += 1
                    wire_points.append(tuple([current_x, current_y]))
            # Down
            elif d.startswith('D'):
                for x in range(current_x, current_x + int(d.lstrip('D'))):
                    current_y -= 1
                    wire_points.append(tuple([current_x, current_y]))
        points[index] = wire_points
        index += 1

    return points


def puzzle1(points):
    print('Puzzle 1')

    closest = 10000000000000
    intersections = set(points[0]).intersection(set(points[1]))
    for i in intersections:
        distance = abs(i[0]) + abs(i[1])
        if distance < closest:
            closest = distance

    return closest


def puzzle2(points):
    print('Calculating fewest steps...')
    print(f'Array length: {len(points[0]["x"])}')
    fewest_steps = 1000000000
    # Loop over first wire's x:
    for num1, x1 in enumerate(points[0]['x']):
        # Loop over list of intersection with second wire's x:
        for num2 in [num2 for num2, x2 in enumerate(points[1]['x']) if x1 == x2]:
            if points[0]['y'][num1] == points[1]['y'][num2]:
                steps = points[0]['steps'][num1] + points[1]['steps'][num2]
                print(steps, num1, num2)
                if fewest_steps > steps:
                    fewest_steps = steps

    return fewest_steps


if __name__ == '__main__':
    instructions = []
    with open('input_day3', 'r') as f:
        for l in f:
            instructions.append(l.split(','))

    elapsed_time = timeit.timeit(lambda: get_grid_points(directions=instructions), number=1)
    print(f'Time to generate grid without steps: {elapsed_time}')

    elapsed_time = timeit.timeit(lambda: get_grid_points_with_steps(directions=instructions), number=1)
    print(f'Time to generate grid with steps: {elapsed_time}')

    elapsed_time = timeit.timeit(lambda: get_grid_namedtuple(directions=instructions), number=1)
    print(f'Time to generate grid with namedtuple: {elapsed_time}')

    grid_points = get_grid_points(directions=instructions)
    elapsed_time = timeit.timeit(lambda: puzzle1(points=grid_points), number=1)
    print(f'Time for puzzle 1: {elapsed_time}')

    grid_points = get_grid_points_with_steps(directions=instructions)
    elapsed_time = timeit.timeit(lambda: puzzle2(points=grid_points), number=1)
    print(f'Time for puzzle 2: {elapsed_time}')

    grid_points = get_grid_points(directions=instructions)
    print(f'Puzzle 1 outcome: {puzzle1(grid_points)}')

    grid_points = get_grid_points_with_steps(directions=instructions)
    print(f'Alternative Puzzle 2 outcome: {puzzle2(grid_points)}')

"""
# Test 1
instructions[0] = ['R8', 'U5', 'L5', 'D3']
instructions[1] = ['U7', 'R6', 'D4', 'L4']
# Test 2
instructions[0] = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
instructions[1] = ['U62','R66','U55','R34','D71','R55','D58','R83']
# Test 3
instructions[0] = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
instructions[1] = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
"""