import requests

from weather_requester import IWeatherRequester


class SimplifiedInheritance(
    IWeatherRequester):  # инстансы этих прослоек хранятся в сервере, это к вопросу о связи сервера и прослойки
    # сама прослойка просто посылает реквесты

    API_KEY = "f5b39ac7a82e4dbd8a5120339231312"  # Paste Your API ID Here
    FINAL_URL = "http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q={}&aqi={}"

    def __init__(self, city):
        self.city = city

    def request_conversion(self):
        result = requests.get(self.FINAL_URL.format(self.city, self.API_KEY))
        data = result.json()

        temperature = data['current']['temp_c']
        coordinate_lon = data['location']['lon']
        coordinate_lat = data['location']['lat']

        return str(temperature) + " " + str(coordinate_lat) + " " + str(coordinate_lon)

    def response_conversion(self):
        pass


if __name__ == '__main__':
    print(SimplifiedInheritance('Moscow').request_conversion())
