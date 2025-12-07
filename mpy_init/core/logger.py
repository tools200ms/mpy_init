import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

from mpy_init.core.environment import Environment

_init_logger = None

class InitFormatter(logging.Formatter):
    def __init__(self, fmt='%(msecs)s - %(name)s - %(levelname)s - %(message)s'):
        super().__init__()

        print("IMPLEMENTATION: " + Environment.info())
        self.fmt = fmt

class Logger(logging.Logger):
    def __init__(self, name='mpy_init'):
        super().__init__(name)
        self.setLevel(DEBUG)

        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(InitFormatter())

        self.addHandler(handler)

    @staticmethod
    def get():
        global _init_logger
        if _init_logger is None:
            _init_logger = Logger()
        return _init_logger

    def debug(self, msg, *args, **kwargs):
        super().debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        super().info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        super().warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        super().error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        super().critical(msg, *args, **kwargs)
