---
name: write-data-api-contracts
description: 기능명세, 화면정의, UI handoff를 API/DB/상태/에러 계약으로 변환한다.
---

# Write Data API Contracts Skill

## 1. 목적

이 스킬은 기능명세, 화면정의, UI handoff를 기반으로 API/DB/상태/에러 계약을 작성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/06_design/ui_handoff/<domain>.md (있는 경우)
- docs/04_architecture/system_architecture.md

## 3. 출력

| 산출물 | 경로 |
|---|---|
| API 계약 | docs/05_contracts/api/api_contract.md |
| ERD | docs/05_contracts/data/erd.md |
| 테이블 명세 | docs/05_contracts/data/table_spec.md |
| 상태 모델 | docs/05_contracts/state_model.md |
| 에러 명세 | docs/05_contracts/error_spec.md |

## 4. 절차

1. 기능명세와 화면정의를 읽는다.
2. `.agents/templates/contract_spec.template.md`를 참고한다.
3. API 엔드포인트를 도출한다. (기능 ID → API ID)
4. ERD를 작성한다.
5. 테이블 명세를 작성한다.
6. 상태 모델을 작성한다. (엔티티별 상태 전이)
7. 에러 명세를 작성한다. (에러 코드 체계)
8. 기능 ID → 화면 ID → API ID → 테이블 → 상태 → 에러 코드 연결을 확인한다.
9. 제품 오너에게 Gate 7. Contract Approval을 요청한다.

## 5. 핵심 연결

```text
기능 ID
→ 화면 ID
→ API ID
→ 테이블
→ 상태
→ 에러 코드
→ 테스트 기준
```

## 6. 금지

- 소스 코드를 작성하지 않는다.
- 기능명세 없이 API를 설계하지 않는다.
- 화면정의 없이 에러 메시지를 정의하지 않는다.
