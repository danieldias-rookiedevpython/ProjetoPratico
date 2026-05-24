from enum import Enum


class AppoimentType(Enum):
    RETURN_APPOINTMENT = "return_appointment"
    FIRST_APPOINTMENT = "first_appointment"
    EMERGENCY_APPOINTMENT = "emergency_appointment"