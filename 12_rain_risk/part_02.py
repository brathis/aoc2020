from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    x, y = 0, 0
    wp_x, wp_y = 10, -1
    for line in lines:
        inst = line[0]
        arg = int(line[1:])
        if inst == 'N':
            wp_y -= arg
        elif inst == 'E':
            wp_x += arg
        elif inst == 'S':
            wp_y += arg
        elif inst == 'W':
            wp_x -= arg
        elif inst == 'R':
            for _ in range(arg // 90):
                wp_x, wp_y = -wp_y, wp_x
        elif inst == 'L':
            for _ in range(arg // 90):
                wp_x, wp_y = wp_y, -wp_x
        elif inst == 'F':
            x += arg * wp_x
            y += arg * wp_y
        else:
            raise ValueError(f'unknown instruction {inst}')

    print(f'solution={abs(x) + abs(y)}')


if __name__ == '__main__':
    part_02()
