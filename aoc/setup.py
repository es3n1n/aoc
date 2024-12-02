import sys

from .context import aoc_context
from .logger import msg


def aoc_setup(year: int, day: int, *, is_demo: bool = False) -> None:
    if '--demo' in sys.argv:
        msg('Overriding demo to true')
        is_demo = True

    msg(f'Setting up for Dec {day} {year}; {is_demo = }')
    aoc_context.setup(year, day, is_demo=is_demo)
