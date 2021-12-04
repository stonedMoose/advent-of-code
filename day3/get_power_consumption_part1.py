import os

from get_lines import get_lines

ZERO = '0'
ONE = '1'


def get_power_consumption(input: str):
    bit_count = get_bit_count_by_pos(input)

    gamma = ''
    epsilon = ''
    for i in range(len(bit_count.keys())):
        if bit_count[i][ZERO] > bit_count[i][ONE]:
            gamma += ZERO
            epsilon += ONE
        else:
            gamma += ONE
            epsilon += ZERO

    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    print('gamma:', gamma_int, 'epsilon:', epsilon_int)

    return gamma_int * epsilon_int


def get_bit_count_by_pos(input):
    lines = get_lines(input)
    bit_count = init_bit_count(lines[0])
    for bits in list(map(lambda a: a.strip(), lines)):
        for i in range(len(bits.strip())):
            bit_count[i][bits[i]] += 1
    return bit_count


def init_bit_count(a_line):
    map = {}
    for i, _ in enumerate(a_line.strip()):
        map[i] = {ZERO: 0, ONE: 0}

    return map


if __name__ == '__main__':
    input = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    print('Power consumption', get_power_consumption(input))