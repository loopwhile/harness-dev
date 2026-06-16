---
name: review-spec-completeness
description: 개발 착수 가능한지 명세 완성도를 최종 검수한다.
---

# Review Spec Completeness Skill

## 1. 목적

이 스킬은 모든 기획/설계/명세 산출물을 검수하고 개발 착수 가능 여부를 판정한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/02_product/ 전체
- docs/03_requirements/functional_spec/ 전체
- docs/03_requirements/screen_definition/ 전체
- docs/04_architecture/ 전체
- docs/05_contracts/ 전체
- docs/06_design/ 전체
- docs/09_pm/wbs/ 전체
- ops/tasks/ 전체

## 3. 출력

spec-reviewer는 보고서 초안을 응답으로 반환한다. 파일 기록은 메인 에이전트 또는 recorder가 수행한다.

| 보고서 초안 | 기록 경로 (메인 에이전트가 기록) |
|---|---|
| 명세 갭 보고서 초안 | docs/09_pm/spec_gap_report.md |
| 개발 착수 가능성 보고서 초안 | docs/09_pm/release_readiness_for_development.md |

## 4. 절차

1. 모든 산출물을 읽는다.
2. `.agents/templates/spec_review_report.template.md`를 참고한다.
3. 기능명세 누락을 검수한다.
4. 화면정의 누락을 검수한다.
5. Stitch/UI handoff 반영 여부를 검수한다.
6. API/DB/상태/에러 연결을 검수한다.
7. WBS/TASK 생성 가능성을 검수한다.
8. 판정값을 산출한다.
9. spec_gap_report.md 초안을 생성한다. (응답으로 반환, 메인 에이전트가 파일로 기록)
10. release_readiness_for_development.md 초안을 생성한다. (응답으로 반환, 메인 에이전트가 파일로 기록)
11. 제품 오너에게 Gate 8. Development Readiness Approval을 요청한다.

## 5. 검수 체크리스트

### 기능명세

- [ ] 모든 도메인에 기능명세가 있는가
- [ ] 각 기능에 기능 ID가 부여되어 있는가
- [ ] 각 기능에 처리 절차와 예외 케이스가 있는가
- [ ] 기능 ID가 화면 ID와 연결되어 있는가

### 화면정의

- [ ] 모든 화면에 화면 ID가 있는가
- [ ] 각 화면에 상태별 UI가 정의되어 있는가
- [ ] 화면 ID가 기능 ID와 연결되어 있는가

### 계약

- [ ] API 엔드포인트가 기능 ID와 연결되어 있는가
- [ ] ERD/테이블이 기능 요구사항을 반영하는가
- [ ] 상태 모델이 비즈니스 규칙과 일치하는가
- [ ] 에러 코드 체계가 정의되어 있는가

### WBS/TASK

- [ ] 모든 기능에 대응하는 TASK가 있는가
- [ ] 각 Feature 마지막에 EVAL TASK가 있는가
- [ ] TASK 간 의존성이 명시되어 있는가
- [ ] TASK의 acceptance criteria가 구체적인가

## 6. 판정 기준

```text
PASS - 개발 착수 가능
CONDITIONAL_PASS - 일부 보강 후 착수 가능 (경미한 누락)
NEEDS_SPEC - 명세 보강 필요 (핵심 누락)
BLOCKED - 결정 필요한 사항이 있어 착수 불가
```

PASS가 나와야 Mode 3 TASK Execution으로 넘어간다.

## 7. 금지

- 산출물을 직접 수정하지 않는다. 검수 결과만 보고한다.
- 소스 코드를 작성하지 않는다.
- PASS가 아닌 상태에서 Mode 3 진입을 권장하지 않는다.
