---
name: plan-commercial-v1
description: 제품 오너의 아이디어를 Lean Commercial v1 제품 정의로 변환한다.
---

# Plan Commercial v1 Skill

## 1. 목적

이 스킬은 제품 오너의 아이디어, 타깃 사용자, 수익모델, 핵심 기능 목록을 입력 받아 상용 v1 제품 정의를 완성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/01_overview/project_overview.md (있는 경우)
- 사용자 아이디어 또는 비전
- 타깃 사용자
- 수익모델
- 필수 기능 목록
- 제외할 기능
- 운영 방식 (셀프 서비스 / 관리자 포함 등)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 제품 요약 | docs/02_product/product_brief.md |
| PRD | docs/02_product/prd.md |
| 범위 | docs/02_product/scope.md |
| 비즈니스 규칙 | docs/02_product/business_rules.md |

## 4. 절차

1. docs/01_overview/project_overview.md가 있으면 먼저 읽는다.
2. 사용자 입력과 project_overview.md를 비교해 제품 정의의 기준 컨텍스트를 확정한다.
3. `.agents/templates/product_brief.template.md`를 참고한다.
4. product_brief.md를 작성한다. (서비스 목적, 타깃 사용자, 핵심 가치)
5. prd.md를 작성한다. (기능 목록, 사용자 시나리오, 기술 제약)
6. scope.md를 작성한다. (v1 포함 범위, 제외 범위, 향후 확장)
7. business_rules.md를 작성한다. (운영 정책, 결제 규칙, 취소 정책 등)
8. 제품 오너에게 Gate 1. Product Scope Approval을 요청한다.

## 5. 핵심 기준

- MVP라고 핵심 기능을 빼지 않는다.
- Enterprise 문서처럼 과도하게 확장하지 않는다.
- Lean Commercial v1 기준으로 정리한다.
- 결정이 필요한 사항은 명시적으로 도출한다.

## 6. 금지

- 소스 코드를 작성하지 않는다.
- 기능명세를 이 단계에서 작성하지 않는다.
- WBS/TASK를 이 단계에서 만들지 않는다.
