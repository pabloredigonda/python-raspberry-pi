from src.di import DI
from src.environment import Environment
from src.program.Program import Program

import time
import signal
import sys


class Application:
    def __init__(self, environment: Environment, di: DI):
        self.startedAt = time.time()
        self.environment = environment
        self.program = Program()
        self.led = di.led
        self.dht11_sensor = di.dht11_sensor
        # self.ds18B20Sensor = di.ds18B20Sensor()
        # self.ads1015Sensor = di.ads1015Sensor()

        signal.signal(signal.SIGINT, self.quit)

    def handle_temperature(self):
        temperature = self.dht11_sensor.temperature()
        print("Temperatura: %s grados" % temperature)

        if temperature < self.program.min_temperature:
            print("Temperatura muy baja, Encendiendo calefaccion")
            self.led.on()
        elif temperature > self.program.max_temperature:
            print("Temperatura muy baja, Encendiendo ventilacion")
            self.led.off()

    def handle_humidity(self):
        # humidity = self.ads1015Sensor.humidity()
        humidity = self.dht11_sensor.humidity()
        print("Humedad: %s" % humidity)

        if humidity < self.program.min_humidity:
            print(f"Humedad ({humidity} %)muy baja, empezando riego")
            self.led.on()
        elif humidity > self.program.max_humidity:
            print("Humedad muy alta, ¿que hacemos?")

    def run(self):
        while self.should_continue():
            # self.handle_temperature()
            self.handle_humidity()
            time.sleep(self.program.seconds_to_sleep)

        self.finish()

    def elapsed(self) -> int:
        elapsedSeconds = int(time.time() - self.startedAt)
        print("elapsedSeconds %s" % elapsedSeconds)
        return int(elapsedSeconds / 60)

    def should_continue(self) -> bool:
        print("running since %s" % self.elapsed())
        return self.program.duration_in_minutes >= self.elapsed()

    def finish(self):
        # GPIO.cleanup()
        print("finish")

    def quit(self, a, b):
        self.finish()
        sys.exit(0)
