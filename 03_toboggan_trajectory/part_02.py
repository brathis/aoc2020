from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
SLOPES = [
    (1, 1),
    (1, 3),  # down 1, right 3
    (1, 5),
    (1, 7),
    (2, 1),
]


def part_02():
    result = None
    for slope in SLOPES:
        with open(INPUT_FILE, 'r') as input_file:
            grid = input_file.readlines()
        # The row list also includes the trailing newline character.
        num_cols = len(grid[0]) - 1
        print(f'grid repeats every {num_cols} columns')
        tree_count = 0
        row_idx, col_idx = 0, 0
        while row_idx < len(grid):
            if grid[row_idx][col_idx] == '#':
                tree_count += 1
                print(f'({row_idx}, {col_idx}) -> TREE (total={tree_count})')
            # Move across grid according to the slope.
            # Grid is periodic along x-axis with period num_cols,
            # thus accessing (row_idx, num_cols + 2)
            # is equivalent to accessing (row_idx, 2)
            row_idx += slope[0]
            col_idx = (col_idx + slope[1]) % num_cols
        print(f'encountered {tree_count} trees')
        if result is None:
            result = tree_count
        else:
            result *= tree_count
        print(f'{result=}')


if __name__ == '__main__':
    part_02()
