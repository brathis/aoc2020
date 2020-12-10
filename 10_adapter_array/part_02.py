from __future__ import annotations

import functools
import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
cache = {}


@functools.lru_cache
def _get_number_of_combinations(current_rating, adapter_joltage_ratings, target):
    """
    Since there is enormous overlap between sub-paths, caching the results saves us orders of magnitude in computational effort.
    :param current_rating: the rating of the current adapter
    :param adapter_joltage_ratings: the rating of the remaining adapters
    :param target: the rating of the device
    :return: the number of combinations from the current adapter to the device using the remaining adapters
    """
    if len(adapter_joltage_ratings) == 0 or max(adapter_joltage_ratings) <= current_rating:
        return 0
    combinations = 0
    for next_rating in range(current_rating + 1, current_rating + 4):
        if next_rating in adapter_joltage_ratings:
            if next_rating == target:
                combinations += 1
            else:
                # Discard everything smaller than next_rating + 1
                next_adapter_joltage_ratings = tuple([r for r in adapter_joltage_ratings if r >= next_rating + 1])
                combinations += _get_number_of_combinations(next_rating, next_adapter_joltage_ratings, target)
    return combinations


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        adapter_joltage_ratings = [int(l) for l in input_file.readlines()]
    # The final device (the one to be charged) has a joltage rating of 3 more than the highest adapter joltage rating.
    adapter_joltage_ratings.append(max(adapter_joltage_ratings) + 3)
    adapter_joltage_ratings.sort()

    combinations = _get_number_of_combinations(0, tuple(adapter_joltage_ratings), max(adapter_joltage_ratings))
    print(f'found {combinations} combinations')


if __name__ == '__main__':
    part_02()
