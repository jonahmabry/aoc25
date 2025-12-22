from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    print(input_data)

    total = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    for x, row in enumerate(input_data):
        for y, col in enumerate(row):
            if col == '@':
                num = 0
                for direction in directions:
                    if 0 <= x + direction[0] < len(input_data) and 0 <= y + direction[1] < len(input_data):
                        char = input_data[x + direction[0]][y + direction[1]]
                        if char == '@':
                            num += 1
                if num < 4:
                    print(x,y)
                    total += 1

    return total


def solve_part2(data: str):
    input_data = [list(line) for line in parse_data(data)]
    print(input_data)

    total = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    while True:
        locations = []
        for x, row in enumerate(input_data):
            for y, col in enumerate(row):
                if col == '@':
                    num = 0
                    for direction in directions:
                        if 0 <= x + direction[0] < len(input_data) and 0 <= y + direction[1] < len(input_data):
                            char = input_data[x + direction[0]][y + direction[1]]
                            if char == '@':
                                num += 1
                    if num < 4:
                        # print(x, y)
                        locations.append((x,y))
        if not locations:
            break

        for lx,ly in locations:
            input_data[lx][ly] = 'x'
            total += 1

    return total
