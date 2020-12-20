from __future__ import annotations

import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
NUM_ITER = 6


def _get_neighbors(x, y, z):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                neighbor = (x + dx, y + dy, z + dz)
                if neighbor != (x, y, z):
                    yield neighbor


def part_01():
    active_cubes = set()
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]

    # Load the initial state (z=0).
    for y, line in enumerate(lines):
        for x, state in enumerate(line):
            if state == '#':
                active_cubes.add((x, y, 0))

    for _ in range(NUM_ITER):
        next_active_cubes = set()
        # First, determine which of the active cubes become inactive.
        for active_cube in active_cubes:
            # Count the active neighbors.
            num_active_neighbors = 0
            for neighbor in _get_neighbors(*active_cube):
                if neighbor in active_cubes:
                    num_active_neighbors += 1
            # If it has 2 or 3 active neighbors, it stays active. Otherwise, it becomes inactive.
            if num_active_neighbors in [2, 3]:
                next_active_cubes.add(active_cube)

        # Next, determine the set of inactive cubes which might become active with the next iteration.
        # For now, create a box which contains all of the active cubes.
        min_x, min_y, min_z = None, None, None
        max_x, max_y, max_z = None, None, None
        for x, y, z in active_cubes:
            if min_x is None or x < min_x:
                min_x = x
            if min_y is None or y < min_y:
                min_y = y
            if min_z is None or z < min_z:
                min_z = z
            if max_x is None or x > max_x:
                max_x = x
            if max_y is None or y > max_y:
                max_y = y
            if max_z is None or z > max_z:
                max_z = z

        inactive_cubes = set()
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    inactive_cubes.add((x, y, z))

        # Count the active neighbors.
        for inactive_cube in inactive_cubes:
            num_active_neighbors = 0
            for neighbor in _get_neighbors(*inactive_cube):
                if neighbor in active_cubes:
                    num_active_neighbors += 1
            # If the cube has exactly 3 active neighbors, it becomes active. Otherwise, it becomes inactive.
            if num_active_neighbors == 3:
                next_active_cubes.add(inactive_cube)

        active_cubes = next_active_cubes
        print(f'{len(active_cubes)=}')


if __name__ == '__main__':
    part_01()
