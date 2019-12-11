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
            slope += '>'
        else:
            slope += '<'
    elif point_a[0] == point_b[0]:
        slope = 'vertical'
        if point_a[1] > point_b[1]:
            slope += '^'
        else:
            slope += 'v'
    else:
        slope = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])

        if point_a[0] > point_b[0]:
            slope = str(slope) + '>'
        else:
            slope = str(slope) + '<'

    return slope


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
    slopes.sort()

    print(slopes[199])
    return slopes[199][1][0] * 100 + slopes[199][1][1]


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
