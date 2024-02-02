from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float