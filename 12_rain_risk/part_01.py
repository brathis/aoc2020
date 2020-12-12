from __future__ import annotations

import math
import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_01():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    x, y = 0, 0
    heading = 90
    for line in lines:
        inst = line[0]
        arg = int(line[1:])
        if inst == 'N':
            y -= arg
        elif inst == 'E':
            x += arg
        elif inst == 'S':
            y += arg
        elif inst == 'W':
            x -= arg
        elif inst == 'R':
            heading = (heading + arg) % 360
        elif inst == 'L':
            heading = (heading - arg) % 360
        elif inst == 'F':
            x += int(math.sin(heading / 180 * math.pi) * arg)
            y -= int(math.cos(heading / 180 * math.pi) * arg)
        else:
            raise ValueError(f'unknown instruction {inst}')

    print(f'solution={abs(x) + abs(y)}')


if __name__ == '__main__':
    part_01()
