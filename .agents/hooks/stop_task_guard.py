#!/usr/bin/env python3
"""
Antigravity Stop hook.

목적:
- 에이전트 실행 종료 시점에 저장소 상태를 확인한다.
- 미커밋 변경사항이 남아 있으면 경고한다.
- TASK Execution Mode에서 작업한 경우 검증, 리뷰, 기록, 커밋으로 닫아야 한다.
- General / Analysis Mode에서는 미커밋 변경이 없을 수 있으며 이는 정상이다.
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
    if not Path(".git").exists():
        return 0

    code, stdout, stderr = run(["git", "status", "--short"])

    if code != 0:
        print(f"[Antigravity Harness Warning] git status 확인 실패: {stderr}", file=sys.stderr)
        return 0

    if stdout:
        print(
            "[Antigravity Harness Warning] 미커밋 변경사항이 남아 있습니다.\n"
            "TASK Execution Mode에서 작업한 경우 검증, 리뷰, 기록 후 커밋으로 닫아야 합니다.\n"
            "General / Analysis Mode에서는 이 경고를 무시할 수 있습니다.\n"
            f"{stdout}",
            file=sys.stderr,
        )

    logs_dir = Path("ops/logs")
    if not logs_dir.exists():
        print(
            "[Antigravity Harness Info] ops/logs 디렉터리가 없습니다. TASK 기록 정책을 확인하세요.",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())