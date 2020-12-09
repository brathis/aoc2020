from __future__ import annotations

import collections
import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_01():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    dictionary = collections.deque(maxlen=25)
    for line in lines:
        if len(dictionary) < dictionary.maxlen:
            # We're still in the preamble
            pass
        else:
            # We're in the actual message.
            # Calculate all possible sums of two elements in the dictionary by brute force.
            dict_set = set(dictionary)
            found = False
            for summand in dict_set:
                remainder_set = dict_set.difference([summand])
                sums = [summand + r for r in remainder_set]
                if int(line) in sums:
                    print(f'{line} = {summand} + {int(line) - summand}')
                    found = True
                    break
            if not found:
                print(f'{line} is not valid')
                return
        dictionary.append(int(line))


if __name__ == '__main__':
    part_01()
