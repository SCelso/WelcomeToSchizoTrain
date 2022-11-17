from enum import Enum


class TrainStatus(Enum):
    IN_REGULATION_CENTER = 1
    TO_TUNNEL = 2
    IN_TUNNEL_ACCES = 3
    IN_TUNNEL = 4
    TO_REGULATION_CENTER = 5
