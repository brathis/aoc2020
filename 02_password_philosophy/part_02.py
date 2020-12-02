from __future__ import annotations

import os.path
import re

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
PASSWORD_REGEX = r'^(?P<pos_1>\d+)-(?P<pos_2>\d+) (?P<char>\w): (?P<password>\w+)'


def part_02():
    valid_passwords = []
    with open(INPUT_FILE, 'r') as input_file:
        for row in input_file.readlines():
            if (match := re.match(PASSWORD_REGEX, row)) is not None:
                # Check that exactly one of the two positions contains the specified character.
                if bool(match.group('password')[int(match.group('pos_1')) - 1] == match.group('char')) \
                        ^ bool(match.group('password')[int(match.group('pos_2')) - 1] == match.group('char')):
                    valid_passwords.append(match.group('password'))
            else:
                print(f'error: row does not match regex: {row}')
                return

    print(f'{len(valid_passwords)} passwords are valid')


if __name__ == '__main__':
    part_02()
