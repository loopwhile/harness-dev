#!/usr/bin/env python3
"""
Codex Stop hook.

목적:
- 에이전트 실행 종료 시점에 저장소 상태를 확인한다.
- TASK 로그 누락, 미커밋 변경사항 등을 경고한다.
- 초기 버전에서는 차단하지 않는다.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> tuple[int, str, str]:
    """명령을 실행하고 exit code, stdout, stderr를 반환한다."""
    result = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def main() -> int:
    git_dir = Path(".git")
    if not git_dir.exists():
        return 0

    code, stdout, stderr = run(["git", "status", "--short"])

    if code != 0:
        print(f"[경고] git status 확인 실패: {stderr}", file=sys.stderr)
        return 0

    if stdout:
        print(
            "[경고] 미커밋 변경사항이 남아 있습니다.\n"
            "TASK가 완료된 상태라면 검증, 리뷰, 기록 후 커밋으로 닫아야 합니다.\n"
            f"{stdout}",
            file=sys.stderr,
        )

    logs_dir = Path("ops/logs")
    if not logs_dir.exists():
        print(
            "[경고] ops/logs 디렉터리가 없습니다. TASK 기록 정책을 확인하세요.",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())