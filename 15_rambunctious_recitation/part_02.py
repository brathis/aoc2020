from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
NUM_IT = 30000000

numbers = {}  # key: number, value: tuple of the last 2 iterations in which it was spoken
last_spoken_number = None


def _speak(number, i, silent=True):
    global numbers
    global last_spoken_number

    last_spoken_number = number
    if number in numbers:
        numbers[number] = (numbers[number][1], i)
    else:
        numbers[number] = (None, i)
    if not silent:
        print(number)


def part_02():
    global numbers
    global last_spoken_number

    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    starting_numbers = [int(n) for n in lines[0].split(',')]
    for i in range(NUM_IT):
        last = i == NUM_IT - 1
        if i < len(starting_numbers):
            _speak(starting_numbers[i], i, not last)
        else:
            last_number_occurrences = numbers[last_spoken_number]
            if last_number_occurrences[0] is None:
                _speak(0, i, not last)
            else:
                _speak(last_number_occurrences[1] - last_number_occurrences[0], i, not last)


if __name__ == '__main__':
    part_02()
