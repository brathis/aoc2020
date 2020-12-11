from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
NUM_ITER = 1


def _get_neighboring_indices(row_idx, col_idx, w, h):
    has_nb_above = row_idx > 0  # seat has neighbors above
    has_nb_below = row_idx < h - 1  # seat has neighbors below
    has_nb_left = col_idx > 0  # seat has neighbors to the left
    has_nb_right = col_idx < w - 1  # seat has neighbors to the right
    # There is a total of 8 separate cases to be distinguished.
    neighbors = []
    if has_nb_above:
        neighbors.append((row_idx - 1, col_idx))
        if has_nb_left:
            neighbors.append((row_idx - 1, col_idx - 1))
        if has_nb_right:
            neighbors.append((row_idx - 1, col_idx + 1))
    if has_nb_below:
        neighbors.append((row_idx + 1, col_idx))
        if has_nb_left:
            neighbors.append((row_idx + 1, col_idx - 1))
        if has_nb_right:
            neighbors.append((row_idx + 1, col_idx + 1))
    if has_nb_left:
        neighbors.append((row_idx, col_idx - 1))
    if has_nb_right:
        neighbors.append((row_idx, col_idx + 1))
    return neighbors


def _get_occupied_neighboring_indices(row_idx, col_idx, grid):
    h = len(grid)
    w = len(grid[0])
    return [(r, c) for (r, c) in _get_neighboring_indices(row_idx, col_idx, w, h) if grid[r][c] == '#']


def part_01():
    with open(INPUT_FILE, 'r') as input_file:
        grid = [l.strip() for l in input_file.readlines()]

    while True:
        for row in grid:
            print(row)
        print('------------------')

        next_grid = []
        for row_idx, row in enumerate(grid):
            next_row = ''
            for col_idx, col in enumerate(row):
                if col == 'L' and len(_get_occupied_neighboring_indices(row_idx, col_idx, grid)) == 0:
                    next_row += '#'
                elif col == '#' and len(_get_occupied_neighboring_indices(row_idx, col_idx, grid)) >= 4:
                    next_row += 'L'
                else:
                    next_row += col
            next_grid.append(next_row)

        if next_grid == grid:
            print(f'steady state reached!')
            break

        grid = next_grid

    occupied_seat_count = 0
    for row in grid:
        occupied_seat_count += len([c for c in row if c == '#'])
    print(f'{occupied_seat_count=}')


if __name__ == '__main__':
    part_01()
