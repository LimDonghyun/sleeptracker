
import json
from core.models import SleepBlock

class JsonFileWriter:
    def __init__(self, filepath):
        self.filepath = filepath

    def save(self, blocks: list[SleepBlock]):
        data = [{
            "start": block.start.isoformat(),
            "end": block.end.isoformat(),
            "duration_minutes": block.duration_minutes
        } for block in blocks]
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2)
