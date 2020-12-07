from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def _consume_bag_spec(tokens):
    # First token must be either:
    # - 'no' -> consume 3 tokens ("no", "other", "bags")
    # - a digit -> consume 4 tokens (<digit>, <color>, <color>, "bags?.?")
    if tokens[0] == 'no':
        return tokens[3:], None, None
    return tokens[4:], f'{tokens[1]} {tokens[2]}', int(tokens[0])


def _get_num_children(rules, bag_color):
    rule = rules[bag_color]
    if len(rule) == 0:
        return 0
    ret = 0
    for color, count in rule.items():
        ret += count * (1 + _get_num_children(rules, color))
    return ret


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [line.strip() for line in input_file.readlines()]

    # Parse the rules.
    # I couldn't do it with regex :(
    rules = {}
    for line in lines:
        tokens = line.split()
        bag_color = f'{tokens[0]} {tokens[1]}'
        tokens = tokens[4:]
        rule = {}
        while len(tokens) >= 3:
            tokens, color, num = _consume_bag_spec(tokens)
            if color is None:
                break
            rule[color] = num
        rules[bag_color] = rule

    print(f'a shiny gold bag contains {_get_num_children(rules, "shiny gold")} bags')


if __name__ == '__main__':
    part_02()
