from enum import Enum, auto


class TruckStatus(Enum):
    FREE = auto()
    ON_THE_ROAD_NOT_FULL = auto()
    ON_THE_ROAD_FULL = auto()
