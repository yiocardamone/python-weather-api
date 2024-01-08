from abc import ABC

from model.geo_temperature import GeoTemperature
from model.weather_requester import IWeatherRequester


class OpenWeatherRequesterMock(IWeatherRequester, ABC):
    temperature: float = -2.0
    lat: float = 55.75
    lon: float = 37.62

    def __init__(self, city: str):
        self.city = city

    def response_conversion(self):
        return GeoTemperature(self.temperature, self.lat, self.lon)

    def request_conversion(self):
        pass
