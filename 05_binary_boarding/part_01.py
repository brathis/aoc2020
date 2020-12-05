from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_01():
    max_seat_id = None
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file.readlines():
            seat_id = int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), base=2)
            if max_seat_id is None or seat_id > max_seat_id:
                max_seat_id = seat_id

    print(f'{max_seat_id=}')


if __name__ == '__main__':
    part_01()
