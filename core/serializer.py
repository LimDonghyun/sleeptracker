from datetime import datetime
import os

def serialize_sleep_blocks(blocks):
    return {
        "device_id": os.uname().nodename,
        "timestamp": datetime.now().isoformat(),
        "blocks": [b.to_dict() for b in blocks]
    }
