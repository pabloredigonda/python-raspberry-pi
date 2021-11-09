from dotenv import load_dotenv

load_dotenv()

from .Environment import Environment
from .Application import Application
from .TestDI import TestDI


def create_app():
    environment = Environment()
    testDi = TestDI(environment)
    application = Application(environment, testDi)

    return application.run()
