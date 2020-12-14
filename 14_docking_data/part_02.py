from __future__ import annotations

import os.path
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
MASK_LINE = r'^mask = ((1|0|X){36})$'
MEM_LINE = r'^mem\[(\d+)\] = (\d+)$'


def _generate_addresses(address: str):
    if (offset := address.find('X', 0)) != -1:
        address_mod_0 = ''.join([('0' if i == offset else c) for i, c in enumerate(address)])
        yield from _generate_addresses(address_mod_0)
        address_mod_1 = ''.join([('1' if i == offset else c) for i, c in enumerate(address)])
        yield from _generate_addresses(address_mod_1)
    else:
        yield int(address, base=2)


def part_02():
    memory = {}
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]

    mask_raw = None

    for line in lines:

        if (match := re.fullmatch(MASK_LINE, line)) is not None:
            mask_raw = match.group(1)

        elif (match := re.fullmatch(MEM_LINE, line)) is not None:
            memory_address = int(match.group(1))
            memory_value = int(match.group(2))

            addr = ''
            for a, m in zip(f'{memory_address:036b}', mask_raw):
                if m == '1':
                    addr += '1'
                elif m == 'X':
                    addr += 'X'
                else:
                    addr += a

            for address in _generate_addresses(addr):
                memory[address] = memory_value

    print(sum(memory.values()))


if __name__ == '__main__':
    part_02()
