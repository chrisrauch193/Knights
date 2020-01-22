from enum import Enum
class Directions(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = 'W'

class Status(Enum):
    LIVE = "LIVE"
    DROWNED = "DROWNED"
    DEAD = "DEAD"

class ItemType(Enum):
    HELMET = 0
    DAGGER = 1
    MAGICSTAFF = 2
    AXE = 3
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

ATTACK_BONUS = 0.5