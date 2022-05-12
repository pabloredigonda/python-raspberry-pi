import time

import RPi.GPIO as GPIO

import sys

from src.sensor.ads1015Sensor import Ads1015Sensor

use_bmc_mode = True

if use_bmc_mode:
    GPIO.setmode(GPIO.BCM)
else:
    GPIO.setmode(GPIO.BOARD)


GPIO.setwarnings(False)
GPIO.cleanup()

sensor = Ads1015Sensor()


if __name__ == "__main__":
    print("Testing Moisture Sensor")
    while True:
        try:
            print("Pump on")
            humidity = sensor.humidity()
            print(f"humidity: {humidity} %")
            time.sleep(2)
        except Exception as error:
            raise error
        except KeyboardInterrupt:
            print("exiting script")
            GPIO.cleanup()
            sys.exit(0)
