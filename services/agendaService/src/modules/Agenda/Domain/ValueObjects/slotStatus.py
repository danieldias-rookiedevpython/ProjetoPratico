from uuid import UUID
from datetime import datetime
from enum import Enum


class SlotStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    SCHEDULED = "SCHEDULED"
    BLOCKED = "BLOCKED"
    HOLIDAY = "HOLIDAY"