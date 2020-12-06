from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        lines = input_file.readlines()
    group_dicts = []
    group_dict = {}
    group_sizes = []
    group_size = 0
    for line in lines:
        line = line.strip()
        # A blank line starts a new group.
        if line == '':
            group_dicts.append(group_dict)
            group_dict = {}
            group_sizes.append(group_size)
            group_size = 0
        # Otherwise, add each character to the dict of the group.
        else:
            group_size += 1
            for c in line:
                if c in group_dict:
                    group_dict[c] += 1
                else:
                    group_dict[c] = 1
    # Add the last group.
    group_dicts.append(group_dict)
    group_sizes.append(group_size)

    total = 0
    for group_dict, group_size in zip(group_dicts, group_sizes):
        answers_chosen_by_everyone = len([a for a in group_dict.values() if a == group_size])
        total += answers_chosen_by_everyone
    print(f'{total=}')


if __name__ == '__main__':
    part_02()
