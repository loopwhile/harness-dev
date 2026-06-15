# Feature Evaluation: [기능명 또는 도메인명]

## Metadata

| Field | Value |
|---|---|
| EVAL TASK ID | TASK-XXX |
| WBS ID | WBS-XX-XXX |
| Domain |  |
| Branch |  |
| Evaluation Type | feature_eval / domain_eval / epic_eval |
| Evaluated At | YYYY-MM-DD HH:mm |
| Evaluator | evaluator agent |
| Verdict | PASS / CONDITIONAL_PASS / FAIL / BLOCKED |

## Evaluation Scope

| Field | Value |
|---|---|
| Target Domain |  |
| Target Feature |  |
| Evaluated TASKs |  |
| Related WBS Items |  |
| Integration Scope |  |

## Evaluation Criteria

| # | 평가 영역 | 등급 | 근거 |
|---|---|---|---|
| 1 | 기능 목표 정합성 |  |  |
| 2 | Acceptance Criteria 충족도 |  |  |
| 3 | 구현 완성도 |  |  |
| 4 | 통합 안정성 |  |  |
| 5 | 테스트/검증 충분성 |  |  |
| 6 | 범위 통제 여부 |  |  |
| 7 | 유지보수성 |  |  |
| 8 | 사용자 검증 가능성 |  |  |

### 등급 기준

| 등급 | 의미 |
|---|---|
| EXCELLENT | 기대 이상의 품질 |
| GOOD | 충분히 만족스러운 품질 |
| ACCEPTABLE | 최소 기준 충족 |
| NEEDS_IMPROVEMENT | 기준 미달이지만 핵심 기능은 동작 |
| FAIL | 핵심 기능 미동작 또는 심각한 결함 |

### Verdict 결정 기준

| Verdict | 조건 |
|---|---|
| PASS | 모든 영역이 ACCEPTABLE 이상이고 FAIL 없음 |
| CONDITIONAL_PASS | 일부 NEEDS_IMPROVEMENT가 있으나 FAIL 없음 |
| FAIL | 하나 이상 FAIL이 있거나 핵심 영역이 NEEDS_IMPROVEMENT 이하 |
| BLOCKED | 평가에 필요한 정보 부족 |

## Domain / Epic Integration Checks

도메인 또는 epic 평가일 때만 작성한다.

- [ ] 기능 간 데이터 흐름이 충돌하지 않는다.
- [ ] 인증/권한 흐름이 일관된다.
- [ ] API/UI 계약이 전체적으로 일관된다.
- [ ] 회귀 위험이 점검되었다.
- [ ] 사용자 여정이 끊기지 않는다.

## Overall Verdict

```text
Verdict:
Reason:
```

## Critical Issues

심각한 문제가 있으면 여기에 기록한다.

-

## Improvement Suggestions

후속 개선이 필요한 사항을 기록한다.

-

## Notes

추가 메모가 있으면 여기에 기록한다.

-
