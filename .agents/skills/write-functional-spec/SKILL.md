---
name: write-functional-spec
description: 요구사항을 도메인별 기능명세로 변환한다.
---

# Write Functional Spec Skill

## 1. 목적

이 스킬은 제품 정의와 요구사항을 도메인별 기능명세로 분해한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/02_product/product_brief.md
- docs/02_product/prd.md
- docs/02_product/scope.md
- docs/02_product/business_rules.md

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 기능명세 인덱스 | docs/03_requirements/functional_spec/_index.md |
| 도메인별 기능명세 | docs/03_requirements/functional_spec/<domain>.md |
| 인수 기준 | docs/03_requirements/acceptance_criteria.md |

## 4. 절차

1. 제품 정의 문서를 읽는다.
2. `.agents/templates/functional_spec.template.md`를 참고한다.
3. 비즈니스 도메인을 식별한다.
4. 각 도메인의 기능을 1/2/3계층으로 분해한다.
5. 각 기능에 기능 ID를 부여한다.
6. 도메인별 기능명세 파일을 작성한다.
7. _index.md에 전체 기능 목록과 도메인 매핑을 작성한다.
8. 제품 오너에게 Gate 2. Functional Spec Approval을 요청한다.

## 5. 각 기능 필수 항목

```text
- 기능 ID
- 기능명
- 사용자 유형
- 선행 조건
- 입력값
- 처리 절차
- 성공 결과
- 실패/예외
- 상태 변화
- 관련 화면 ID
- 관련 API ID
- 관련 테이블
- 테스트 기준
```

## 6. 기능 ID 체계

```text
{DOMAIN}-{FEATURE}-{SEQ}

예:
AUTH-SIGNUP-001 이메일 회원가입 폼 입력
AUTH-SIGNUP-002 비밀번호 정책 검증
AUTH-SIGNUP-003 이메일 중복 확인
RSRV-CREATE-001 예약 일시 선택
PAY-CHECKOUT-001 결제 수단 선택
```

## 7. 금지

- "회원 기능", "결제 기능"처럼 큰 덩어리로 끝내지 않는다.
- 소스 코드를 작성하지 않는다.
- 화면정의를 이 단계에서 작성하지 않는다.
