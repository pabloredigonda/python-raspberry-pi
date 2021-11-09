from dotenv import load_dotenv

load_dotenv()

from .Environment import Environment
from .Application import Application
from .DI import DI


def create_app():
    environment = Environment()
    di = DI(environment)
    application = Application(environment, di)
    return application.run()
