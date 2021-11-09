import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor as W1ThermSensorAA


class W1ThermSensor:
    def __init__(self):
        self.sensor = W1ThermSensorAA()

    def read(self):
        return self.sensor.get_temperature()
