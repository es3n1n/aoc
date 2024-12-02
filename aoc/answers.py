from typing import Any

from .context import aoc_context
from .logger import crit, error, info


stored_answers: dict[int, Any] = {}


def answer(part_num: int, value: Any) -> None:
    if part_num in stored_answers:
        crit(f'already have an answer for {part_num = }')

    info(f'answer {part_num} = {value}')
    stored_answers[part_num] = value


def expect_answer(part_num: int, value: Any, *, for_demo: bool = False) -> None:
    if for_demo != aoc_context.is_demo:
        return

    got_value = stored_answers.get(part_num)
    if value == got_value:
        # Don't log anything if check passed
        return

    error(f'answer {part_num} check failed; expected {value}, got {got_value}')
