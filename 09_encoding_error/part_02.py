from __future__ import annotations

import collections
import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
TARGET = 1721308972


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    # We solve this by back-tracking.
    # Starting at index 0, sum up successive numbers in the list. If the sum is equal to the target, we've found the solution. Otherwise,
    # if the sum becomes larger than the target, we know that we can't be on the right track and abort the iteration.
    for i in range(len(lines)):
        cumulative_sum = 0
        summand_range = []
        for j in range(i, len(lines)):
            cumulative_sum += int(lines[j])
            summand_range.append(int(lines[j]))
            if cumulative_sum == TARGET:
                print(f'found target: {summand_range}, solution: {min(summand_range) + max(summand_range)}')
                return
            elif cumulative_sum > TARGET:
                print(f'cumulative sum {cumulative_sum} > {TARGET}, aborting')


if __name__ == '__main__':
    part_02()
