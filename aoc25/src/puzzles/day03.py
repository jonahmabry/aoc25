from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    print(input_data)

    total = 0
    for bank in input_data:
        high = 0
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                high = max(high, int(bank[i] + bank[j]))
        total += high

    return total


def solve_part2(data: str):
    input_data = parse_data(data)
    print(input_data)

    total = 0
    for bank in input_data:
        high = ""
        cur_ix = 0
        for i in range(12):
            remaining_num = 11-i
            search_range = bank[cur_ix : (len(bank) - remaining_num)]

            max_digit = max(search_range)
            found_at = search_range.index(max_digit)

            high += max_digit
            cur_ix += found_at + 1
        print(high)
        total += int(high)
    return total