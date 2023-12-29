# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class IWeatherRequester(ABC):
    @abstractmethod
    def request_conversion(self):
        pass

    @abstractmethod
    def response_conversion(self):
        pass
