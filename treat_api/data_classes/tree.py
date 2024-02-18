from dataclasses import dataclass
from .coordinates import Coordinates

@dataclass
class Tree:
    id: int
    coordinates: Coordinates