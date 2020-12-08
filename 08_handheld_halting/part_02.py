from __future__ import annotations

import os.path
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
INSTRUCTION_REGEX = r'^(?P<op>nop|acc|jmp) (?P<arg>(\+|-)\d+)$'


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    instructions = []
    candidate_pcs = []
    for i, line in enumerate(lines):
        match = re.fullmatch(INSTRUCTION_REGEX, line)
        instructions.append((match['op'], int(match['arg'])))
        if match['op'] in ['nop', 'jmp']:
            candidate_pcs.append(i)

    print(f'there are {len(candidate_pcs)} potentially corrupted instructions')

    for corrupted_pc in candidate_pcs:
        print(f'modifiying instruction at pc={corrupted_pc}')
        acc = 0
        pc = 0
        pc_seen = set()
        while True:
            try:
                instruction = lines[pc]
            except IndexError:
                print(f'{pc=} out of bounds, halting. {acc=}')
                return
            if pc in pc_seen:
                print(f'fetched {pc=} a second time, terminating. {acc=}')
                break
            pc_seen.add(pc)
            match = re.fullmatch(INSTRUCTION_REGEX, instruction)
            if match:
                op = match['op']
                arg = int(match['arg'])

                if op == 'nop':
                    if pc == corrupted_pc:
                        print('changing nop -> jmp')
                        pc += arg
                    else:
                        pc += 1
                elif op == 'jmp':
                    if pc == corrupted_pc:
                        print('changing jmp -> nop')
                        pc += 1
                    else:
                        pc += arg
                elif op == 'acc':
                    acc += arg
                    pc += 1
                else:
                    raise ValueError(f'unknown operation "{op}"')

            else:
                raise ValueError(f'"{instruction}" does not match regex')


if __name__ == '__main__':
    part_02()
