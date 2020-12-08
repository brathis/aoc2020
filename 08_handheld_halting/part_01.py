from __future__ import annotations

import os.path
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
INSTRUCTION_REGEX = r'^(?P<op>nop|acc|jmp) (?P<arg>(\+|-)\d+)$'


def part_01():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    acc = 0
    pc = 0
    pc_seen = set()
    while True:
        try:
            instruction = lines[pc]
        except IndexError:
            print(f'{pc=} out of bounds, terminating.')
            break
        print(f'{pc=} {acc=}')
        if pc in pc_seen:
            print(f'fetched {pc=} a second time, terminating. {acc=}')
            break
        pc_seen.add(pc)
        match = re.fullmatch(INSTRUCTION_REGEX, instruction)
        if match:
            op = match['op']
            arg = int(match['arg'])

            if op == 'nop':
                pc += 1
            elif op == 'jmp':
                pc += arg
            elif op == 'acc':
                acc += arg
                pc += 1
            else:
                raise ValueError(f'unknown operation "{op}"')

        else:
            raise ValueError(f'"{instruction}" does not match regex')


if __name__ == '__main__':
    part_01()
