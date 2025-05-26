
import subprocess
import re
import json
from datetime import datetime, timedelta
from pathlib import Path
from core.models import SleepEvent

class MacLogReader:
    """
    MacLogReader
    macOS의 시스템 로그를 파싱하여 수면/기상 이벤트를 SleepEvent 객체로 추출합니다.
    """

    SLEEP_KEYWORDS = [
        "Entering Sleep state due to 'Clamshell Sleep'",
        "Entering Sleep state due to 'Idle Sleep'",
        "Entering Sleep state due to 'Software Sleep'"
    ]

    WAKE_KEYWORDS = [
        "Creating assertion to keep device awake while display is on"
    ]

    SNAPSHOT_FILE = Path(__file__).resolve().parent / ".last_wake_snapshot"

    def __init__(self, hours_back=24):
        self.hours_back = hours_back

    def get_last_timestamp(self):
        if self.SNAPSHOT_FILE.exists():
            try:
                return int(self.SNAPSHOT_FILE.read_text().strip())
            except Exception:
                pass
        return int((datetime.now() - timedelta(hours=self.hours_back)).timestamp())

    def update_snapshot(self):
        now = int(datetime.now().timestamp())
        self.SNAPSHOT_FILE.write_text(str(now))

    def read(self) -> list[SleepEvent]:
        start_ts = self.get_last_timestamp()
        start_time = datetime.fromtimestamp(start_ts)
        end_time = datetime.now()

        cmd = [
            "log", "show",
            "--style", "syslog",
            "--predicate",
            '(eventMessage CONTAINS "Entering Sleep state due to" OR eventMessage CONTAINS "Creating assertion to keep device awake while display is on")',
            "--start", start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "--end", end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "--info", "--debug"
        ]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            raise RuntimeError("macOS log command failed.")

        events = []
        for line in result.stdout.splitlines():
            timestamp_match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
            if not timestamp_match:
                continue
            timestamp_str = timestamp_match.group(1)
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            for kw in self.SLEEP_KEYWORDS + self.WAKE_KEYWORDS:
                if kw in line:
                    message = "start" if "Entering Sleep" in kw else "end"
                    events.append(SleepEvent(timestamp=timestamp, message=message))
                    break

        self.update_snapshot()
        return sorted(events, key=lambda e: e.timestamp)
