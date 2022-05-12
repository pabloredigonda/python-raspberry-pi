import logging


class Logger:
    logger = None

    def __init__(self, file: str):
        logging.basicConfig(
            filename=file,
            filemode="a",
            format="%(asctime)s %(message)s",
            datefmt="%Y:%m:%d %H:%M:%S",
            level=logging.DEBUG,
        )

        self.logger = logging.getLogger("humidity")

    def log(self, message: str) -> None:
        self.logger.info(message)

    def log_event(self, event: str) -> None:
        self.logger.info(f"event: {event}%")

    def log_humidity(self, humidity: float) -> None:
        self.logger.info(f"humidity: {humidity}%")

    def log_temperature(self, temperature: float) -> None:
        self.logger.info(f"temperature: {temperature} grados")
