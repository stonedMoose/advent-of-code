#!/usr/bin/env python3
import os


def get_depth_increase_count():
    depths = compute_depth_windows()

    return count_depth_increase(depths)


def count_depth_increase(depths):
    previous = None
    count = 0
    for depth in depths:
        if previous is not None and previous < depth:
            count += 1
        previous = depth
    return count


def compute_depth_windows():
    window1 = []
    window2 = []
    window3 = []
    window4 = []
    depths = []
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt'), 'r') as file:
        lines = file.readlines()
        length = len(lines)

        for i in range(length):
            add_to_list_if_exists(i, lines, window1, length)
            add_to_list_if_exists(i + 1, lines, window2, length)
            add_to_list_if_exists(i + 2, lines, window3, length)
            add_to_list_if_exists(i + 3, lines, window4, length)

            window1 = reset_window_adding_sum_to_depth_if_completed(depths, window1)
            window2 = reset_window_adding_sum_to_depth_if_completed(depths, window2)
            window3 = reset_window_adding_sum_to_depth_if_completed(depths, window3)
            window4 = reset_window_adding_sum_to_depth_if_completed(depths, window4)

    return depths


def reset_window_adding_sum_to_depth_if_completed(depths, window1):
    if len(window1) == 3:
        depths.append(sum(window1))
        return []
    return window1


def add_to_list_if_exists(i, lines, window, length):
    if i < length:
        window.append(int(lines[i].strip()))


if __name__ == '__main__':
    print(get_depth_increase_count())
