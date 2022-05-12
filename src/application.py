from src.di import DI
from src.environment import Environment
from src.program.Program import Program

import time
import signal
import sys


class Application:
    def __init__(self, environment: Environment, di: DI, gpio):
        self.gpio = gpio
        self.startedAt = time.time()
        self.environment = environment
        self.program = Program()
        self.humidity_handler = di.humidity_handler

        signal.signal(signal.SIGINT, self.quit)

    def run(self):

        try:
            time.sleep(10)
            while self.should_continue():
                self.humidity_handler.exec(self.program)
                time.sleep(self.program.seconds_to_sleep)

            self.finish()
        except KeyboardInterrupt:
            print("KeyboardInterrupt exception is caught")
            self.quit()
        except Exception:
            print("Exception is caught")
            self.quit()
        else:
            print("Program Finished")

    def elapsed(self) -> int:
        elapsed_seconds = int(time.time() - self.startedAt)
        print("elapsedSeconds %s" % elapsed_seconds)
        return int(elapsed_seconds / 60)

    def should_continue(self) -> bool:
        print("running since %s" % self.elapsed())
        return self.program.duration_in_minutes >= self.elapsed()

    def finish(self):
        self.gpio.cleanup()
        print("finish")

    def quit(self, event=None, zaraza=None):
        self.finish()
        sys.exit(0)
