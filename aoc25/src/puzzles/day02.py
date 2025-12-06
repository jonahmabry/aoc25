from ..utils import parse_data

EXAMPLE = ['11-22,95-115,998-1012,1188511880-1188511890,222220-222224,'
           '1698522-1698528,446443-446449,38593856-38593862,565653-565659,'
           '824824821-824824827,2121212118-2121212124']

def solve_part1(data: str):
    input_data = parse_data(data)
    # input_data = EXAMPLE
    print(input_data)

    total = 0
    endpoints = input_data[0].split(',')

    for endpoint in endpoints:
        low, high = endpoint.split('-')
        for i in range(int(low), int(high) + 1):
            i = str(i)
            first_half = i[0:len(i)//2]
            second_half = i[len(i) // 2:]

            if first_half == second_half:
                # print(i)
                total += int(i)

    return total


def solve_part2(data: str):
    input_data = parse_data(data)
    # input_data = EXAMPLE
    print(input_data)

    total = 0
    endpoints = input_data[0].split(',')
    sequences = [2,3,5,7]

    for endpoint in endpoints:
        low, high = map(int, endpoint.split('-'))
        for i in range(low, high + 1):
            i = str(i)
            for seq in sequences:
                if len(i) % seq == 0:
                    block_size = len(i) // seq
                    blocks = []
                    for j in range(seq):
                        blocks.append(i[j*block_size:(j+1)*block_size])

                    if len(set(blocks)) == 1:
                        total += int(i)
                        break

    return total
