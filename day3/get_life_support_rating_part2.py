import os

from get_lines import get_lines


def count_occurrences_at_pos(lines: [str], pos: int) -> {'0': int, '1': int}:
    count = {'0': 0, '1': 0}
    for line in lines:
        count[line[pos]] += 1
    return count


def get_most_common_bit_at_pos(lines: [str], pos: int) -> str:
    occurences = count_occurrences_at_pos(lines, pos)
    return '0' if occurences['0'] > occurences['1'] else '1'


def get_least_common_bit_at_pos(lines: [str], pos: int) -> str:
    occurences = count_occurrences_at_pos(lines, pos)
    return '1' if occurences['1'] < occurences['0'] else '0'


def is_bit_at_pos_equals_to(line: [str], pos: int, bit_to_filter: str):
    return line[pos] == bit_to_filter


def get_remaining_line_value_matching(lines_to_filter: [str], get_bit_to_filter_function):
    bit_pos = 0
    while len(lines_to_filter) > 1:
        bit_to_check = get_bit_to_filter_function(lines_to_filter, bit_pos)
        lines_to_filter = list(filter(lambda a_line: is_bit_at_pos_equals_to(a_line, bit_pos,
                                      bit_to_check),
                                      lines_to_filter))
        bit_pos += 1

    return int(lines_to_filter[0], 2)


def get_life_support_rating(input: str):
    lines = get_lines(input)
    oxygen = get_remaining_line_value_matching(lines, get_most_common_bit_at_pos)
    co2 = get_remaining_line_value_matching(lines, get_least_common_bit_at_pos)

    print('oxygen', oxygen)
    print('co2', co2)

    return co2 * oxygen


if __name__ == '__main__':
    input = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    print('Life support rating', get_life_support_rating(input))
