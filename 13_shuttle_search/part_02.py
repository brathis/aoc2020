from __future__ import annotations

import math
import os.path


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def _euclid_extended(a, b):
    """
    Given a,b, return gcd,s,t such that gcd(a,b) = s * a + t * b
    """
    if a == 0:
        return b, 0, 1
    g, s_bm, t_bm = _euclid_extended(b % a, a)
    s = t_bm - (b // a) * s_bm
    t = s_bm
    return g, s, t


def part_02():
    with open(INPUT_FILE, 'r') as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    bus_ids = [None if i == 'x' else int(i) for i in lines[1].split(',')]
    constraints = []
    for delta, bus_id in enumerate(bus_ids):
        if bus_id is not None:
            # Each constraint is a congruence: t = (interval - delta) (mod interval)
            constraints.append(((bus_id - delta) % bus_id, bus_id))

    for (delta, interval) in constraints:
        # It turns out that all of the intervals in the data set are coprime.
        for _, other_interval in constraints:
            if other_interval != interval:
                assert math.gcd(interval, other_interval) == 1

    # Chinese remainder theorem.
    M = math.prod([i for _, i in constraints])
    t = 0
    for (a_i, m_i) in constraints:
        M_i = int(M / m_i)
        one, r_i, s_i = _euclid_extended(m_i, M_i)
        assert one == 1
        assert r_i * m_i + s_i * M_i == 1
        e_i = s_i * M_i
        assert e_i % m_i == 1
        t += e_i * a_i

    print(t % M)


if __name__ == '__main__':
    part_02()
