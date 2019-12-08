import textwrap


def read_input():
    with open('input_day8', 'r') as f:
        return f.readlines()


def puzzle1(image_data):
    dimension = 25 * 6
    fewest_zeroes = 1000000000000000
    found_layer = None
    layers = textwrap.wrap(image_data, dimension)

    for layer in layers:
        zeroes = str(layer).count('0')
        if zeroes < fewest_zeroes:
            fewest_zeroes = zeroes
            found_layer = layer

    return str(found_layer).count('1') * str(found_layer).count('2')


def puzzle2(image_data):
    print('Puzzle 2')
    width = 25
    height = 6
    dimension = width * height
    layers = textwrap.wrap(text=image_data, width=dimension)
    image = list('2' * dimension)
    for layer in layers:
        for num, c in enumerate(layer):
            if image[num] == '2' and c != '2':
                image[num] = c

    image = ''.join(image)
    image = image.replace('1', '#')
    image = image.replace('0', '.')

    lines = textwrap.wrap(text=image, width=width)
    for line in lines:
        print(line)


if __name__ == '__main__':
    data = read_input()[0].strip()
    print(f'Data: {data}\n')

    print(f'Puzzle 1 outcome: {puzzle1(data)}')
    puzzle2(data)
