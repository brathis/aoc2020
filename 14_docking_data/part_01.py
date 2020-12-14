from __future__ import annotations

import os.path
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
MASK_LINE = r'^mask = ((1|0|X){36})$'
MEM_LINE = r'^mem\[(\d+)\] = (\d+)$'


def part_01():
    memory = {}
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]

    mask_ones = None
    mask_zeros = None

    for line in lines:

        if (match := re.fullmatch(MASK_LINE, line)) is not None:
            mask_raw = match.group(1)
            mask_ones = int(''.join([('1' if b == '1' else '0') for b in mask_raw]), base=2)
            mask_zeros = int(''.join([('0' if b == '0' else '1') for b in mask_raw]), base=2)

        elif (match := re.fullmatch(MEM_LINE, line)) is not None:
            memory_location = int(match.group(1))
            memory_value = int(match.group(2))
            # Apply bit masks
            memory_value |= mask_ones
            memory_value &= mask_zeros
            memory[memory_location] = memory_value

    print(sum(memory.values()))


if __name__ == '__main__':
    part_01()
