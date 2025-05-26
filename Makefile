install:
	@echo "📦 설치 시작: 수면 트래커 환경을 초기화합니다."
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	mkdir -p data logs
	@echo "✅ 기본 구조 준비 완료"

run:
	python3 $(CURDIR)/sleep_tracker_cli/tracker.py
