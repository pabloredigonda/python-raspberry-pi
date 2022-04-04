import os


class Environment:

    led_pin: int
    dht11_sensor_pin: int
    environment: str
    is_testing: bool

    def __init__(self):
        self.led_pin = int(os.getenv("LED_GPIO"))
        self.dht11_sensor_pin = int(os.getenv("DHT11_SENSOR_GPIO"))
        self.environment = str(os.getenv("ENVIRONMENT"))
        self.is_testing = "TESTING" == self.environment
