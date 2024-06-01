from dataclasses import dataclass
from typing import Tuple

Client = Tuple[int,str]

def process_clients(clients:list[Client]):
    ...

@dataclass
class Point:
    lat:float
    lang:float

def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinates"""
    return Point(latitude, longitude)