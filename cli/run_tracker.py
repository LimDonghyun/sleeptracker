
"""
CLI 실행 - macOS 시스템 로그 기반 수면 추적

🎯 목적: MacLogReader를 사용하여 시스템 로그에서 수면/기상 이벤트를 추출하고 수면 블록으로 저장
"""
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services.tracker import SleepTracker
from adapters.log_reader_mac import MacLogReader
from adapters.file_writer import JsonFileWriter
from core.analyzer import SleepAnalyzer

if __name__ == "__main__":
    reader = MacLogReader()
    writer = JsonFileWriter("sleep_blocks.json")
    tracker = SleepTracker(reader, SleepAnalyzer, writer)
    tracker.run()
