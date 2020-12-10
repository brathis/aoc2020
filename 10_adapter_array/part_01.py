from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_01():
    with open(INPUT_FILE, 'r') as input_file:
        adapter_joltage_ratings = [0] + [int(l) for l in input_file.readlines()]
    # The final device (the one to be charged) has a joltage rating of 3 more than the highest adapter joltage rating.
    adapter_joltage_ratings.append(max(adapter_joltage_ratings) + 3)

    differences = []
    current_rating = adapter_joltage_ratings[0]
    while len(adapter_joltage_ratings) > 1:
        # Find an adapter with a rating of at most 3 more jolts than the current rating.
        next_adapter_rating_range = range(current_rating + 1, current_rating + 4)
        found = False
        for next_rating in next_adapter_rating_range:
            if next_rating in adapter_joltage_ratings:
                diff = next_rating - current_rating
                print(f'{current_rating}J -> {next_rating}J ({diff=})')
                differences.append(diff)
                current_rating = next_rating
                adapter_joltage_ratings.remove(next_rating)
                found = True
                break
        if not found:
            raise RuntimeError(f'{current_rating=} needs joltage range {next_adapter_rating_range}')

    diff_1 = len([d for d in differences if d == 1])
    diff_3 = len([d for d in differences if d == 3])
    print(f'{diff_1} * {diff_3} = {diff_1 * diff_3}')


if __name__ == '__main__':
    part_01()
