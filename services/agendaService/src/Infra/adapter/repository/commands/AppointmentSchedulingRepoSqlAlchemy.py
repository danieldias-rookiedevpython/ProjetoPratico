from src.infra.adapter.repository.base import SQLiteRepository
from src.modules.agenda.aplication.dtos.repositorys.output.AppointmentSchedulingOutputDTO import (
    AppointmentSchedulingOutputDTO,
)
from src.modules.agenda.domain.entities import Day, Doctor, Patient, Room
from src.modules.agenda.domain.rules import GenericRule, RuleEffect, TargetType
from src.modules.agenda.domain.valueObjects import AppointmentType, Date, DayStatus, Hour
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime


class AppointmentSchedulingRepository(SQLiteRepository):
    async def getContext(self, appointmentScheduling):
        available_rule = GenericRule(
            ruleEffect=RuleEffect.ADD,
            targetType=TargetType.DAY,
            rangeTime=RangeTime("00:00", "23:59"),
            description="Default availability",
        )
        patient = Patient(
            id=appointmentScheduling.patient,
            name=appointmentScheduling.patient,
        )
        doctor = Doctor(
            id=appointmentScheduling.doctor,
            name=appointmentScheduling.doctor,
            rules=[available_rule],
        )
        room = Room(
            id=appointmentScheduling.room or "default-room",
            name=appointmentScheduling.room or "default-room",
            rules=[available_rule],
        )
        day = Day(
            rooms=[room],
            date=self._parse_date(appointmentScheduling.date),
            weekday=int(appointmentScheduling.weekday or 0),
            availability=True,
            status=DayStatus.AVAILABLE,
            rules=[available_rule],
        )
        return AppointmentSchedulingOutputDTO(
            doctor=doctor,
            day=day,
            patient=patient,
            room=[room],
            appointments=[],
            type=AppointmentType(
                name=appointmentScheduling.type,
                duration=30,
                description=appointmentScheduling.type,
            ),
            time=Hour(appointmentScheduling.time),
        )

    def _parse_date(self, value: str) -> Date:
        clean = value.split("T", 1)[0]
        year, month, day = clean.split("-")
        return Date(day=int(day), month=int(month), year=int(year))
