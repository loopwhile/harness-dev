---
name: write-screen-definition
description: 기능명세를 화면 ID 단위의 화면정의서로 변환한다.
---

# Write Screen Definition Skill

## 1. 목적

이 스킬은 기능명세를 기반으로 도메인별 화면정의서를 작성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/03_requirements/functional_spec/<domain>.md
- docs/02_product/prd.md
- docs/02_product/scope.md
- docs/06_design/DESIGN.md (있는 경우)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 사용자 흐름 | docs/03_requirements/user_flows.md |
| 화면정의 인덱스 | docs/03_requirements/screen_definition/_index.md |
| 도메인별 화면정의 | docs/03_requirements/screen_definition/<domain>.md |

## 4. 절차

1. 기능명세를 읽는다.
2. `.agents/templates/screen_definition.template.md`를 참고한다.
3. 사용자 흐름(user_flows.md)을 작성한다.
4. 화면 목록을 도출하고 화면 ID를 부여한다.
5. 프론트엔드가 여러 개인 경우 대상 Frontend ID를 명시한다.
6. 도메인별 화면정의 파일을 작성한다.
7. 각 화면에서 기능 ID와의 연결을 명시한다.
8. DESIGN.md가 있으면 충돌하는 부분을 확인한다.
9. 제품 오너에게 Gate 3. Screen Definition Approval을 요청한다.

## 5. 각 화면 필수 항목

```text
- 화면 ID (SCREEN-{DOMAIN}-{NAME})
- URL/path
- 접근 권한
- 화면 목적
- Frontend ID (프론트엔드가 여러 개인 경우)
- Design Reference (관련 DESIGN.md 경로)
- 표시 컴포넌트
- 입력 필드 (이름, 타입, 필수 여부, 유효성 규칙)
- 버튼/액션
- 상태별 UI (기본/로딩/빈/에러/권한없음/성공)
- 에러 메시지
- 관련 기능 ID
- 관련 API ID
```

## 6. 금지

- 소스 코드를 작성하지 않는다.
- Stitch 프롬프트를 이 단계에서 작성하지 않는다.
- 기능명세 없이 화면정의를 작성하지 않는다.
