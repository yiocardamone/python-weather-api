import json
import os

import requests
import urllib3

from model.geo_temperature import GeoTemperature
from model.weather_requester import IWeatherRequester


def find_values_by_key(data: dict, key: str):
    def find_values(obj: dict):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    if isinstance(v, list):
                        return v[0]  # Возвращает первый элемент списка
                    else:
                        return v
                else:
                    result = find_values(v)
                    if result is not None:
                        return result
        elif isinstance(obj, list):
            for element in obj:
                result = find_values(element)
                if result is not None:
                    return result

    return find_values(data)


class SimplifiedInheritance(IWeatherRequester):
    current_directory = os.getcwd()
    path = os.path.join(current_directory, "config.json")

    def __init__(self, coordinate: str):
        self.coordinate = coordinate

    def request_conversion(self):
        with open(self.path) as f:
            data = json.load(f)
            api_url = data["arr"]

            for subjects in api_url:
                url = subjects["url"]
                query_params = subjects["query_params"]
                authenticity_key = list(query_params.values())[0]

                try:
                    result = requests.get(url.format(authenticity_key, self.coordinate))
                    result.raise_for_status()  # Проверяем наличие ошибки в ответе.

                except requests.exceptions.HTTPError as err:
                    if result.status_code == 400:
                        print(f"URL-адрес запроса API недействителен: {err}")
                    if result.status_code == 401:
                        print(f"Ключ не предоставлен: {err}")
                    if result.status_code == 403:
                        continue
                except urllib3.exceptions.NewConnectionError as err:
                    print(f"Произошла ошибка соединения: {err}")
                except requests.exceptions.RequestException as err:
                    print(f"Произошла ошибка обработки запроса: {err}")

                data = result.json()
                support_params = subjects["support_params"]

                location = list(support_params.keys())[0]  # object location
                current = list(support_params.keys())[1]  # object temperature

                lat = support_params[location][0]  # the name of the "location" field
                lon = support_params[location][1]
                temp = support_params[current]  # the name of the "temperature" field

                coordinate_lon = find_values_by_key(data, lon)
                coordinate_lat = find_values_by_key(data, lat)
                temperature = find_values_by_key(data, temp)
                return GeoTemperature(temperature, coordinate_lon, coordinate_lat)

    def response_conversion(self):
        pass
