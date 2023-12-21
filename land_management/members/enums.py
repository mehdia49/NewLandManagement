from enum import Enum, auto

class TransactionType(Enum):
    SALE = 'Sale'
    LEASE = 'Lease'
    TRANSFER = 'Transfer'
    
class TenureType(Enum):
    FREEHOLD = 'Freehold'
    LEASEHOLD = 'Leasehold'
    OTHER = 'Other'

class InfrastructureType(Enum):
    ROAD = 'Road'
    BRIDGE = 'Bridge'
    BUILDING = 'Building'
    OTHER = 'Other'