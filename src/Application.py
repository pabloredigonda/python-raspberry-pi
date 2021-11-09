from .Environment import Environment
from .program.Program import Program

# import RPi.GPIO as GPIO
import time
import signal
import sys

class Application:

    def __init__(self, environment: Environment, di):
        self.startedAt = time.time()
        self.environment = environment
        self.program = Program()
        self.led = di.led()
        self.dht11Sensor = di.dht11Sensor()
        self.ds18B20Sensor = di.ds18B20Sensor()
        self.ads1015Sensor = di.ads1015Sensor()

        # self.configureGpio()
        signal.signal(signal.SIGINT, self.quit)

    # def configureGpio(self):
    #     GPIO.setmode(GPIO.BCM)
    #     GPIO.setwarnings(False)

    def handleTemperature(self):
        temperature = self.dht11Sensor.temperature()
        print("Temperatura: %s grados" % temperature)

        if temperature < self.program.minTemperature():
            print("Temperatura muy baja, Encendiendo calefaccion")
            self.led.on()
        elif temperature > self.program.maxTemperature():
            print("Temperatura muy baja, Encendiendo ventilacion")
            self.led.off()


    def handleHumidity(self):
        humidity = self.ads1015Sensor.humidity()
        print("Humedad: %s" % humidity)

        if humidity < self.program.minHumidity():
            print("Humedad muy baja, empezando riego")
            self.led.on()
        elif humidity > self.program.maxHumidity():
            print("Humedad muy alta, ¿que hacemos?")

    def run(self):

        while self.shouldContinue():
            #self.handleTemperature()
            self.handleHumidity()
            time.sleep(self.program.secondsToSleep())

        self.finish()

    def elapsed(self) -> int:
        elapsedSeconds = int(time.time() - self.startedAt)
        print("elapsedSeconds %s" % elapsedSeconds)
        return int(elapsedSeconds/60)

    def shouldContinue(self) -> bool:
        print("running since %s" % self.elapsed())
        return self.program.durationInMinutes() >= self.elapsed()

    def finish(self):
        # GPIO.cleanup()
        print("finish")

    def quit(self, a, b):
        self.finish()
        sys.exit(0)