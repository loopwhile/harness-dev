# TASK-XXX: Task Title

## Metadata

| Field | Value |
|---|---|
| TASK ID | TASK-XXX |
| WBS ID | WBS-XX-XXX |
| Domain |  |
| Branch |  |
| Status | TODO |
| Priority | P1 |
| Type | feature / fix / refactor / docs / test / infra / eval |
| Owner |  |
| Created At | YYYY-MM-DD |
| Updated At | YYYY-MM-DD |
| Target Commit | TASK-XXX WBS-XX-XXX: short summary |

## 1. Objective

이 TASK에서 달성해야 하는 결과를 한 문단으로 작성한다.

## 2. Source Context

| Source | Path | Required |
|---|---|---|
| WBS | docs/09_pm/wbs/wbs_xx_xxx.md | Yes |
| PRD | docs/02_product/prd.md | No |
| Scope | docs/02_product/scope.md | No |
| Business Rules | docs/02_product/business_rules.md | No |
| Functional Spec | docs/03_requirements/functional_spec/<domain>.md | No |
| Screen Definition | docs/03_requirements/screen_definition/<domain>.md | No |
| User Flows | docs/03_requirements/user_flows.md | No |
| Design System | docs/06_design/DESIGN.md | No |
| Frontend Design | docs/06_design/frontends/<frontend>/DESIGN.md | No |
| UI Handoff | docs/06_design/ui_handoff/<domain>.md | No |
| Architecture | docs/04_architecture/system_architecture.md | No |
| Architecture Diagrams | docs/04_architecture/architecture_diagrams.md | No |
| Sequence Diagrams | docs/04_architecture/sequence_diagrams.md | No |
| API Contract | docs/05_contracts/api/api_contract.md | No |
| Table Spec | docs/05_contracts/data/table_spec.md | No |
| State Model | docs/05_contracts/state_model.md | No |
| Error Spec | docs/05_contracts/error_spec.md | No |
| ERD | docs/05_contracts/data/erd.md | No |
| Test Strategy | docs/07_test_qa/test_strategy.md | No |

## 3. Allowed Files

에이전트는 아래 파일 또는 디렉터리만 수정할 수 있다.

- 

## 4. Forbidden Files

에이전트는 아래 파일 또는 디렉터리를 수정하면 안 된다.

- docs/01_overview/**
- docs/02_product/**
- docs/03_requirements/**
- docs/04_architecture/**
- docs/05_contracts/**
- docs/06_design/**
- docs/09_pm/wbs/**
- .git/**
- 

## 5. Implementation Requirements

- 
- 
- 

## 6. Acceptance Criteria

- [ ] 
- [ ] 
- [ ] 

## 7. Verification Commands

아래 명령을 실행해 구현 결과를 검증한다.

```bash
# 예시
# npm test
# npm run lint
# npm run build
# pytest
# ./gradlew test
```

## 8. Manual Verification

자동 검증으로 확인하기 어려운 경우 아래 기준으로 수동 검증한다.

- [ ] 
- [ ] 

## 9. Review Checklist

- [ ] 구현이 allowed files 범위 안에 있다.
- [ ] forbidden files가 수정되지 않았다.
- [ ] 관련 없는 리팩터링이 없다.
- [ ] acceptance criteria가 충족되었다.
- [ ] 테스트 또는 검증 명령이 실행되었다.
- [ ] 에러 처리가 적절하다.
- [ ] 보안 위험이 없다.
- [ ] public contract 위반이 없다.
- [ ] 민감 정보가 커밋되지 않았다.

## 10. Recording Requirements

검증과 리뷰 후 아래 파일을 생성 또는 갱신한다.

- `ops/logs/TASK-XXX.log.md`

## 11. Commit Rule

커밋 메시지는 아래 형식을 따른다.

```text
TASK-XXX WBS-XX-XXX: short summary
```

예시:

```text
TASK-001 WBS-01-001: implement reservation creation API
```

## 12. Blockers

TASK를 진행할 수 없는 경우 여기에 사유를 기록한다.

- 

## 13. Execution Notes

에이전트가 실행 중 필요한 짧은 메모를 남길 수 있다.

- 

## 14. Evaluation Scope (EVAL TASK 전용)

EVAL TASK에서만 작성한다. 일반 TASK에서는 이 섹션을 비워둔다.

| Field | Value |
|---|---|
| Evaluation Type | feature_eval / domain_eval / epic_eval |
| Target Domain |  |
| Target Feature |  |
| Evaluated TASKs |  |
| Related WBS Items |  |
| Integration Scope |  |

## 15. User Validation Guide (EVAL TASK 전용)

EVAL TASK에서만 작성한다. 일반 TASK에서는 이 섹션을 비워둔다.

사용자가 직접 기능을 검증할 수 있는 시나리오를 기술한다.

- [ ] 
- [ ] 

사용자 판정 기준:

| 선택 | 의미 |
|---|---|
| APPROVED | 검증 통과. 다음 기능 그룹으로 진행. |
| REJECTED | 검증 실패. 수정 후 재평가 필요. |
| REQUEST_CHANGES | 부분 수정 필요. 지적된 항목만 수정 후 재검증. |
| DEFERRED | 보류. 후속 조치 결정 후 진행. |