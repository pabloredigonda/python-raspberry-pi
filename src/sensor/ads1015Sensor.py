import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class ads1015Sensor:
    def __init__(self):
        self.zeroSaturation = 11008
        self.fullSaturation = 9472
        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)
        # Create the ADC object using the I2C bus
        ads = ADS.ADS1015(i2c)
        # Create single-ended input on channel 0
        self.chan = AnalogIn(ads, ADS.P0)



    def humidity(self):
        return self.percent(self.chan.value)

    def percent(self, rawVal):
        percentage = abs((rawVal - self.zeroSaturation) / (self.fullSaturation - self.zeroSaturation)) * 100
        return round(percentage, 2)