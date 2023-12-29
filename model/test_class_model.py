from abc import ABC

from model.geo_temperature import GeoTemperature
from model.weather_requester import IWeatherRequester


class TestClassModel(IWeatherRequester, ABC):
    temperature = -2.0
    lat = 55.75
    lon = 37.62

    def __init__(self, city):
        self.city = city

    def response_conversion(self):
        tom = GeoTemperature(self.temperature, self.lat, self.lon)
        return tom

    def request_conversion(self):
        pass
