from collections import defaultdict

from aoc import *


aoc_setup(2024, 5)
pt1 = 0
pt2 = 0

orders_after: defaultdict[int, list[int]] = defaultdict(list)


def find_invalid(ns: list[int]) -> list[tuple[int, int]]:
    misplaced = []
    for i, n in enumerate(ns):
        prevs = ns[:i]
        for x in orders_after.get(n, []):
            if x not in prevs:
                continue
            misplaced.append((i, x))
    return misplaced


parsing_commands = False
for line in day_input_lines():
    if not line:
        continue

    if not parsing_commands:
        if '|' in line:
            lv, rv = list(map(int, line.split('|')))
            orders_after[lv].append(rv)
            continue
        parsing_commands = True

    ns = list(map(int, line.split(',')))
    misplaced = find_invalid(ns)

    if not misplaced:
        pt1 += ns[len(ns) // 2]
        continue

    while misplaced := find_invalid(ns):
        for misplaced_i, wanted in misplaced:
            got = ns[misplaced_i]
            ii = ns.index(wanted)
            ns[ii] = got
            ns[misplaced_i] = wanted

    pt2 += ns[len(ns) // 2]

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 143)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 123)
