import re

from aoc import *


aoc_setup(2024, 3)

muls = [(m.start(), m[1], m[2]) for m in re.finditer(r'mul\((\d{1,3})\,(\d{1,3})\)', day_input())]
controls = [(m.start(), m.group()) for m in re.finditer(r'(?:do|don\'t)\(\)', day_input())]

pt1 = 0
pt2 = 0
i = 0
enabled = True

for start, lhs, rhs in muls:
    pt1 += int(lhs) * int(rhs)

    while i < len(controls) and controls[i][0] < start:
        enabled = controls[i][1] == 'do()'
        i += 1

    if enabled:
        pt2 += int(lhs) * int(rhs)

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 161)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 48)
