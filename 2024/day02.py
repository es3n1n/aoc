from aoc import *


aoc_setup(2024, 2)


def unsafe_counter(params: list[int]) -> int:
    result = 0
    is_dec = False
    for i in range(1, len(params)):
        if result > 1:
            break
        p, c = params[i - 1 : i + 1]
        cur_dec = c < p
        if i != 1 and is_dec != cur_dec:
            result += 1
            continue
        if i == 1:
            is_dec = cur_dec
        diff = abs(p - c)
        if diff == 0 or diff > 3:
            result += 1
            continue
    return result


def unsafe_forgiving_counter(params: list[int]) -> int:
    if unsafe_counter(params) == 0:
        return 0

    for i in range(len(params)):
        if unsafe_counter(params[:i] + params[i + 1 :]) == 0:
            return 1

    return 999


pt1 = 0
pt2 = 0
for ints in day_input_lines_ints():
    c = unsafe_forgiving_counter(ints)
    if c == 0:
        pt1 += 1
        pt2 += 1
    elif c == 1:
        pt2 += 1

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 2)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 4)
