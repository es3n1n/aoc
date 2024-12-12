from collections import defaultdict

from aoc import *


aoc_setup(2024, 8)

antennas = defaultdict(list)
grid = list(day_input_lines())
max_x = len(grid[0]) - 1
max_y = len(grid) - 1

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char != '.':
            antennas[char].append(x + 1j * y)

pt1 = set()
for positions in antennas.values():
    for i, ant1 in enumerate(positions):
        for ant2 in positions[i + 1 :]:
            diff = ant1 - ant2

            for potential in [ant1 + diff, ant2 - diff, ant1 - diff * 2, ant2 + diff * 2]:
                x, y = int(potential.real), int(potential.imag)

                if 0 <= x <= max_x and 0 <= y <= max_y:
                    pt1.add(potential)

pt2 = set()
for positions in antennas.values():
    for i, ant1 in enumerate(positions):
        for ant2 in positions[i + 1 :]:
            diff = ant1 - ant2
            for j in range(-100, 100):
                potential = ant1 + diff * j

                x, y = int(potential.real), int(potential.imag)
                if 0 <= x <= max_x and 0 <= y <= max_y:
                    pt2.add(potential)

answer(1, len(pt1), auto_submit=True)
expect_demo_answer(1, 14)
answer(2, len(pt2), auto_submit=True)
expect_demo_answer(2, 34)
