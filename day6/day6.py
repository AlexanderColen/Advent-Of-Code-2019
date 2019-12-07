import networkx as nx


def read_input():
    raw_data = []
    processed_data = []

    with open('input_day6', 'r') as f:
        for line in f:
            raw_data.append(line.rstrip('\n'))

    for d in raw_data:
        processed_data.append(d.split(')'))

    return processed_data


def puzzle1(data):
    g = nx.Graph(data)
    orbits = 0
    for node in g.nodes:
        orbits += nx.shortest_path_length(G=g, source=node, target='COM')
    return orbits


def puzzle2(data):
    g = nx.Graph(data)
    return nx.shortest_path_length(G=g, source='YOU', target='SAN') - 2


if __name__ == '__main__':
    processed = read_input()
    print(f'Puzzle 1 outcome: {puzzle1(data=processed)}')
    print(f'Puzzle 2 outcome: {puzzle2(data=processed)}')

"""
test_data = ['COM)B', 'B)C', 'C)D', 'D)E',
             'E)F', 'B)G', 'G)H', 'D)I',
             'E)J', 'J)K', 'K)L']
test_data = ['COM)B', 'B)C', 'B)E', 'C)D', 'C)F', 'F)G']
"""