
from core.models import SleepEvent, SleepBlock

class SleepAnalyzer:
    def __init__(self, events: list[SleepEvent]):
        self.events = events

    def extract_blocks(self) -> list[SleepBlock]:
        blocks = []
        start = None
        for event in self.events:
            msg = event.message.lower()
            if "start" in msg:
                start = event.timestamp
            elif "end" in msg and start:
                blocks.append(SleepBlock(start=start, end=event.timestamp))
                start = None
        return blocks
