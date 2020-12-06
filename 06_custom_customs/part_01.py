from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_01():
    with open(INPUT_FILE, 'r') as input_file:
        lines = input_file.readlines()
    group_sets = []
    group_set = set()
    for line in lines:
        line = line.strip()
        # A blank line starts a new group.
        if line == '':
            group_sets.append(group_set)
            group_set = set()
        # Otherwise, add each character to the set of the group.
        else:
            for c in line:
                group_set.add(c)
    # Add the last group.
    group_sets.append(group_set)

    total = sum([len(group_set) for group_set in group_sets])
    print(f'{total=}')


if __name__ == '__main__':
    part_01()
