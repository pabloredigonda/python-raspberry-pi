import time

import RPi.GPIO as GPIO

from src.artifact.pump import Pump
import sys


use_bmc_mode = True

if use_bmc_mode:
    GPIO.setmode(GPIO.BCM)
    pin = 21
else:
    GPIO.setmode(GPIO.BOARD)
    pin = 40


# GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

pump = Pump(GPIO, pin)


if __name__ == "__main__":
    print("Testing Pump")
    while True:
        try:
            print("Pump on")
            pump.on()
            time.sleep(2)
            pump.off()
            time.sleep(15)
        except Exception as error:
            raise error
        except KeyboardInterrupt:
            print("exiting script")
            pump.off()
            GPIO.cleanup()
            sys.exit(0)