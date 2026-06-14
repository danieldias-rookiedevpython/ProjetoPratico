from datetime import datetime, time


class RangeTime:

    TIME_PATTERN = "%H:%M"

    def __init__(
        self,
        start_time: str,
        end_time: str
    ):

        self.start_time = self._validate_time(start_time)
        self.end_time = self._validate_time(end_time)

        if self.start_time >= self.end_time:
            raise ValueError(
                "start_time must be lower than end_time"
            )

    def _validate_time(self, value: str) -> time:
        try:
            return datetime.strptime(
                value,
                self.TIME_PATTERN
            ).time()

        except ValueError:
            raise ValueError(
                f"Invalid time format. Use {self.TIME_PATTERN}"
            )

    def __str__(self):
        return (
            f"{self.start_time.strftime(self.TIME_PATTERN)}"
            f" - "
            f"{self.end_time.strftime(self.TIME_PATTERN)}"
        )

    def compare(
        self,
        start_time: str,
        end_time: str
    ):

        start_obj = self._validate_time(start_time)
        end_obj = self._validate_time(end_time)

        return (
            self.start_time == start_obj
            and
            self.end_time == end_obj
        )

    def overlaps(
        self,
        start_time: str,
        end_time: str
    ):

        start_obj = self._validate_time(start_time)
        end_obj = self._validate_time(end_time)

        return (
            self.start_time < end_obj
            and
            self.end_time > start_obj
        )