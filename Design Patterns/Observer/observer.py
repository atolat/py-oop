"""
Weather station
Our objective is to build a weather monitoring application with 3 players:
- Physical Devices that acquire weather data
- The weather data objext that tracks data coming from the weather station
- Display devices that consume this data and render them in different formats
"""

from abc import ABC, abstractmethod


# Observables
"""
The Subject Object manages some bits of data
When data changes, observers are notified of the change
This is done by executing the update method on the observers
"""
class Subject(ABC):

    @abstractmethod
    def registerObserver(self, observer):
        """
        Observers will call this method to register themselves with a Subject
        """
        pass

    @abstractmethod
    def removeObserver(self, observer):
        """
        Observers will call this method to de-register themselves with a Subject
        """
        pass

    @abstractmethod
    def notifyObservers():
        """
        This method is used to notify all observers when the Subject's state has changed
        """
        pass


class WeatherData(Subject):
    
    def __init__(self):
        # A list that holds registered observers
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def registerObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except:
            pass

    def notifyObservers(self):
        # Every observer has an implementation of the update method with the same signature
        for obs in self._observers:
            obs.update(self._temperature, self._humidity, self._pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        
        self.measurementsChanged()


# Observers
"""
The observer interface is implemented by all observers, so they all have to implement the update() method
"""
class Observer(ABC):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + str(self._temperature) +
                "F degrees and " + str(self._humidity) + " % humidity");


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self._max_temp = 0.0
        self._min_temp = 200
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self._temp_sum += temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self):
        avg_temp = self._temp_sum / self._num_readings
        print("Statistics Avg/Max/Min temperature = {0}/{1}/{2}".format(
            avg_temp, self._max_temp, self._min_temp))


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self._current_pressure = 29.92
        self._last_pressure = 0.0
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: "),
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        elif self._current_pressure < self._last_pressure:
            print("Watch out for cooler, rainy weather")


if __name__ == '__main__':
    # WeatherStation code
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.setMeasurements(80, 65, 30.4)
    weather_data.setMeasurements(82, 70, 29.2)
    weather_data.setMeasurements(78, 90, 29.2)
