from ..utils import parse_data


def solve_part1(data: str):
    input_data = iter(parse_data(data))
    print(input_data)

    ranges = set()
    total = 0

    for line in input_data:
        if line == '':
            break
        ranges.add(tuple(map(int, line.split("-"))))

    for line in input_data:
        for start, end in ranges:
            if start <= int(line) <= end:
                total += 1
                break

    return total


def solve_part2(data: str):
    input_data = parse_data(data)
    print(input_data)

    ranges = []
    total = 0

    for line in input_data:
        if line == '':
            break
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ranges.sort()
    merged = []

    current_start, current_end = ranges[0]
    for next_start, next_end in ranges[1:]:
        print(next_start, next_end)
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    merged.append((current_start, current_end))
    print(merged)
    for start, end in merged:
        total += end - start + 1

    return total
