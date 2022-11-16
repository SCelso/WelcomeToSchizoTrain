from enum import Enum


class TrainStatus(Enum):
    __IN_REGULATION_CENTER=1
    __TO_TUNNEL=2
    __IN_TUNNEL_ACCES=3
    __IN_TUNNEL=4
    __TO_REGULATION_CENTER=5