from .Environment import Environment
from .artifact.FakeLed import FakeLed as Led
from .sensor.FakeW1ThermSensor import FakeW1ThermSensor as W1ThermSensor
from .sensor.FakeDHT11Sensor import FakeDHT11Sensor as DHT11Sensor

class TestDI:

    def __init__(self, environment: Environment):
        self._environment = environment
        self._led = Led(1, 1)
        self._dht11Sensor = DHT11Sensor()
        self._ds18B20Sensor = W1ThermSensor()

    def led(self) -> Led:
        return self._led

    def dht11Sensor(self) -> DHT11Sensor:
        return self._dht11Sensor

    def ds18B20Sensor(self) -> W1ThermSensor:
        return self._ds18B20Sensor
