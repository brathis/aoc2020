from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def _get_visible_occupied_seat_count(row_idx, col_idx, grid):
    h = len(grid)
    w = len(grid[0])
    occupied_count = 0

    def _idx_is_valid(r_idx, c_idx):
        return 0 <= r_idx <= h - 1 and 0 <= c_idx <= w - 1

    for d_x in [-1, 0, 1]:
        for d_y in [-1, 0, 1]:
            if d_x == d_y == 0:
                continue
            x, y = col_idx + d_x, row_idx + d_y
            while _idx_is_valid(y, x):
                if grid[y][x] == '#':
                    occupied_count += 1
                    break
                if grid[y][x] == 'L':
                    break
                x += d_x
                y += d_y

    return occupied_count


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        grid = [l.strip() for l in input_file.readlines()]

    while True:
        for row in grid:
            print(row)
        print('-' * len(grid[0]))

        next_grid = []
        for row_idx, row in enumerate(grid):
            next_row = ''
            for col_idx, col in enumerate(row):
                if col == 'L' and _get_visible_occupied_seat_count(row_idx, col_idx, grid) == 0:
                    next_row += '#'
                elif col == '#' and _get_visible_occupied_seat_count(row_idx, col_idx, grid) >= 5:
                    next_row += 'L'
                else:
                    next_row += col
            next_grid.append(next_row)

        # Detect steady state.
        if next_grid == grid:
            break

        grid = next_grid

    occupied_seat_count = sum([len([c for c in row if c == '#']) for row in grid])
    print(f'{occupied_seat_count=}')


if __name__ == '__main__':
    part_02()
