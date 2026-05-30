---
name: evaluate-feature
description: EVAL TASK에서 기능 또는 도메인 단위의 품질 평가를 수행하고 사용자 검증 안내를 생성할 때 사용한다.
---

# Evaluate Feature Skill

## 1. 목적

이 스킬은 EVAL TASK에서 기능 또는 도메인 단위의 구현 품질을 평가한다.

evaluator는 구현자가 아니다. 품질 평가자다.

평가 결과를 기록하고 사용자 검증 안내를 생성한 후 중단한다.

## 2. 입력

필수 입력:

- EVAL TASK 파일
- 선행 TASK 목록과 실행 로그
- 관련 WBS 항목
- 관련 문서 및 계약

## 3. 평가 영역

다음 8개 영역을 평가한다.

| # | 평가 영역 | 설명 |
|---|---|---|
| 1 | 기능 목표 정합성 | WBS, PRD, 요구사항에서 정의한 기능 목표와 구현 결과가 일치하는가? |
| 2 | Acceptance Criteria 충족도 | 선행 TASK들의 acceptance criteria가 모두 충족되었는가? |
| 3 | 구현 완성도 | 기능이 실제로 동작하며 누락된 핵심 흐름이 없는가? |
| 4 | 통합 안정성 | 다른 기능과의 연결점이 안정적인가? 회귀 위험이 없는가? |
| 5 | 테스트/검증 충분성 | 테스트 커버리지가 충분하고 핵심 경로가 검증되었는가? |
| 6 | 범위 통제 여부 | 구현이 TASK 범위를 벗어나지 않았는가? 불필요한 변경이 없는가? |
| 7 | 유지보수성 | 코드 구조, 네이밍, 문서화가 적절한가? |
| 8 | 사용자 검증 가능성 | 사용자가 직접 기능을 검증할 수 있는 상태인가? |

## 4. 등급 체계

각 영역은 다음 5단계로 평가한다.

| 등급 | 의미 |
|---|---|
| EXCELLENT | 기대 이상의 품질 |
| GOOD | 충분히 만족스러운 품질 |
| ACCEPTABLE | 최소 기준 충족 |
| NEEDS_IMPROVEMENT | 기준 미달이지만 핵심 기능은 동작 |
| FAIL | 핵심 기능 미동작 또는 심각한 결함 |

## 5. Verdict 결정 기준

최종 verdict는 다음 규칙으로 결정한다.

| Verdict | 조건 |
|---|---|
| PASS | 모든 영역이 ACCEPTABLE 이상이고 FAIL 없음 |
| CONDITIONAL_PASS | 일부 NEEDS_IMPROVEMENT가 있으나 FAIL 없음 |
| FAIL | 하나 이상 FAIL이 있거나 핵심 영역이 NEEDS_IMPROVEMENT 이하 |
| BLOCKED | 평가에 필요한 정보가 부족 |

핵심 영역은 다음이다.

- 기능 목표 정합성
- Acceptance Criteria 충족도
- 구현 완성도

## 6. Evaluation Type

평가 유형에 따라 범위가 다르다.

| Type | 범위 |
|---|---|
| feature_eval | 단일 기능 내 TASK들만 평가 |
| domain_eval | 도메인 내 모든 기능과 기능 간 통합 평가 |
| epic_eval | 여러 도메인에 걸친 대규모 통합 평가 |

domain_eval 또는 epic_eval에서는 추가로 통합 관점 항목을 확인한다.

- 기능 간 데이터 흐름 충돌 여부
- 인증/권한 흐름 일관성
- API/UI 계약 전체 일관성
- 회귀 위험 점검
- 사용자 여정 연속성

## 7. 절차

1. EVAL TASK 파일을 읽는다.
2. AGENTS.md를 확인한다.
3. Evaluation Scope를 확인한다.
   - 평가 대상 TASK 목록
   - Evaluation Type
   - 관련 WBS 항목
4. 선행 TASK 로그를 읽는다.
   - `ops/logs/TASK-xxx.log.md` 파일들
5. 필요한 소스 코드, 테스트, 계약 문서를 읽는다.
6. 통합 검증이 필요하면 verification commands를 실행한다.
7. 8개 평가 영역에 대해 등급과 근거를 작성한다.
8. domain_eval 또는 epic_eval이면 통합 체크 항목을 추가로 확인한다.
9. 최종 verdict를 결정한다.
10. 사용자 검증 안내를 작성한다.
    - 검증 시나리오
    - 경계 조건
    - 알려진 제한사항
11. 평가 결과를 오케스트레이션 에이전트에게 반환한다.

## 8. 사용자 검증 안내 작성 규칙

사용자 검증 안내는 다음 원칙을 따른다.

- 사용자가 직접 실행할 수 있는 구체적 단계를 제공한다.
- 기대 결과를 명확히 기술한다.
- 기술적 전문 용어를 최소화한다.
- 필요한 환경 준비사항을 명시한다.
- 알려진 제한사항을 미리 안내한다.

## 9. 출력 형식

```text
Role: evaluator
TASK ID:
Evaluation Type:
Verdict:
Criteria Results:
  1. 기능 목표 정합성: [등급] - [근거]
  2. Acceptance Criteria 충족도: [등급] - [근거]
  3. 구현 완성도: [등급] - [근거]
  4. 통합 안정성: [등급] - [근거]
  5. 테스트/검증 충분성: [등급] - [근거]
  6. 범위 통제 여부: [등급] - [근거]
  7. 유지보수성: [등급] - [근거]
  8. 사용자 검증 가능성: [등급] - [근거]
Integration Checks: (domain_eval/epic_eval만)
Critical Issues:
Improvement Suggestions:
User Validation Scenarios:
```

## 10. 하드 룰

- 구현 파일을 수정하지 않는다.
- 리팩터링을 하지 않는다.
- 테스트를 수정하지 않는다.
- 커밋하지 않는다.
- 삭제/파괴성 작업을 수행하지 않는다.
- TASK 범위를 확장하지 않는다.
- 평가 증거를 조작하지 않는다.
- 실행하지 않은 검증을 평가에 반영하지 않는다.
- FAIL verdict일 때 사용자에게 보고하고 중단한다.
- 자동으로 이전 TASK를 재실행하지 않는다.
