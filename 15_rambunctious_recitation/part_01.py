from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

numbers = {}  # key: number, value: tuple of the last 2 iterations in which it was spoken
last_spoken_number = None


def _speak(number, i):
    global numbers
    global last_spoken_number

    last_spoken_number = number
    if number in numbers:
        numbers[number] = (numbers[number][1], i)
    else:
        numbers[number] = (None, i)
    print(number)


def part_01():
    global numbers
    global last_spoken_number

    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    starting_numbers = [int(n) for n in lines[0].split(',')]
    for i in range(2020):
        if i < len(starting_numbers):
            _speak(starting_numbers[i], i)
        else:
            last_number_occurrences = numbers[last_spoken_number]
            if last_number_occurrences[0] is None:
                _speak(0, i)
            else:
                _speak(last_number_occurrences[1] - last_number_occurrences[0], i)


if __name__ == '__main__':
    part_01()
