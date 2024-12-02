from .context import aoc_context
from .logger import crit


def day_input() -> str:
    file_name = str(aoc_context.day)
    if aoc_context.is_demo:
        file_name += '.demo'

    cached_input_path = aoc_context.year_dir / 'inputs' / file_name
    if cached_input_path.exists():
        return cached_input_path.read_text('utf-8')

    cached_input_path.parent.mkdir(parents=True, exist_ok=True)

    if aoc_context.is_demo:
        cached_input_path.write_text('')
        crit(f'Missing demo data, please paste it to {cached_input_path}')

    response = aoc_context.http_session.get(f'https://adventofcode.com/{aoc_context.year}/day/{aoc_context.day}/input')
    if response.status_code != 200:
        crit(f'Got {response.status_code} while trying to get the input for day {aoc_context.day}')

    cached_input_path.write_text(response.text)
    return response.text


def day_input_lines() -> list[str]:
    return day_input().splitlines()
