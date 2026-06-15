# Status Report

## 1. 현재 상태
- 최근 종료 task:
- 현재 active task pointer:
- 현재 활성 WBS:
- 상태: `READY` | `IN_PROGRESS` | `BLOCKED` | `STANDBY` | `DONE`

## 2. 최근 종료
- 완료 항목 1
- 완료 항목 2

## 3. 현재 작업
- 작업 ID:
- 목표:
- 범위:

## 4. active task 전환 규칙
- 대표 추적 포인터는 Domain Branch Status (`docs/09_pm/wbs/wbs_00_index.md`)에서 관리한다.
- 단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.
- 단일 브랜치는 한 번에 하나의 Active TASK만 가진다.
- 현재 task가 `PASS` 검증을 마치고 로그 반영이 확인된 뒤에만 전환한다.
- 같은 턴에서 다음 `READY` task를 자동 실행하지 않고 pointer 준비까지만 허용한다.
- `DONE` task가 active pointer로 남아 있으면 종료 전 반드시 다음 candidate 또는 `standby`로 갱신한다.

## 5. restart-safe 운영 체크
- 종료 시점에 `status_report.md`, `wbs_00_index.md`, TASK 파일이 상호 참조 가능해야 한다.
- 전환 사유와 다음 task 또는 `standby` 사유가 문서에 남아 있어야 한다.

## 6. 현재 블로커
- blocker 1
- blocker 2

## 7. 최근 검증 상태
- test:
- typecheck:
- lint:
- build:

## 8. 다음 단계
- 다음 단계 1
- 다음 단계 2
