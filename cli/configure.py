import os
import json

def run():
    print("🔧 Sleeptracker 설정")

    server = input("서버 주소를 입력하세요 (예: https://tracker.example.com): ").strip()
    log_dir = input("로그 저장 폴더 (기본값: ~/Library/Application Support/sleeptracker): ").strip()

    config = {
        "server": server,
        "log_dir": log_dir or "~/Library/Application Support/sleeptracker"
    }

    config_dir = os.path.expanduser("~/.sleeptracker")
    os.makedirs(config_dir, exist_ok=True)
    config_path = os.path.join(config_dir, "config.json")

    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"✅ 설정이 저장되었습니다: {config_path}")

if __name__ == "__main__":
    run()