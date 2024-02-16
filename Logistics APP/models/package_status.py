from enum import Enum


class PackageStatus(Enum):
    NOT_ASSIGNED = 'not_assigned'
    ASSIGNED_TO_ROUTE = 'assigned_to_route'
    DELIVERED = 'delivered'