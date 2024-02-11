from enum import Enum


class TruckStatus(Enum):
    FREE = 'free'
    ON_THE_ROAD_NOT_FULL = 'on_the_road_not_full'
    ON_THE_ROAD_FULL = 'on_the_road_full'
