from dataclasses import dataclass


@dataclass
class GeoTemperature:
    temperature: float
    lon: float
    lat: float
