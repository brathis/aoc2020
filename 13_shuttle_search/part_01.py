from __future__ import annotations

import math
import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_01():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    earliest_timestamp = int(lines[0])
    print(f'earliest departure at {earliest_timestamp}')
    bus_services = [int(s) for s in lines[1].split(',') if s != 'x']
    earliest_bus_interval, min_delay = None, None
    for interval in bus_services:
        iteration = math.ceil(earliest_timestamp / interval)
        time = iteration * interval
        delay = time - earliest_timestamp
        print(f'Bus #{interval} leaves at {time} ({delay} minutes after earliest time)')
        if min_delay is None or delay < min_delay:
            min_delay = delay
            earliest_bus_interval = interval

    print(f'best option: bus #{earliest_bus_interval} with {min_delay} minutes wait, solution: {earliest_bus_interval * min_delay}')


if __name__ == '__main__':
    part_01()
