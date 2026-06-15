#!/usr/bin/env python3
"""
Codex PreToolUse hook.

목적:
- 프로젝트 루트 밖 파괴, 프로젝트 전체 삭제, 원격/외부 시스템 파괴만 감지한다.
- TASK allowed files 내부의 일반적인 rm, git rm 등은 허용한다.
- 현재는 경고만 출력한다. 안정화 후 exit code 1로 차단 가능.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


# 프로젝트 루트 밖 파괴 또는 전체 파괴 패턴
ROOT_DESTRUCTION_PATTERNS = [
    r"\brm\s+-rf\s+/(?!\S)",           # rm -rf /
    r"\brm\s+-rf\s+\.(?:\s|$)",        # rm -rf .
    r"\brm\s+-rf\s+\.\.(?:\s|$)",      # rm -rf ..
    r"\brm\s+-rf\s+\./\*",             # rm -rf ./*
    r"\bfind\s+/\s+-delete\b",         # find / -delete
    r"\bfind\s+\.\.\s+-delete\b",      # find .. -delete
]

# 원격/외부/git 파괴 패턴
REMOTE_DESTRUCTION_PATTERNS = [
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-fdx\b",
    r"\bgit\s+push\s+--force\b",
    r"\bgit\s+push\s+--force-with-lease\b",
    r"\bdrop\s+database\b",
    r"\bdrop\s+table\b",
    r"\btruncate\s+table\b",
]

# 시스템 레벨 위험 패턴
SYSTEM_PATTERNS = [
    r"\bsudo\b",
    r"\bchmod\s+-R\s+777\b",
    r"\bchown\s+-R\b",
    r">\s*/dev/sd[a-z]",
]

ALL_BLOCKED_PATTERNS = (
    ROOT_DESTRUCTION_PATTERNS
    + REMOTE_DESTRUCTION_PATTERNS
    + SYSTEM_PATTERNS
)


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

    for pattern in ALL_BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            print(
                "[경고] 프로젝트 루트 밖 파괴 또는 원격/외부 파괴 명령이 감지되었습니다.\n"
                f"명령: {command}\n"
                f"패턴: {pattern}\n"
                "이 작업은 사용자 승인이 필요합니다.\n"
                "현재 hook은 경고만 출력합니다. 필요하면 이 스크립트에서 exit code를 1로 변경해 차단하세요.",
                file=sys.stderr,
            )
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())