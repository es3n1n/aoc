from .context import aoc_context
from .logger import msg


def aoc_setup(year: int, day: int, *, is_demo: bool = False) -> None:
    msg(f'Setting up for Dec {day} {year}; {is_demo = }')
    aoc_context.setup(year, day, is_demo=is_demo)
