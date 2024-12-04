from aoc import *


aoc_setup(2024, 4)
lines = day_input_lines()
lc = len(lines)
llc = len(lines[0])


def _check(s: str, val: str) -> bool:
    return s == val or s[::-1] == val


def get_string_in_direction(
    start_row: int, start_col: int, d_row: int, d_col: int, length: int
) -> tuple[str, set[tuple[int, int]]]:
    if not (0 <= start_row + (length - 1) * d_row < lc and 0 <= start_col + (length - 1) * d_col < llc):
        return '', set()

    string = []
    coords = set()
    for kk in range(length):
        r = start_row + kk * d_row
        c = start_col + kk * d_col

        string.append(lines[r][c])
        coords.add((r, c))
    return ''.join(string), coords


directions = (
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
)
seen_patterns = set()

pt1 = 0
for i in range(lc):
    for j in range(llc):
        for dr, dc in directions:
            s, coords = get_string_in_direction(i, j, dr, dc, 4)
            if not _check(s, 'XMAS'):
                continue

            pattern = frozenset(coords)
            if pattern in seen_patterns:
                continue

            seen_patterns.add(pattern)
            pt1 += 1

pt2 = 0
for i in range(1, lc - 1):
    for j in range(1, llc - 1):
        diags = (
            (
                get_string_in_direction(i - 1, j - 1, 1, 1, 3)[0],
                get_string_in_direction(i - 1, j + 1, 1, -1, 3)[0],
            ),
            (
                get_string_in_direction(i - 1, j + 1, 1, -1, 3)[0],
                get_string_in_direction(i - 1, j - 1, 1, 1, 3)[0],
            ),
        )

        if any(all(_check(s, 'MAS') for s in cross) for cross in diags):
            pt2 += 1

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 18)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 9)
