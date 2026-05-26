#!/usr/bin/env python3
"""
Antigravity PreToolUse hook.

목적:
- run_command 도구로 실행되는 삭제/파괴성 명령을 감지한다.
- 초기 버전에서는 강제 차단이 아니라 경고 출력 중심으로 둔다.
- 실제 차단 응답 포맷은 Antigravity CLI 버전별로 달라질 수 있으므로,
  우선 AGENTS.md와 agent instruction의 사용자 승인 규칙을 1차 안전장치로 사용한다.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


DESTRUCTIVE_PATTERNS = [
    r"(^|\s)rm\s+",
    r"(^|\s)rmdir\s+",
    r"(^|\s)unlink\s+",
    r"(^|\s)git\s+rm\s+",
    r"(^|\s)git\s+clean\s+",
    r"(^|\s)git\s+reset\s+--hard\b",
    r"(^|\s)git\s+push\s+--force\b",
    r"(^|\s)drop\s+database\b",
    r"(^|\s)drop\s+table\b",
]


def read_payload() -> dict[str, Any]:
    """표준 입력으로 전달된 hook payload를 읽는다."""
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return {}
        return json.loads(raw)
    except Exception:
        return {}


def extract_command(payload: dict[str, Any]) -> str:
    """
    Antigravity hook payload에서 command를 최대한 보수적으로 추출한다.

    CLI 버전에 따라 payload key가 달라질 수 있으므로 여러 후보를 확인한다.
    """
    candidates = []

    if isinstance(payload, dict):
        candidates.append(payload.get("command"))

        tool_input = payload.get("tool_input")
        if isinstance(tool_input, dict):
            candidates.append(tool_input.get("command"))

        input_value = payload.get("input")
        if isinstance(input_value, dict):
            candidates.append(input_value.get("command"))

        args = payload.get("args")
        if isinstance(args, dict):
            candidates.append(args.get("command"))

    for candidate in candidates:
        if isinstance(candidate, str) and candidate.strip():
            return candidate

    return ""


def main() -> int:
    payload = read_payload()
    command = extract_command(payload)

    if not command:
        return 0

    normalized = command.strip().lower()

    for pattern in DESTRUCTIVE_PATTERNS:
        if re.search(pattern, normalized):
            print(
                "[Antigravity Harness Warning] 삭제 또는 파괴성 명령이 감지되었습니다.\n"
                f"명령: {command}\n"
                "AGENTS.md 규칙에 따라 사용자 승인을 먼저 받아야 합니다.\n",
                file=sys.stderr,
            )
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())