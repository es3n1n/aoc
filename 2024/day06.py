from tqdm import trange

from aoc import *


aoc_setup(2024, 6)
pt1 = 0
pt2 = 0

start_pos: tuple[int, int] | None = None
the_map = []

for i, line in enumerate(day_input_lines(stripped=True)):
    row = list(line)
    the_map.append(row)

    if start_pos is None and '^' in row:
        start_pos = (i, row.index('^'))

if not start_pos:
    raise ValueError


def in_range(x: int, min_v: int, max_v: int) -> bool:
    return min_v <= x < max_v


directions = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
}


def simulate_guard(current_map: list[list[str]], coords: list[int], *, track_visited: bool = True) -> bool | int:
    direction = 'u'
    visited: set[tuple[int, int, str] | tuple[int, int]] = set()
    count = 0

    while True:
        if track_visited:
            pos = (coords[0], coords[1])
            if pos not in visited:
                count += 1
                visited.add(pos)
        else:
            state = (coords[0], coords[1], direction)
            if state in visited:
                return True
            visited.add(state)

        next_c = coords.copy()
        next_c[0] += directions[direction][0]
        next_c[1] += directions[direction][1]

        if next_c[0] < 0 or next_c[0] >= len(current_map) or next_c[1] < 0 or next_c[1] >= len(current_map[0]):
            return count if track_visited else False

        if current_map[next_c[0]][next_c[1]] == '#':
            direction = {
                'u': 'r',
                'r': 'd',
                'd': 'l',
                'l': 'u',
            }[direction]
            continue

        coords = next_c


pt1 = simulate_guard(the_map, list(start_pos), track_visited=True)

for i in trange(len(the_map), desc='pt2'):
    for j in range(len(the_map[0])):
        if the_map[i][j] != '.' or [i, j] == list(start_pos):
            continue

        test_map = [row.copy() for row in the_map]
        test_map[i][j] = '#'

        if simulate_guard(test_map, list(start_pos), track_visited=False):
            pt2 += 1

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 41)
answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 6)
