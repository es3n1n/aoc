import datetime
import enum
import sys
from dataclasses import dataclass
from typing import ClassVar, NoReturn


class LogLevel(enum.Enum):
    MSG = 'msg'
    INFO = 'info'
    TODO = 'todo'
    FIXME = 'fix'
    ERROR = 'err'
    CRITICAL = 'crit'
    WARN = 'warn'


@dataclass
class LogConfig:
    show_timestamp: bool = True
    color_output: bool = True

    COLORS: ClassVar[dict[LogLevel, str]] = {
        LogLevel.MSG: '\033[0m',  # Default
        LogLevel.INFO: '\033[32m',  # Green
        LogLevel.TODO: '\033[33m',  # Yellow
        LogLevel.WARN: '\033[33m',  # Yellow
        LogLevel.FIXME: '\033[35m',  # Magenta
        LogLevel.ERROR: '\033[31m',  # Red
        LogLevel.CRITICAL: '\033[1;31m',  # Bold Red
    }
    RESET = '\033[0m'


class Logger:
    def __init__(self, config: LogConfig | None = None) -> None:
        if not config:
            config = LogConfig()
        self.config = config

    def _format_message(self, level: LogLevel, message: str) -> str:
        parts = []

        if self.config.show_timestamp:
            timestamp = datetime.datetime.now(tz=datetime.UTC).strftime('%H:%M:%S')
            parts.append(f'[{timestamp}]')

        parts.append(f'{level.value:<4} >>')
        parts.append(message)

        formatted = ' '.join(parts)

        if self.config.color_output and sys.stdout.isatty():
            return f'{self.config.COLORS[level]}{formatted}{self.config.RESET}'
        return formatted

    def _write(self, level: LogLevel, message: str) -> None:
        # str() to allow passing non-strs while debugging
        formatted = self._format_message(level, str(message))

        print(formatted, file=sys.stdout if level != LogLevel.ERROR else sys.stderr)
        sys.stdout.flush()

    def msg(self, message: str) -> None:
        self._write(LogLevel.MSG, message)

    def info(self, message: str) -> None:
        self._write(LogLevel.INFO, message)

    def todo(self, message: str) -> None:
        self._write(LogLevel.TODO, message)

    def fixme(self, message: str) -> None:
        self._write(LogLevel.FIXME, message)

    def error(self, message: str) -> None:
        self._write(LogLevel.ERROR, message)

    def crit(self, message: str) -> NoReturn:
        self._write(LogLevel.CRITICAL, message)
        sys.exit(1)

    def warn(self, message: str) -> None:
        self._write(LogLevel.WARN, message)


default_logger = Logger()
msg = default_logger.msg
info = default_logger.info
todo = default_logger.todo
fixme = default_logger.fixme
error = default_logger.error
crit = default_logger.crit
warn = default_logger.warn
