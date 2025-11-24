# Logger used by coral

if __name__ == "__main__":
    raise RuntimeError("`logger.py` is not meant to be run unless imported")

import time

from pathlib import Path
from typing import Literal


class LoggingError(Exception):
    """Base Class for all logging related Errors."""

def get_path() -> str:
    ct = str(time.time()).replace(".", "")
    try:
        with open(f"log_{ct}.log", "r", errors="strict") as file: 
            file.close()
            return get_path()
    except FileNotFoundError:
        return f"latest.log"
    return f"log_{ct}.log"


class logger():

    def __init__(self, newPath: str | None=None) -> None: 
        """
        Initiate a new log at `logs/`, except another path is given.
        """

        if new_path is None:
            self.LOG_PATH = rf"logs/{get_path()}"
        else: 
            self.LOG_PATH = f"{new_path}.log"
        with open(self.LOG_PATH, "x", errors="strict"):
            pass
        self.new_entry(f"Initiated file as {self.LOG_PATH}", "Info")

    def new_entry(self, msg: str, level: Literal["Debug", "Info", "Error", "Fatal"]="Debug") -> None:
        """
        Log to existing log, or create a new one and log to that one if needed.
        """

        try:
            with open(self.LOG_PATH, "a", errors="strict") as file:
                file.write(f"{time.strftime("%H:%M:%S", time.localtime())} [{level}]: {msg}\n")
        except NameError:
            self.__init__()
            self.new_entry(msg, level)

    def current_path(self) -> str:
        """
        Return the current Path of the log.
        """

        try:
            return self.LOG_PATH
        except NameError: 
            raise LogError("LOG_PATH is unavailable. Did it get deleted?")

    def del_all(self) -> None:
        """
        Delete all logs, except the latest.
        """

        directory = Path(self.LOG_PATH).parent
        for file in directory.iterdir():
            if file.is_file() and file.suffix == ".log" and file.name != self.LOG_PATH:
                file.unlink()

    def new_Path(self, newPath: str) -> None:
        self.__init__(newPath)

    def extensive_error(self, obj) -> None:
        self.new_entry(f"{obj}, traceback to {obj.__traceback__.tb_frame}", "Error")
        self.new_entry(f"Traceback object at {obj.__traceback__}", "Error")
        self.new_entry(f"TB Lasti: {obj.__traceback__.tb_lasti}", "Error")
        self.new_entry(f"TB Lineno: {obj.__traceback__.tb_lineno}", "Error")
        self.new_entry(f"TB Next: {obj.__traceback__.tb_next}", "Error")
        self.new_entry(f"Exiting Program", "Fatal")

    def debug(self, msg: str) -> None:
        self.new_entry(msg, level="Debug")

    def info(self, msg: str) -> None:
        self.new_entry(msg, level="Info")

    def error(self, msg: str) -> None:
        self.new_entry(msg, level="Error")

    def fatal(self, error: Exception, msg: str | None = "") -> None:
        self.new_entry(f"{error}: {msg}", "Fatal")
        raise error
