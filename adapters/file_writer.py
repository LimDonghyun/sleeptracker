import json
from core.models import SleepBlock

class JsonFileWriter:
    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, blocks: list[SleepBlock]):
        from core.serializer import serialize_sleep_blocks
        data = serialize_sleep_blocks(blocks)
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
