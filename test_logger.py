import sys
import time

from src.logger import Logger


if __name__ == "__main__":
    print("Testing logger")
    logger = Logger(file="/home/pablo/test_logger.txt")
    while True:
        try:
            print("Loggin humidity")
            logger.log_humidity(40)
            logger.log_temperature(40)
            time.sleep(3)
        except Exception as error:
            raise error
        except KeyboardInterrupt:
            print("Exiting script")
            sys.exit(0)
