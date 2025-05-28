

import os
import json

def get_config():
    config_path = os.path.expanduser("~/.sleeptracker/config.json")
    if os.path.exists(config_path):
        with open(config_path) as f:
            return json.load(f)
    return {}