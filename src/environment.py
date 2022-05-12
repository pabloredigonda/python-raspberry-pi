import os


class Environment:

    logger_file: str
    led_pin: int
    dht11_sensor_pin: int
    environment: str
    is_testing: bool

    def __init__(self):
        self.logger_file = str(os.getenv("LOGGER_FILE"))
        self.led_pin = int(os.getenv("LED_GPIO"))
        self.dht11_sensor_pin = int(os.getenv("DHT11_SENSOR_GPIO"))
        self.environment = str(os.getenv("ENVIRONMENT"))
        self.is_testing = "TESTING" == self.environment
