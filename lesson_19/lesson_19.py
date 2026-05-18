import logging
from datetime import datetime
from pathlib import Path

TARGET_KEY = "TSTFEED0300|7E3E|0400"
TIMESTAMP_MARKER = "Timestamp "
TIMESTAMP_LENGTH = 8
TIME_FORMAT = "%H:%M:%S"

WARNING_THRESHOLD = 31
ERROR_THRESHOLD = 33


def setup_logger(log_file: Path) -> logging.Logger:
    logger = logging.getLogger("heartbeat_analyzer")
    logger.setLevel(logging.WARNING)
    logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def filter_lines_by_key(source_file: Path, key: str) -> list[str]:
    filtered: list[str] = []
    with open(source_file, "r", encoding="utf-8") as f:
        for line in f:
            if key in line:
                filtered.append(line.strip())
    return filtered


def extract_timestamp(line: str) -> datetime:
    marker_index = line.find(TIMESTAMP_MARKER)
    if marker_index == -1:
        raise ValueError(f"No '{TIMESTAMP_MARKER}' in line: {line}")

    start = marker_index + len(TIMESTAMP_MARKER)
    time_str = line[start:start + TIMESTAMP_LENGTH]
    return datetime.strptime(time_str, TIME_FORMAT)


def analyze_heartbeats(lines: list[str], logger: logging.Logger) -> dict[str, int]:
    stats = {"ok": 0, "warning": 0, "error": 0}

    for i in range(len(lines) - 1):
        current_time = extract_timestamp(lines[i])
        next_time = extract_timestamp(lines[i + 1])

        diff_seconds = (current_time - next_time).total_seconds()

        current_ts_str = current_time.strftime(TIME_FORMAT)
        next_ts_str = next_time.strftime(TIME_FORMAT)

        if diff_seconds >= ERROR_THRESHOLD:
            logger.error(
                "Heartbeat gap %.0f sec between %s and %s (>=%d sec)",
                diff_seconds, next_ts_str, current_ts_str, ERROR_THRESHOLD,
            )
            stats["error"] += 1
        elif diff_seconds > WARNING_THRESHOLD:
            logger.warning(
                "Heartbeat gap %.0f sec between %s and %s (>%d sec)",
                diff_seconds, next_ts_str, current_ts_str, WARNING_THRESHOLD,
            )
            stats["warning"] += 1
        else:
            stats["ok"] += 1

    return stats


def run_heartbeat_check(source_file: Path, log_file: Path, key: str) -> dict[str, int]:
    logger = setup_logger(log_file)
    lines = filter_lines_by_key(source_file, key)

    if len(lines) < 2:
        logger.warning("Not enough data: found %d lines", len(lines))
        return {"ok": 0, "warning": 0, "error": 0}

    return analyze_heartbeats(lines, logger)


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    source = script_dir / "hblog.txt"
    output = script_dir / "hb_test.log"

    result = run_heartbeat_check(source, output, TARGET_KEY)
    print(f"Analysis finished. Stats: {result}")
    print(f"Result saved to: {output}")