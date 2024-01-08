from dataclasses import dataclass


@dataclass
class GeoTemperature:
    temperature: float = 0.0
    lon: float(0) = 0.0
    lat: float(0) = 0.0
