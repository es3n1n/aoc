from collections import defaultdict

from aoc import *


aoc_setup(2024, 1, is_demo=False)

lv: list[int] = []
rv: list[int] = []
rc: defaultdict[int, int] = defaultdict(int)

for a, b in day_input_lines_ints():
    lv.append(a)
    rv.append(b)
    rc[b] += 1

answer(1, sum(abs(a - b) for a, b in zip(sorted(lv), sorted(rv), strict=False)))
expect_demo_answer(1, 11)

answer(2, sum(x * rc[x] for x in lv))
expect_demo_answer(2, 31)
