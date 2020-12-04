from __future__ import annotations

import os.path
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
FIELD_REGEX = r'^(\w{3}):(\S+)'
REQUIRED_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]


def part_01():
    passport_data = []
    passport_data_item = None
    valid_count = 0
    with open(INPUT_FILE, 'r') as input_file:
        for row in input_file.readlines():
            # Read the row into passport_data_item, if the latter is None.
            if passport_data_item is None and row.strip() != '':
                passport_data_item = row
            elif row.strip() == '':
                # An empty row denotes the end of a passport.
                passport_data.append(passport_data_item)
                passport_data_item = None
            else:
                # The row is still part of the current passport.
                passport_data_item += row
        # There may not be a blank line after the last passport.
        if passport_data_item is not None:
            passport_data.append(passport_data_item)
    print(f'read {len(passport_data)} passports')

    for passport in passport_data:
        # Split the passport data into fields.
        fields = [f for f in re.split(r'( |\n)', passport) if f not in ['', ' ', '\n']]
        field_map = {}
        for field in fields:
            if match := re.match(FIELD_REGEX, field):
                field_map[match.group(1)] = match.group(2)
            else:
                raise ValueError(f'field >{field}< did not match pattern')

        # Check if the passport contains all valid fields.
        valid = True
        for req_field in REQUIRED_FIELDS:
            if req_field not in field_map:
                valid = False
                break
        if valid:
            valid_count += 1

    print(f'found {valid_count} valid passports')


if __name__ == '__main__':
    part_01()
