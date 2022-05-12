from abc import ABC, abstractmethod
import RPi.GPIO as GPIO


class Artifact(ABC):
    def __init__(self, gpio, pin):
        self.gpio = gpio
        self.pin = pin
        self.gpio.setup(pin, GPIO.OUT)
        self.gpio.output(pin, GPIO.LOW)

    def on(self):
        self.gpio.output(self.pin, GPIO.HIGH)

    def off(self):
        self.gpio.output(self.pin, GPIO.LOW)
