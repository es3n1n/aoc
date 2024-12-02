from collections import defaultdict

from aoc import *


aoc_setup(2024, 1, is_demo=False)

lv: list[int] = []
rv: list[int] = []
rc: defaultdict[int, int] = defaultdict(int)

for line in day_input_lines():
    a, b = map(int, line.split())
    lv.append(a)
    rv.append(b)
    rc[b] += 1

answer(1, sum(abs(a - b) for a, b in zip(sorted(lv), sorted(rv), strict=False)))
expect_answer(1, 11, for_demo=True)

answer(2, sum(x * rc[x] for x in lv))
expect_answer(2, 31, for_demo=True)
