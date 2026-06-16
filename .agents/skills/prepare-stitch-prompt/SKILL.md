---
name: prepare-stitch-prompt
description: screen_definition을 Stitch에 넣을 수 있는 프롬프트 묶음으로 변환한다.
---

# Prepare Stitch Prompt Skill

## 1. 목적

이 스킬은 화면정의서를 Stitch 입력용 프롬프트 묶음으로 변환한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/02_product/product_brief.md
- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/03_requirements/user_flows.md
- docs/06_design/design_direction.md (있는 경우)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 도메인별 Stitch 프롬프트 | docs/06_design/stitch/prompts/<domain>.md |

## 4. 절차

1. 화면정의서를 읽는다.
2. `.agents/templates/stitch_prompt_pack.template.md`를 참고한다.
3. 화면별 Stitch 프롬프트를 생성한다.
4. 디자인 방향(있으면)을 프롬프트에 반영한다.
5. 도메인별 Stitch Prompt Pack을 작성한다.
6. 제품 오너에게 Gate 4. Stitch Prompt Approval을 요청한다.

## 5. 프롬프트 구조

프롬프트는 화면별로 생성한다.

```text
SCREEN-AUTH-SIGNUP Stitch Prompt
SCREEN-AUTH-LOGIN Stitch Prompt
SCREEN-AUTH-RESET-PASSWORD Stitch Prompt
```

각 프롬프트에 포함할 정보:

```text
- 화면 목적
- 주요 컴포넌트
- 입력 필드와 유효성
- 버튼과 액션
- 상태별 UI 요구사항
- 디자인 톤 (있으면)
```

## 6. 금지

- 소스 코드를 작성하지 않는다.
- Stitch를 직접 실행하지 않는다. 프롬프트만 준비한다.
- 화면정의 없이 프롬프트를 작성하지 않는다.
