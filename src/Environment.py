import os

class Environment:

    def __init__(self):
        self._ledPin = int(os.getenv('LED_GPIO'))
        self._dht11SensorPin = int(os.getenv('DHT11_SENSOR_GPIO'))

    def ledPin(self) -> int:
        return self._ledPin

    def dht11SensorPin(self) -> int:
        return self._dht11SensorPin

    def isTesting(self) -> bool:
        return 'TESTING' == self.environment()

    def environment(self) -> str:
        return os.getenv('ENVIRONMENT')


