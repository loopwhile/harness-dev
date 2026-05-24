#!/usr/bin/env python3
"""
Codex PreToolUse hook.

목적:
- 위험한 bash 명령을 사전에 감지한다.
- 초기 버전에서는 차단보다 경고를 우선한다.
- 안정화 후 필요하면 exit code를 1로 바꿔 강제 차단할 수 있다.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


DANGEROUS_PATTERNS = [
    r"\brm\s+-rf\s+/",
    r"\brm\s+-rf\s+\.",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-fdx\b",
    r"\bsudo\b",
    r"\bchmod\s+-R\s+777\b",
    r"\bchown\s+-R\b",
    r">\s*/dev/sd[a-z]",
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
    """hook payload에서 bash command를 최대한 안전하게 추출한다."""
    tool_input = payload.get("tool_input") or {}
    if isinstance(tool_input, dict):
        return str(tool_input.get("command") or "")
    return ""


def main() -> int:
    payload = read_payload()
    command = extract_command(payload)

    if not command:
        return 0

    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command):
            print(
                "[경고] 위험 가능성이 있는 명령이 감지되었습니다.\n"
                f"명령: {command}\n"
                f"패턴: {pattern}\n"
                "현재 hook은 경고만 출력합니다. 필요하면 이 스크립트에서 exit code를 1로 변경해 차단하세요.",
                file=sys.stderr,
            )
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())