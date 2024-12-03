import re
import sys
from collections.abc import Iterator
from platform import platform
from typing import Any

from .context import aoc_context
from .logger import crit, error, info, warn


def day_input() -> str:
    file_name = str(aoc_context.day)
    if aoc_context.is_demo:
        file_name += '.demo'

    cached_input_path = aoc_context.year_dir / 'inputs' / file_name
    if cached_input_path.exists():
        return cached_input_path.read_text('utf-8')

    cached_input_path.parent.mkdir(parents=True, exist_ok=True)

    if aoc_context.is_demo:
        keybind = 'Ctrl + D'
        if 'windows' in platform().lower():
            keybind = 'Ctrl + Z + Enter'
        warn(f'Missing demo data, please paste it here and press {keybind}')

        demo_data = ''
        for line in sys.stdin:
            demo_data += line

        cached_input_path.write_text(demo_data, 'utf-8')
        info('Saved demo data')
        return demo_data

    response = aoc_context.http_session.get(f'https://adventofcode.com/{aoc_context.year}/day/{aoc_context.day}/input')
    if response.status_code != 200:
        crit(f'Got {response.status_code} while trying to get the input for day {aoc_context.day}')

    cached_input_path.write_text(response.text)
    return response.text


def day_input_lines() -> list[str]:
    return day_input().splitlines()


def day_input_lines_ints(separator: str | None = None, max_split: int = -1) -> Iterator[list[int]]:
    for line in day_input_lines():
        yield list(map(int, line.split(sep=separator, maxsplit=max_split)))


def submit_answer(part: int, answer: Any, ignore_answers: list[int] | None = None) -> None:
    prefix = f'answer {part} ({answer})'

    if aoc_context.is_demo:
        warn(f'{prefix}: skipped (in demo)')
        return

    if ignore_answers and answer in ignore_answers:
        error(f'{prefix}: skipped (explicitly ignored)')
        return

    resp = aoc_context.http_session.post(
        f'https://adventofcode.com/{aoc_context.year}/day/{aoc_context.day}/answer',
        data={
            'level': str(part),
            'answer': str(answer),
        },
    )
    content = resp.text.lower()

    if resp.status_code != 200:
        error(f'{prefix}: rejected due to status_code != 200 ({resp.status_code})')
        return

    if 'did you already complete it' in content:
        warn(f'{prefix}: skipped (already solved)')
        return

    if "that's the right answer" in content:
        info(f'{prefix}: correct')
        return

    if 'you have to wait' in content:
        occ = re.findall(r'you have ([\w ]+) left to wait', resp.text)
        reason = 'too fast'
        if occ:
            reason = f'too fast, {occ[0]} left to wait'
        warn(f'{prefix}: rejected ({reason})')
        return

    error(f'{prefix}: wrong answer')
