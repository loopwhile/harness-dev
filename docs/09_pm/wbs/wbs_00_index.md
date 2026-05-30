# WBS Index

## 1. 목적

현재 프로젝트의 WBS 구조, 활성 작업, 사용자 검증 상태를 관리한다.

## 2. 상태 규칙

### TASK / WBS 상태

| 상태 | 의미 |
|---|---|
| TODO | 생성됨. 아직 시작 불가. |
| READY | 시작 가능 |
| IN_PROGRESS | 현재 진행 중 |
| BLOCKED | 외부 결정 또는 수정 필요 |
| DONE | 완료 |

### 사용자 검증 상태 (EVAL TASK 전용)

| 상태 | 의미 |
|---|---|
| PENDING_USER_VALIDATION | EVAL 완료. 사용자 검증 대기 중. |
| APPROVED | 사용자 검증 통과. 다음 기능 그룹 진행 가능. |
| REQUEST_CHANGES | 부분 수정 필요. 지적된 항목만 수정 후 재검증. |
| REJECTED | 사용자 검증 실패. 수정 후 재평가 필요. |
| DEFERRED | 보류. 후속 조치 결정 후 진행. |

## 3. 현재 활성 포인터

| Field | Value |
|---|---|
| Active Domain WBS |  |
| Active Feature WBS |  |
| Active TASK |  |
| Active EVAL TASK |  |
| User Validation Status |  |
| Next Allowed Action |  |

## 4. WBS 목록

| WBS ID | Domain | Status |
|---|---|---|
| `wbs_01_xxx.md` |  | TODO |
| `wbs_02_xxx.md` |  | TODO |
| `wbs_03_xxx.md` |  | TODO |
| `wbs_04_xxx.md` |  | TODO |
| `wbs_05_xxx.md` |  | TODO |
| `wbs_06_xxx.md` |  | TODO |

## 5. 운영 규칙

- 일반 TASK는 기존 흐름대로 실행한다. (orchestrator → implementer → verifier → reviewer → recorder → commit)
- 기능 완료 시점에는 반드시 EVAL TASK를 실행한다.
- EVAL TASK 완료 후 상태는 `PENDING_USER_VALIDATION`으로 둔다.
- 사용자 `APPROVED` 전까지 다음 Feature group 또는 WBS group으로 진행하지 않는다.
- `REQUEST_CHANGES`이면 correction TASK를 생성하거나 해당 기능 범위에서 수정한다.
- `REJECTED`이면 기능 방향을 재검토하고 재작업 계획을 세운다.
- `DEFERRED`이면 후속 결정 전까지 진행하지 않는다.
- 한 턴에 하나의 TASK만 실행한다.
- 완료 처리는 검증 후 수행한다.
- blocker는 status report에도 반영한다.
