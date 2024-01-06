from abc import ABC
import requests

import config
from model.geo_temperature import GeoTemperature
from weather_requester import IWeatherRequester


class SimplifiedInheritance(IWeatherRequester, ABC):  # instance этих прослоек хранятся в сервере, это к вопросу о
    # связи сервера и прослойки
    # сама прослойка просто посылает request

    __FINAL_URL = f"http://api.weatherapi.com/v1/current.json?key={config.api_key}&q={{}}&aqi={{}}"

    def __init__(self, city):
        self.city = city

    def request_conversion(self):
        result = requests.get(self.__FINAL_URL.format(self.city, config.api_key))
        data = result.json()

        temperature = data['current']['temp_c']
        coordinate_lon = data['location']['lon']
        coordinate_lat = data['location']['lat']
        return GeoTemperature(temperature, coordinate_lon, coordinate_lat)

    def response_conversion(self):
        pass


if __name__ == '__main__':
    print(SimplifiedInheritance('Moscow').request_conversion())
