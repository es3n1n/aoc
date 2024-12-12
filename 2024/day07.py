from collections.abc import Iterator

from aoc import *


aoc_setup(2024, 7)
pt1 = 0
pt2 = 0


def brute(val: int, rhs: int, *others: int, with_concatenation: bool = False) -> Iterator[int]:
    if not others:
        yield val + rhs
        yield val * rhs
        if with_concatenation:
            yield int(str(val) + str(rhs))
        return

    yield from [
        *brute(val + rhs, *others, with_concatenation=with_concatenation),
        *brute(val * rhs, *others, with_concatenation=with_concatenation),
        *(
            brute(int(str(val) + str(rhs)), *others, with_concatenation=with_concatenation)
            if with_concatenation
            else ()
        ),
    ]


for line in day_input_lines():
    result, other = line.split(':')
    ns = list(map(int, other.strip().split()))

    should_check_pt1 = not aoc_context.is_demo or result in ('190', '3267', '292')
    should_check_pt2 = not aoc_context.is_demo or result in ('190', '3267', '292', '156', '7290', '192')

    if should_check_pt1 and int(result) in list(brute(*ns, with_concatenation=False)):
        pt1 += int(result)

    if should_check_pt2 and int(result) in list(brute(*ns, with_concatenation=True)):
        pt2 += int(result)

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 3749)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 11387)
