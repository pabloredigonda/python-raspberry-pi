from src.artifact.pump import Pump
import time

from src.logger import Logger


class Sprinkler:
    _logger: Logger

    def __init__(self, pump: Pump, logger: Logger):
        self._pump = pump
        self._logger = logger

    def irrigate(self, seconds: int):
        self._logger.log_event("irrigation started")
        self._pump.on()
        time.sleep(seconds)
        self._pump.off()
        self._logger.log_event("irrigation finished")
