from abc import ABC, abstractmethod


class IWeatherRequester(ABC):
    @abstractmethod
    def request_conversion(self):
        raise NotImplementedError

    @abstractmethod
    def response_conversion(self):
        raise NotImplementedError
