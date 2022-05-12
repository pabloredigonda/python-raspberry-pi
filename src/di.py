import RPi.GPIO as GPIO

from src.artifact.pump import Pump
from src.environment import Environment

# from src.artifact.Led import Led
# from src.sensor.W1ThermSensor import W1ThermSensor
from src.humidity_handler import HumidityHandler

# from src.sensor.DHT11Sensor import DHT11Sensor
# from src.sensor.ads1015Sensor import ads1015Sensor
from src.logger import Logger
from src.sensor.ads1015Sensor import Ads1015Sensor
from src.sprinkler import Sprinkler


class DI:
    _environment: Environment
    # led: Led
    pump: Pump
    sprinkler: Sprinkler
    # dht11_sensor: DHT11Sensor
    ads1015Sensor: Ads1015Sensor
    humidity_handler: HumidityHandler
    logger: Logger

    def __init__(self, environment: Environment):
        self._environment = environment
        # self.led = Led(GPIO, self.__environment.led_pin)
        self.logger = Logger(file=environment.logger_file)
        self.pump = Pump(GPIO, self._environment.led_pin)
        self.sprinkler = Sprinkler(pump=self.pump, logger=self.logger)
        # self.dht11_sensor = DHT11Sensor(self.__environment.dht11_sensor_pin)
        self.ads1015Sensor = Ads1015Sensor()
        self.humidity_handler = HumidityHandler(
            ads_1015_sensor=self.ads1015Sensor, sprinkler=self.sprinkler, logger=self.logger
        )
        # self.ds18B20Sensor = W1ThermSensor()
        # self.ads1015Sensor = ads1015Sensor()
