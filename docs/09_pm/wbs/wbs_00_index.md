# WBS Index

## 1. 목적

현재 프로젝트의 WBS 구조, 도메인 브랜치 상태, 사용자 검증 상태를 관리한다.

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

## 3. Domain Branch Status

| WBS | Domain | Branch | Active TASK | Status | Depends On | User Validation | Next Action |
|---|---|---|---|---|---|---|---|
| WBS-00 | Common | common | - | TODO | - | - | start |
| WBS-01 | Auth | auth | - | TODO | WBS-00 | - | wait |
| WBS-02 | Reservation | reservation | - | TODO | WBS-00, WBS-01 | - | wait |
| WBS-03 | Payment | payment | - | TODO | WBS-00, WBS-01 | - | wait |
| WBS-04 | Board | board | - | TODO | WBS-00, WBS-01 | - | wait |
| WBS-05 | Notification | notification | - | TODO | WBS-00, WBS-01 | - | wait |

## 4. WBS 목록

| WBS ID | Domain | Branch | Status |
|---|---|---|---|
| `wbs_01_xxx.md` |  |  | TODO |
| `wbs_02_xxx.md` |  |  | TODO |
| `wbs_03_xxx.md` |  |  | TODO |
| `wbs_04_xxx.md` |  |  | TODO |
| `wbs_05_xxx.md` |  |  | TODO |
| `wbs_06_xxx.md` |  |  | TODO |

## 5. 운영 규칙

- 단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.
- 단일 브랜치는 한 번에 하나의 Active TASK만 가진다.
- 프로젝트 전체에서는 여러 도메인 브랜치가 각자 다른 TASK를 병렬로 실행할 수 있다.
- 일반 TASK는 기존 흐름대로 실행한다. (orchestrator → implementer → verifier → reviewer → recorder → commit)
- 기능 완료 시점에는 반드시 EVAL TASK를 실행한다.
- EVAL TASK 완료 후 상태는 `PENDING_USER_VALIDATION`으로 둔다.
- 사용자 `APPROVED` 전까지 다음 Feature group 또는 WBS group으로 진행하지 않는다.
- `REQUEST_CHANGES`이면 correction TASK를 생성하거나 해당 기능 범위에서 수정한다.
- `REJECTED`이면 기능 방향을 재검토하고 재작업 계획을 세운다.
- `DEFERRED`이면 후속 결정 전까지 진행하지 않는다.
- TASK 실행 전 현재 git branch가 TASK의 Branch와 일치하는지 확인한다.
- 완료 처리는 검증 후 수행한다.
- blocker는 Domain Branch Status에도 반영한다.
