from dataclasses import dataclass
from .treater import Treater
from .tree import Tree

@dataclass
class Quest:
    treater_id: int
    missions: list[Tree]