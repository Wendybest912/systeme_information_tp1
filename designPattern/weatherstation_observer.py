import random
import time
import datetime
from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def notify(self, subject):
        pass

class StatsDisplay(Observer):
    
    def notify(self, subject):
        self.__display(subject.temperature, subject.humidity, subject.pressure)
    
    def __display(self, temperature, humidity, pressure):
        print(f'Stats: {temperature}, {humidity}, {pressure}')

class RealTimeDisplay(Observer):
    
    def notify(self, subject):
        self.__display(subject.temperature, subject.humidity, subject.pressure)
    
    def __display(self, temperature, humidity, pressure):
        print(f'Real Time: {temperature}, {humidity}, {pressure}')

class DailyMaxDisplay(Observer):
    
    def __init__(self):
        self.__max_temperature = 0
        self.__max_pressure = 0
        self.__max_humidity = 0
    
    def notify(self, subject):
        self.__calculate(subject.temperature, subject.pressure, subject.humidity)
    
    def __calculate(self, temperature, pressure, humidity):
        if humidity > self.__max_humidity:
            self.__max_humidity = humidity
        if pressure > self.__max_pressure:
            self.__max_pressure = pressure
        if temperature > self.__max_temperature:
            self.__max_temperature = temperature
        print(f'Max: {self.__max_temperature} {self.__max_pressure} {self.__max_humidity}')
    

class Subject(ABC):
    def __init__(self):
            self.observer = []

    def attach(self, observer):
        if observer not in self.observer:
            self.observer.append(observer)

    def detach(self, observer):
        if observer in self.observer:
            self.observer.remove(observer)

    def notify(self):
        for observer in self.observer:
            observer.notify(self._temperature, self._humidity, self._pressure)


class WeatherStation(Subject):
    
    def __init__(self):
        super().__init__()
        self.__temperature = 0
        self.__humidity = 0
        self.__pressure = 0
        
    @property
    def temperature(self):
        return self.__temperature
    
    @property
    def humidity(self):
        return self.__humidity
    
    @property
    def pressure(self):
        return self.__pressure
        
    
    def __get_temperature(self):
        return random.randint(-30, 50)
    
    def __get_humidity(self):
        return random.randint(0, 100)
    
    def __get_pressure(self):
        return random.randint(800, 1300)
    

    
    
    def measures_changed(self):
        # get all measures
        self.__temperature = self.__get_temperature()
        self.__humidity = self.__get_humidity()
        self.__pressure = self.__get_pressure()
        # display on screen
        print(datetime.datetime.now())
        for observer in self.observer:
            observer.notify(self)
        
        
        
if __name__ == '__main__':
    stats = StatsDisplay()
    real_time = RealTimeDisplay()
    daily_max = DailyMaxDisplay()
    daily_max_backup = DailyMaxDisplay()
    polar_station = WeatherStation()


    for observer in [stats, real_time, daily_max, daily_max_backup]:
        polar_station.attach(observer)

    for _ in range(10):
        polar_station.measures_changed()
        time.sleep(1)
    