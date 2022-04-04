from src.sensor.dht11 import DHT11


class DHT11Sensor:
    def __init__(self, pin):
        self.device = DHT11(pin)

    def temperature(self):
        return self.device.read().temperature

    def humidity(self):
        return self.device.read().humidity
