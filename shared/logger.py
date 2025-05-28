# 로깅 유틸리티 (샘플)
def get_logger():
    import logging
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger('sleeptracker')
