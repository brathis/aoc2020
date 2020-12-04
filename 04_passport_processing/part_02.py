from __future__ import annotations

import os.path
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
FIELD_REGEX = r'^(\w{3}):(\S+)'
REQUIRED_FIELDS = {
    'byr': r'^(\d{4})$',
    'iyr': r'^(\d{4})$',
    'eyr': r'^(\d{4})$',
    'hgt': r'^(\d+)(cm|in)$',
    'hcl': r'^#[0-9a-f]{6}$',
    'ecl': r'^amb|blu|brn|gry|grn|hzl|oth$',
    'pid': r'^\d{9}$',
}
FIELD_CONSTRAINTS = {
    'byr': lambda match: 1920 <= int(match.group(1)) <= 2002,
    'iyr': lambda match: 2010 <= int(match.group(1)) <= 2020,
    'eyr': lambda match: 2020 <= int(match.group(1)) <= 2030,
    'hgt': lambda match: 150 <= int(match.group(1)) <= 193 if match.group(2) == 'cm' else 59 <= int(match.group(1)) <= 76,
}


def part_02():
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

        valid = True
        for req_field, req_field_pattern in REQUIRED_FIELDS.items():
            # Check if the passport contains all valid fields.
            if req_field not in field_map:
                print(f'passport is missing field "{req_field}"')
                valid = False
                break
            # Check if the field also matches the regex.
            if not (match := re.match(req_field_pattern, field_value := field_map[req_field])):
                print(f'"{field_value}" does not match pattern "{req_field_pattern}"')
                valid = False
                break
            # Validate additional constraints, if they exist.
            elif req_field in FIELD_CONSTRAINTS:
                if not FIELD_CONSTRAINTS[req_field](match):
                    print(f'"{field_value}" has failed constraint for field {req_field}')
                    valid = False
                    break

        if valid:
            valid_count += 1

    print(f'found {valid_count} valid passports')


if __name__ == '__main__':
    part_02()
