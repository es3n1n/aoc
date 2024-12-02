from dataclasses import dataclass, field
from pathlib import Path

from requests import Session
from requests.cookies import cookiejar_from_dict

from aoc.logger import crit


_AOC_DEFAULT_CACHE_DIR = Path(__file__).parent.parent / '.aoc'


@dataclass
class AOCContext:
    cache_dir: Path = _AOC_DEFAULT_CACHE_DIR
    year_dir: Path = _AOC_DEFAULT_CACHE_DIR / '2024'

    http_session: Session = field(default_factory=Session)

    year: int = 2024
    day: int = 1

    is_demo: bool = False

    def setup(self, year: int, day: int, *, is_demo: bool) -> None:
        self.year = year
        self.day = day
        self.is_demo = is_demo

        self.year_dir = self.cache_dir / str(self.year)
        self.year_dir.mkdir(exist_ok=True, parents=True)

        self._setup_session()

    def _setup_session(self) -> None:
        session_path = self.year_dir / 'session'

        should_save: bool = False
        session_data: str | None = None
        if session_path.exists():
            session_data = session_path.read_text('utf-8')

        if not session_data:
            session_data = input(f'Session cookie for year {self.year}:')
            should_save = True

        self.http_session = Session()
        self.http_session.headers = {'User-Agent': f'es3n1n/aoc/{self.year}/{self.year}/1.0'}
        self.http_session.cookies = cookiejar_from_dict({'session': session_data})

        if not should_save:
            return

        response = self.http_session.get('https://adventofcode.com/2024/day/1/input')
        if response.status_code != 200:
            crit(f'Session cookie seems to be invalid, server returned {response.status_code}')
        session_path.write_text(session_data, encoding='utf-8')


aoc_context = AOCContext()
