def read_input():
    data = []

    with open('input_day10', 'r') as f:
        for l in f:
            data.append(l.strip())

    return data


def get_asteroids(raw_data):
    asteroids = []

    for y, line in enumerate(raw_data):
        for x, char in enumerate(list(line)):
            if char == '#':
                asteroids.append([x, y])

    return asteroids


def calculate_line(point_a, point_b):
    if point_a[1] == point_b[1]:
        slope = 'horizontal'
        if point_a[0] > point_b[0]:
            char = '>'
        else:
            char = '<'
    elif point_a[0] == point_b[0]:
        slope = 'vertical'
        if point_a[1] > point_b[1]:
            char = '^'
        else:
            char = 'v'
    else:
        slope = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])

        if point_a[0] > point_b[0]:
            char = '>'
        else:
            char = '<'

    return [slope, char]


def puzzle1(asteroids):
    max_detected_asteroids = 0
    best_space = []
    all_slopes = []

    for space in asteroids:
        slopes = []
        unique_slopes = []
        detected_asteroids = 0
        for asteroid in asteroids:
            if space != asteroid:
                slope = calculate_line(point_a=space, point_b=asteroid)
                slopes.append([slope, asteroid])
                if slope not in unique_slopes:
                    unique_slopes.append(slope)
                    detected_asteroids += 1

        if max_detected_asteroids < detected_asteroids:
            max_detected_asteroids = detected_asteroids
            best_space = space
            all_slopes = slopes

    return max_detected_asteroids, best_space, all_slopes


def puzzle2(station, slopes):
    # Calculate distance per slope.
    for slope in slopes:
        distance = abs(station[0] - slope[1][0]) + abs(station[1] - slope[1][1])
        slope.append(distance)

    # Split into separate arrays.
    vertical_up = []
    vertical_down = []
    horizontal_right = []
    horizontal_left = []
    positive_right = []
    positive_left = []
    negative_right = []
    negative_left = []

    for slope in slopes:
        if slope[0][0] == 'vertical':
            if slope[0][1] == '^':
                vertical_up.append(slope)
            elif slope[0][1] == 'v':
                vertical_down.append(slope)
        elif slope[0][0] == 'horizontal':
            if slope[0][1] == '>':
                horizontal_right.append(slope)
            elif slope[0][1] == '<':
                horizontal_left.append(slope)
        elif slope[0][0] > 0:
            if slope[0][1] == '>':
                positive_right.append(slope)
            elif slope[0][1] == '<':
                positive_left.append(slope)
        elif slope[0][0] < 0:
            if slope[0][1] == '>':
                negative_right.append(slope)
            elif slope[0][1] == '<':
                negative_left.append(slope)
        else:
            print(f'Error with slope {slope}')

    # Sort all the arrays.
    vertical_up.sort(key=lambda x: (x[0][0], x[2]))
    vertical_down.sort(key=lambda x: (x[0][0], x[2]))
    horizontal_right.sort(key=lambda x: (x[0][0], x[2]))
    horizontal_left.sort(key=lambda x: (x[0][0], x[2]))
    positive_right.sort(key=lambda x: (x[0][0], x[2]))
    positive_left.sort(key=lambda x: (x[0][0], x[2]))
    negative_right.sort(key=lambda x: (x[0][0], x[2]))
    negative_left.sort(key=lambda x: (x[0][0], x[2]))

    # Append them all back together.
    sorted_slopes = []
    sorted_slopes.extend(vertical_up)
    sorted_slopes.extend(positive_right)
    sorted_slopes.extend(horizontal_right)
    sorted_slopes.extend(negative_right)
    sorted_slopes.extend(vertical_down)
    sorted_slopes.extend(positive_left)
    sorted_slopes.extend(horizontal_left)
    sorted_slopes.extend(negative_left)

    # Loop over them all and destroy them one by one.
    last_destroyed = [[[]]]
    destroyed = 0
    edited_slopes = sorted_slopes
    while destroyed != 200:
        for slope in sorted_slopes:
            if last_destroyed[0][0] != slope[0][0]:
                last_destroyed = slope
                edited_slopes.remove(slope)
                destroyed += 1
                print(f'Destroyed {destroyed} - Slope {slope}')
                if destroyed == 200:
                    return slope[1][0] * 100 + slope[1][1]
        sorted_slopes = edited_slopes


if __name__ == '__main__':
    asteroid_locations = get_asteroids(raw_data=read_input())
    max_asteroids, monitoring_station, asteroid_slopes = puzzle1(asteroids=asteroid_locations)

    print(f'Puzzle 1 outcome: {max_asteroids}')
    print(f'Puzzle 2 outcome: {puzzle2(station=monitoring_station, slopes=asteroid_slopes)}')

    """
        test_data = ['.#..#',
                     '.....',
                     '#####',
                     '....#',
                     '...##']
    test_data = ['......#.#.',
                 '#..#.#....',
                 '..#######.',
                 '.#.#.###..',
                 '.#..#.....',
                 '..#....#.#',
                 '#..#....#.',
                 '.##.#..###',
                 '##...#..#.',
                 '.#....####']
    test_data = ['#.#...#.#.',
                 '.###....#.',
                 '.#....#...',
                 '##.#.#.#.#',
                 '....#.#.#.',
                 '.##..###.#',
                 '..#...##..',
                 '..##....##',
                 '......#...',
                 '.####.###.']
    test_data = ['.#..#..###',
                 '####.###.#',
                 '....###.#.',
                 '..###.##.#',
                 '##.##.#.#.',
                 '....###..#',
                 '..#.#..#.#',
                 '#..#.#.###',
                 '.##...##.#',
                 '.....#.#..']
    test_data = ['.#..##.###...#######',
                 '##.############..##.',
                 '.#.######.########.#',
                 '.###.#######.####.#.',
                 '#####.##.#.##.###.##',
                 '..#####..#.#########',
                 '####################',
                 '#.####....###.#.#.##',
                 '##.#################',
                 '#####.##.###..####..',
                 '..######..##.#######',
                 '####.##.####...##..#',
                 '.#####..#.######.###',
                 '##...#.##########...',
                 '#.##########.#######',
                 '.####.#.###.###.#.##',
                 '....##.##.###..#####',
                 '.#.#.###########.###',
                 '#.#.#.#####.####.###',
                 '###.##.####.##.#..##']
    """
