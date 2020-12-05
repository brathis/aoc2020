from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_02():
    scanned_seat_ids = set()
    remaining_seat_ids = set(range(2 ** 10))  # Contains the seats which have not been scanned.
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file.readlines():
            seat_id = int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), base=2)
            scanned_seat_ids.add(seat_id)
            remaining_seat_ids.remove(seat_id)

    for seat_id in remaining_seat_ids:
        # Our seat is the one which has not been scanned (i.e. which is in the `remaining_seat_ids` set)
        # but for which both neighbors (i.e. those with a seat id off by 1) are in the `scanned_seat_ids` set.
        if seat_id + 1 in scanned_seat_ids and seat_id - 1 in scanned_seat_ids:
            print(f'found seat: {seat_id=}')


if __name__ == '__main__':
    part_02()
