
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SleepEvent:
    timestamp: datetime
    message: str

@dataclass
class SleepBlock:
    start: datetime
    end: datetime

    @property
    def duration_minutes(self) -> float:
        return (self.end - self.start).total_seconds() / 60
