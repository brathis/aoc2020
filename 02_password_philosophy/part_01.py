from __future__ import annotations

import os.path
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
PASSWORD_REGEX = r'^(?P<min_occ>\d+)-(?P<max_occ>\d+) (?P<char>\w): (?P<password>\w+)'


def part_01():
    valid_passwords = []
    with open(INPUT_FILE, 'r') as input_file:
        for row in input_file.readlines():
            if (match := re.match(PASSWORD_REGEX, row)) is not None:
                # Count the occurrences of the specified character.
                char_count = len([c for c in match.group('password') if c == match.group('char')])
                if int(match.group('min_occ')) <= char_count <= int(match.group('max_occ')):
                    valid_passwords.append(match.group('password'))
            else:
                print(f'error: row does not match regex: {row}')
                return

    print(f'{len(valid_passwords)} passwords are valid')


if __name__ == '__main__':
    part_01()
