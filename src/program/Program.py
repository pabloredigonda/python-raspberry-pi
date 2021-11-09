
class Program:
    _durationInMinutes = 1
    _secondsToSleep = 10
    _minTemperature = 20
    _maxTemperature = 24
    _minHumidity = 40
    _maxHumidity = 60

    def secondsToSleep(self) -> int:
        return self._secondsToSleep

    def durationInMinutes(self) -> int:
        return self._durationInMinutes

    def minTemperature(self) -> int:
        return self._minTemperature

    def maxTemperature(self) -> int:
        return self._maxTemperature

    def minHumidity(self) -> int:
        return self._minHumidity

    def maxHumidity(self) -> int:
        return self._maxHumidity