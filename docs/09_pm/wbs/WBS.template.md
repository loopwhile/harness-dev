# WBS Domain Template

## Metadata

| Field | Value |
|---|---|
| WBS ID | WBS-XX |
| Domain |  |
| Branch |  |
| Status | TODO |
| Priority | P1 |
| Owner |  |
| Created At | YYYY-MM-DD |
| Updated At | YYYY-MM-DD |
| Depends On |  |
| User Validation Status |  |
| Related Docs |  |
| Related ADRs |  |

## 1. Objective

이 도메인에서 달성할 목표를 명확히 작성한다.

## 2. Background

이 작업이 필요한 이유, 상위 요구사항, 관련 문서, 의사결정 배경을 작성한다.

## 3. Scope

### 3.1 In Scope

-

### 3.2 Out of Scope

-

## 4. Deliverables

| Deliverable | Path | Description |
|---|---|---|
|  |  |  |

## 5. WBS 분해 구조

WBS는 아래 3계층으로 분해한다.

```text
Domain (WBS-XX)
└── Feature (WBS-XX-XXX)
    ├── Feature-internal TASK (계약, 백엔드, 프론트엔드, 테스트 등)
    ├── Feature-internal TASK
    ├── Feature-internal TASK
    └── EVAL TASK: 기능 평가 및 사용자 검증 안내
```

도메인 마지막에는 도메인 전체 통합 EVAL TASK를 배치한다.

## 6. Features

### WBS-XX-001 [기능명]

| Order | TASK ID | Title | Type | Priority | Dependencies | Status | Notes |
|---:|---|---|---|---|---|---|---|
| 1 | TASK-XXX | 요청/응답 계약 정의 | feature | P1 |  | TODO |  |
| 2 | TASK-XXX | 백엔드 기본 흐름 구현 | feature | P1 | TASK-XXX | TODO |  |
| 3 | TASK-XXX | 예외/검증 처리 | feature | P1 | TASK-XXX | TODO |  |
| 4 | TASK-XXX | 프론트엔드 연결 | feature | P2 | TASK-XXX | TODO |  |
| 5 | TASK-XXX | 테스트 보강 | test | P2 | TASK-XXX | TODO |  |
| 6 | TASK-XXX | EVAL: [기능명] 평가 및 사용자 검증 안내 | eval | P1 | TASK-XXX ~ TASK-XXX | TODO |  |

### WBS-XX-002 [기능명]

| Order | TASK ID | Title | Type | Priority | Dependencies | Status | Notes |
|---:|---|---|---|---|---|---|---|
| 1 | TASK-XXX |  | feature | P1 |  | TODO |  |
| 2 | TASK-XXX |  | feature | P1 | TASK-XXX | TODO |  |
| N | TASK-XXX | EVAL: [기능명] 평가 및 사용자 검증 안내 | eval | P1 | 선행 TASK 전부 | TODO |  |

## 7. Domain EVAL

| Order | TASK ID | Title | Type | Priority | Dependencies | Status | Notes |
|---:|---|---|---|---|---|---|---|
| 1 | TASK-XXX | EVAL: [도메인명] 전체 통합 평가 및 사용자 검증 안내 | eval | P1 | 도메인 내 모든 TASK | TODO |  |

## 8. TASK 생성 규칙

하나의 Feature는 여러 Feature-internal TASK와 마지막 EVAL TASK로 분해한다.

각 Feature 마지막에는 반드시 기능 EVAL TASK를 둔다.

각 Domain 마지막에는 반드시 도메인 통합 EVAL TASK를 둔다.

TASK 파일명 규칙:

```text
ops/tasks/TASK-XXX.md
```

TASK 번호 체계:

```text
WBS-01: TASK-001 ~ TASK-019
WBS-02: TASK-020 ~ TASK-039
WBS-03: TASK-040 ~ TASK-059
...
```

도메인 전체 EVAL TASK는 해당 범위의 마지막 번호 또는 999를 사용한다.

## 9. EVAL TASK 배치 규칙

1. 기능 마지막에 기능 EVAL TASK를 배치한다.
2. 도메인 마지막에 도메인 통합 EVAL TASK를 배치한다.
3. EVAL TASK의 dependencies에는 해당 범위의 모든 선행 TASK를 명시한다.
4. EVAL TASK의 Type은 반드시 `eval`로 표기한다.
5. EVAL TASK 완료 후 상태는 `PENDING_USER_VALIDATION`으로 둔다.
6. 사용자 `APPROVED` 전까지 다음 Feature group 또는 WBS group으로 진행하지 않는다.

## 10. Dependencies

| Dependency | Type | Impact |
|---|---|---|
|  |  |  |

## 11. Acceptance Criteria

- [ ] 모든 일반 TASK 완료
- [ ] 모든 기능 EVAL TASK 완료
- [ ] 모든 기능 사용자 검증 APPROVED
- [ ] 도메인 EVAL TASK 완료
- [ ] 도메인 사용자 검증 APPROVED

## 12. Verification Strategy

| Check | Command or Method | Required |
|---|---|---|
| Unit test |  | Yes |
| Integration test |  | No |
| Lint |  | Yes |
| Type check |  | Yes |
| Build |  | Yes |
| Manual review |  | Yes |

## 13. Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
|  | Low / Medium / High | Low / Medium / High |  |

## 14. Notes

-