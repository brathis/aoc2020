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


def _recurse(rules, containing_bag_type, bag_type):
    # The number of bags of a certain type contained in a "rule" is equal to the number of bags of that type directly specified by the rule,
    # plus the number of bags of that type contained in bags of other types, multiplied by their respective quantities.
    ret = 0
    rule = rules[containing_bag_type]
    for child_bag_type, quantity in rule.items():
        if child_bag_type == bag_type:
            ret += quantity
        else:
            ret += quantity * _recurse(rules, child_bag_type, bag_type)
    return ret


def part_01():
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

    # Traverse the tree and count the number of occurrences of "shiny gold" bags.
    bag_count = 0
    for bag_type in rules.keys():
        if _recurse(rules, bag_type, "shiny gold") > 0:
            bag_count += 1
    print(f'{bag_count} bag colors can eventually contain shiny gold bags')


if __name__ == '__main__':
    part_01()
