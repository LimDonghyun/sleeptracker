
import json
from datetime import datetime
from core.models import SleepEvent

class JsonLogReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self) -> list[SleepEvent]:
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        return [
            SleepEvent(
                timestamp=datetime.fromisoformat(d["timestamp"]),
                message=d["message"]
            )
            for d in data
        ]
