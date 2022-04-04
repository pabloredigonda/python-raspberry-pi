import RPi.GPIO as GPIO
from src.environment import Environment
from src.artifact.Led import Led
# from src.sensor.W1ThermSensor import W1ThermSensor
from src.sensor.DHT11Sensor import DHT11Sensor
# from src.sensor.ads1015Sensor import ads1015Sensor


class DI:
    led: Led
    dht11_sensor: DHT11Sensor

    def __init__(self, environment: Environment):
        self.__environment = environment
        self.led = Led(GPIO, self.__environment.led_pin)
        self.dht11_sensor = DHT11Sensor(self.__environment.dht11_sensor_pin)
        # self.ds18B20Sensor = W1ThermSensor()
        # self.ads1015Sensor = ads1015Sensor()


    # def ds18B20_sensor(self) -> W1ThermSensor:
    #     return self.ds18B20Sensor
    #
    # def ads1015Sensor(self) -> ads1015Sensor:
    #     return self.ads1015Sensor
