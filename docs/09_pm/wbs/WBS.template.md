# WBS Template

## Metadata

| Field | Value |
|---|---|
| WBS ID | WBS-XX-XXX |
| Title |  |
| Status | TODO |
| Priority | P1 |
| Owner |  |
| Created At | YYYY-MM-DD |
| Updated At | YYYY-MM-DD |
| Related Docs |  |
| Related ADRs |  |
| Related TASKs |  |

## 1. Objective

이 WBS 항목의 목적을 명확히 작성한다.

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

## 5. Work Items

| WBS Item ID | Title | Target TASK | Status | Notes |
|---|---|---|---|---|
| WBS-XX-001 |  | ops/tasks/TASK-XXX.md | TODO |  |
| WBS-XX-002 |  | ops/tasks/TASK-XXX.md | TODO |  |
| WBS-XX-003 |  | ops/tasks/TASK-XXX.md | TODO |  |

## 6. Dependencies

| Dependency | Type | Impact |
|---|---|---|
|  |  |  |

## 7. Acceptance Criteria

- [ ] 
- [ ] 
- [ ] 

## 8. Verification Strategy

| Check | Command or Method | Required |
|---|---|---|
| Unit test |  | Yes |
| Integration test |  | No |
| Lint |  | Yes |
| Type check |  | Yes |
| Build |  | Yes |
| Manual review |  | Yes |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
|  | Low / Medium / High | Low / Medium / High |  |

## 10. TASK 생성 규칙

이 WBS의 각 work item은 가능한 한 하나의 TASK로 변환한다.

TASK 파일명 규칙:

```text
ops/tasks/TASK-XXX.md
```

TASK와 WBS 매핑 예시:

```text
WBS-01-001 -> ops/tasks/TASK-001.md
WBS-01-002 -> ops/tasks/TASK-002.md
WBS-01-003 -> ops/tasks/TASK-003.md
```

## 11. Notes

- 