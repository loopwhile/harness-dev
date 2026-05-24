#!/usr/bin/env python3
"""
Codex PostToolUse hook.

목적:
- Bash 명령 실행 이후 결과를 확인한다.
- 실패한 명령이 있으면 경고를 출력한다.
- 초기 버전에서는 차단하지 않는다.
"""

from __future__ import annotations

import json
import sys
from typing import Any


def read_payload() -> dict[str, Any]:
    """표준 입력으로 전달된 hook payload를 읽는다."""
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return {}
        return json.loads(raw)
    except Exception:
        return {}


def main() -> int:
    payload = read_payload()

    tool_result = payload.get("tool_result") or {}
    success = tool_result.get("success")

    if success is False:
        print(
            "[경고] 방금 실행한 명령이 실패했습니다. "
            "검증 실패를 숨기지 말고 TASK 로그에 기록하세요.",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())