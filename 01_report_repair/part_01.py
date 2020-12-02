from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_01():
    found = 0
    with open(INPUT_FILE, 'r') as input_file:
        rows = input_file.readlines()
        for left_operand in rows:
            for right_operand in rows:
                if (left := int(left_operand)) + (right := int(right_operand)) == 2020:
                    print(f'{left} + {right} = 2020\n{left} * {right} = {left * right}')
                    found += 1
    if not found:
        print('no two rows adding up to 2020 found :(')


if __name__ == '__main__':
    part_01()
