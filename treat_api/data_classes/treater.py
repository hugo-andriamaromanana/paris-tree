from dataclasses import dataclass
from typing import Optional

from .coordinates import Coordinates
from .tree import Tree

@dataclass
class Treater:
    name: str
    starting_position: Coordinates
    closest_tree: Optional[Tree] = None