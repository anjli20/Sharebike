from enum import Enum


class Status(Enum):
    RENTED = "RENTED"
    VACANT = "VACANT"
    LOWPOWER = "LOWPOWER"
    BROKEN = "BROKEN"


class UserType(Enum):
    MANAGER = "manager"
    OPERATOR = "operator"
    CUSTOMER = "customer"

