from aoc import *


aoc_setup(2024, 4)

pt1 = 0
pt2 = 0

lines = day_input_lines()
lc = len(lines)
seen_patterns = set()


def _check(s: str, val: str) -> bool:
    return any(
        x == val
        for x in (
            s,
            s[::-1],
        )
    )


def is_xmas(s: str) -> bool:
    return _check(s, 'XMAS')


def is_mas(s: str) -> bool:
    return _check(s, 'MAS')


for i in range(lc):
    for j in range(len(lines[i])):
        if j + 3 < len(lines[i]):
            s = ''.join(lines[i][j : j + 4])
            if is_xmas(s):
                pattern = frozenset((i, j + k) for k in range(4))
                if pattern not in seen_patterns:
                    seen_patterns.add(pattern)
                    pt1 += 1

        if i >= 3:
            s = ''.join(lines[i - k][j] for k in range(4))
            if is_xmas(s):
                pattern = frozenset((i - k, j) for k in range(4))
                if pattern not in seen_patterns:
                    seen_patterns.add(pattern)
                    pt1 += 1

        if i <= (lc - 4):
            s = ''.join(lines[i + k][j] for k in range(4))
            if is_xmas(s):
                pattern = frozenset((i + k, j) for k in range(4))
                if pattern not in seen_patterns:
                    seen_patterns.add(pattern)
                    pt1 += 1

        if (i + 3) < lc and (j + 3) < len(lines[i]):
            s = ''.join(lines[i + k][j + k] for k in range(4))
            if is_xmas(s):
                pattern = frozenset((i + k, j + k) for k in range(4))
                if pattern not in seen_patterns:
                    seen_patterns.add(pattern)
                    pt1 += 1

        if (i + 3) < lc and j >= 3:
            s = ''.join(lines[i + k][j - k] for k in range(4))
            if is_xmas(s):
                pattern = frozenset((i + k, j - k) for k in range(4))
                if pattern not in seen_patterns:
                    seen_patterns.add(pattern)
                    pt1 += 1

        if i >= 3 and (j + 3) < len(lines[i]):
            s = ''.join(lines[i - k][j + k] for k in range(4))
            if is_xmas(s):
                pattern = frozenset((i - k, j + k) for k in range(4))
                if pattern not in seen_patterns:
                    seen_patterns.add(pattern)
                    pt1 += 1

        if i >= 3 and j >= 3:
            s = ''.join(lines[i - k][j - k] for k in range(4))
            if is_xmas(s):
                pattern = frozenset((i - k, j - k) for k in range(4))
                if pattern not in seen_patterns:
                    seen_patterns.add(pattern)
                    pt1 += 1


for i in range(1, lc - 1):
    for j in range(1, len(lines[i]) - 1):
        c1 = all(
            is_mas(x)
            for x in (
                ''.join(lines[i - 1 + k][j - 1 + k] for k in range(3)),
                ''.join(lines[i - 1 + k][j + 1 - k] for k in range(3)),
            )
        )
        c2 = all(
            is_mas(x)
            for x in (
                ''.join(lines[i - 1 + k][j + 1 - k] for k in range(3)),
                ''.join(lines[i - 1 + k][j - 1 + k] for k in range(3)),
            )
        )

        if c1 or c2:
            pt2 += 1

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 18)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 9)
