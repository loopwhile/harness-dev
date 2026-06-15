#!/usr/bin/env python3
"""
Antigravity PreToolUse hook.

목적:
- run_command 도구로 실행되는 명령 중 프로젝트 루트 밖 파괴,
  프로젝트 전체 삭제, 원격/외부 시스템 파괴만 감지한다.
- TASK allowed files 내부의 일반적인 rm, git rm 등은 허용한다.
- 현재는 경고만 출력한다. 향후 exit code 1로 차단 가능.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


# 프로젝트 루트 밖 파괴 또는 전체 파괴 패턴
ROOT_DESTRUCTION_PATTERNS = [
    r"\brm\s+-rf\s+/(?!\S)",        # rm -rf /
    r"\brm\s+-rf\s+\.\s",           # rm -rf .
    r"\brm\s+-rf\s+\.\.\s",         # rm -rf ..
    r"\brm\s+-rf\s+\./\*",          # rm -rf ./*
    r"\brm\s+-rf\s+\.\.",           # rm -rf ..
    r"\bfind\s+/\s+-delete\b",      # find / -delete
    r"\bfind\s+\.\.\s+-delete\b",   # find .. -delete
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

    for pattern in ALL_BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            print(
                "[Antigravity Harness Warning] 프로젝트 루트 밖 파괴 또는 원격/외부 파괴 명령이 감지되었습니다.\n"
                f"명령: {command}\n"
                f"패턴: {pattern}\n"
                "AGENTS.md 규칙에 따라 이 작업은 사용자 승인이 필요합니다.\n",
                file=sys.stderr,
            )
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())