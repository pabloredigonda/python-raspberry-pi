from .Environment import Environment
import RPi.GPIO as GPIO
from .artifact.Led import Led
from .sensor.W1ThermSensor import W1ThermSensor
from .sensor.DHT11Sensor import DHT11Sensor
from .sensor.ads1015Sensor import ads1015Sensor

class DI:

    def __init__(self, environment: Environment):
        self.environment = environment
        self.led = Led(GPIO, self.environment.ledPin())
        self.dht11Sensor = DHT11Sensor(self.environment.dht11SensorPin())
        self.ds18B20Sensor = W1ThermSensor()
        self.ads1015Sensor = ads1015Sensor()

    def led(self) -> Led:
        return self.led

    def dht11Sensor(self) -> DHT11Sensor:
        return self.dht11Sensor

    def ds18B20Sensor(self) -> W1ThermSensor:
        return self.ds18B20Sensor

    def ads1015Sensor(self) -> ads1015Sensor:
        return self.ads1015Sensor
