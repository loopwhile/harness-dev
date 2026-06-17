---
name: write-design-system-doc
description: DESIGN.md를 작성하거나 Stitch 결과에서 추출하여 갱신한다.
---

# Write Design System Doc Skill

## 1. 목적

이 스킬은 프론트엔드 UI/UX의 기준 문서인 DESIGN.md를 작성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/02_product/product_brief.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/06_design/ui_handoff/<domain>.md (있는 경우)
- docs/06_design/stitch/results/<domain>.md (있는 경우)
- 사용자의 디자인 선호
- 프론트엔드 앱 목록

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 전역 디자인 기준 | docs/06_design/DESIGN.md |
| 프론트엔드별 디자인 기준 | docs/06_design/frontends/<frontend>/DESIGN.md |
| 디자인 방향 (선택) | docs/06_design/design_direction.md |

## 4. 절차

1. 제품 정의와 화면정의를 읽는다.
2. `.agents/templates/design_doc.template.md`를 참고한다.
3. 프론트엔드 앱 목록을 확인한다.
4. 전역 DESIGN.md를 작성한다.
5. 프론트엔드가 여러 개인 경우 각 프론트엔드별 DESIGN.md를 작성한다.
6. Stitch 결과가 있으면 디자인 토큰, 레이아웃 패턴, 컴포넌트 패턴을 추출하여 반영한다.
7. 화면정의서와 DESIGN.md 간 일관성을 확인한다.
8. 사용자 디자인 선호 또는 Stitch 이전 방향성이 필요한 경우 design_direction.md를 작성한다.

## 5. 전역 DESIGN.md 필수 내용

```text
1. Design Principles
2. Brand Tone
3. Layout Principles
4. Navigation Rules
5. Responsive Rules
6. Color / Typography / Spacing
7. Component Guidelines
8. Form / Validation UX
9. Error / Empty / Loading States
10. Accessibility Rules
11. Screen Pattern Rules
12. Stitch Extraction Notes
13. Frontend Implementation Notes
```

## 6. 프론트엔드별 DESIGN.md 필수 내용

전역 DESIGN.md를 상속하되, 해당 프론트엔드에 특화된 내용을 추가한다.

```text
1. Frontend Overview (대상 사용자, 목적)
2. 전역 DESIGN.md와의 차이
3. 고유 레이아웃 / 내비게이션
4. 고유 컴포넌트
5. 사용 API 범위
6. 권한 모델
```

## 7. 진실 공급원 우선순위

```text
1. screen_definition/<domain>.md
2. docs/06_design/DESIGN.md
3. docs/06_design/frontends/<frontend>/DESIGN.md
4. ui_handoff/<domain>.md
5. Stitch results
6. Stitch prompts
```

## 8. 금지

- 소스 코드를 작성하지 않는다.
- Stitch 결과 코드를 프로덕션 코드로 채택하지 않는다.
- 화면정의 없이 DESIGN.md를 작성하지 않는다.
