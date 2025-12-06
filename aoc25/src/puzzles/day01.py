from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    print(input_data)

    count = 0
    position = 50

    for move in input_data:
        direction = move[0:1]
        amount = int(move[1:])

        if direction == 'L':
            position -= amount
        else:
            position += amount

        if not(0 < position < 99):
            position %= 100

        if position == 0:
            count += 1

    return count


def solve_part2(data: str):
    input_data = parse_data(data)
    print(input_data)

    count = 0
    position = 50

    for move in input_data:
        direction = move[0:1]
        amount = int(move[1:])

        for _ in range(amount):
            if direction == 'L':
                position -= 1
            else:
                position += 1

            if not(0 < position < 99):
                position %= 100

            if position == 0:
                count += 1


    return count
