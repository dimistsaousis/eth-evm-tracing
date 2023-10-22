import logging
import asyncio
from datetime import datetime
from dotenv import load_dotenv


class LogColors:
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BRIGHT_RED = "\033[31;1m"
    RESET = "\033[0m"


class LogLevels:
    TRACE = 5
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARN = logging.WARNING
    ERROR = logging.ERROR


logging.addLevelName(LogLevels.TRACE, "TRACE")
logging.addLevelName(LogLevels.DEBUG, "DEBUG")
logging.addLevelName(LogLevels.INFO, "INFO")
logging.addLevelName(LogLevels.WARN, "WARN")
logging.addLevelName(LogLevels.ERROR, "ERROR")


def colorize_log(record):
    color_dict = {
        "TRACE": LogColors.CYAN,
        "DEBUG": LogColors.MAGENTA,
        "INFO": LogColors.GREEN,
        "WARN": LogColors.RED,
        "ERROR": LogColors.BRIGHT_RED,
    }
    level_name = logging.getLevelName(record.levelno)
    color = color_dict.get(level_name, LogColors.RESET)
    return f"{color}{record.msg}{LogColors.RESET}"


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        record.msg = colorize_log(record)
        return super().format(record)


def setup_logger():
    handler = logging.StreamHandler()
    handler.setFormatter(
        ColoredFormatter(f"[%(asctime)s][%(levelname)s] %(message)s", "%H:%M:%S")
    )
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(LogLevels.ERROR)
    logging.getLogger("revm_playground").setLevel(LogLevels.INFO)
