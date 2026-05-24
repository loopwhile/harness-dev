# TASK-001: Format README and Initialize Repository Template Structure

## Metadata

| Field | Value |
|---|---|
| TASK ID | TASK-001 |
| WBS ID | WBS-01-001 |
| Status | IN_PROGRESS |
| Priority | P1 |
| Type | docs |
| Owner | Antigravity |
| Created At | 2026-05-24 |
| Updated At | 2026-05-24 |
| Target Commit | TASK-001 WBS-01-001: format README and initialize repository template structure |

## 1. Objective

README.md 파일의 중복 라인을 제거하고, 프로젝트 템플릿의 초기 디렉터리 구조 및 규칙 파일들을 Git에 추적하도록 설정하고 커밋한다.

## 2. Source Context

| Source | Path | Required |
|---|---|---|
| WBS | docs/09_pm/wbs/wbs_00_index.md | Yes |

## 3. Allowed Files

에이전트는 아래 파일 또는 디렉터리만 수정할 수 있다.

- README.md
- .agents/**
- .codex/**
- AGENTS.md
- docs/**
- ops/**

## 4. Forbidden Files

- None (초기 템플릿 설정이므로 모든 템플릿 파일 허용)

## 5. Implementation Requirements

- README.md의 중복 라인을 삭제한다.
- `.agents/`, `.codex/`, `AGENTS.md`, `docs/`, `ops/` 디렉터리 및 파일을 추적하도록 설정한다.

## 6. Acceptance Criteria

- [x] README.md의 중복 라인 삭제 완료
- [x] 프로젝트 초기 템플릿 파일들의 Git 추적 설정 완료

## 7. Verification Commands

아래 명령을 실행해 구현 결과를 검증한다.

```bash
git status
```

## 8. Manual Verification

- [x] git status 출력 상에서 README.md 수정 사항과 untracked 파일들이 staged 상태로 들어가거나 커밋 가능해졌는지 확인

## 9. Review Checklist

- [x] 구현이 allowed files 범위 안에 있다.
- [x] forbidden files가 수정되지 않았다.
- [x] 관련 없는 리팩터링이 없다.
- [x] acceptance criteria가 충족되었다.
- [x] 테스트 또는 검증 명령이 실행되었다.
- [x] 에러 처리가 적절하다.
- [x] 보안 위험이 없다.
- [x] public contract 위반이 없다.
- [x] 민감 정보가 커밋되지 않았다.

## 10. Recording Requirements

검증과 리뷰 후 아래 파일을 생성 또는 갱신한다.

- `ops/logs/TASK-001.log.md`

## 11. Commit Rule

커밋 메시지는 아래 형식을 따른다.

```text
TASK-001 WBS-01-001: format README and initialize repository template structure
```

## 12. Blockers

- None

## 13. Execution Notes

- 사용자 요청에 따라 현재 상태를 커밋하기 위해 TASK-001을 생성하고 수행함.
