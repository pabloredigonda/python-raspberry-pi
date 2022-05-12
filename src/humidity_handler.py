from src.logger import Logger
from src.sensor.ads1015Sensor import Ads1015Sensor
from src.sprinkler import Sprinkler
from src.sensor.DHT11Sensor import DHT11Sensor
from src.program.Program import Program
import time


class HumidityHandler:
    program: Program = None
    humidity: float = None
    watering_time: int = 3  # Seconds
    min_time_between_watering: int = 120  # Seconds
    last_watering: int = None  # Seconds
    _sensor: Ads1015Sensor
    _sprinkler: Sprinkler
    _logger: Logger

    def __init__(self, ads_1015_sensor: Ads1015Sensor, sprinkler: Sprinkler, logger: Logger):
        self._sensor = ads_1015_sensor
        self._sprinkler = sprinkler
        self._logger = logger

    def exec(self, program: Program):
        self.program = program
        self._read_humidity()
        if self._humidity_to_low():

            time_since_last_watering = self._time_since_last_watering()
            if (
                time_since_last_watering is None
                or time_since_last_watering > self.min_time_between_watering
            ):
                self._sprinkler.irrigate(self.watering_time)
                self.last_watering = time.time()


    def _humidity_to_low(self) -> bool:
        # print(f"humidity: {self.humidity} %")
        self._logger.log_humidity(self.humidity)
        if self.humidity < self.program.min_humidity:
            return True
        return False

    def _read_humidity(self) -> float:
        self.humidity = self._sensor.humidity()
        return self.humidity

    def _time_since_last_watering(self) -> int:
        if not self.last_watering:
            return None

        elapsed_seconds = int(time.time() - self.last_watering)
        print(f"time_since_last_watering: {int(elapsed_seconds)}")
        return int(elapsed_seconds)
