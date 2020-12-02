from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_02():
    found = 0
    with open(INPUT_FILE, 'r') as input_file:
        rows = input_file.readlines()
        for op_1 in rows:
            for op_2 in rows:
                for op_3 in rows:
                    if (int_1 := int(op_1)) + (int_2 := int(op_2)) + (int_3 := int(op_3)) == 2020:
                        print(f'{int_1} + {int_2} + {int_3} = 2020\n{int_1} * {int_2} * {int_3} = {int_1 * int_2 * int_3}')
                        found += 1
    if not found:
        print('no three rows adding up to 2020 found :(')


if __name__ == '__main__':
    part_02()
