from dotenv import load_dotenv
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
load_dotenv()


from src.environment import Environment
from src.application import Application
from src.di import DI


def configure_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)


def create_app():
    # configure_gpio()

    environment = Environment()
    di = DI(environment)
    application = Application(environment, di)
    return application.run()
