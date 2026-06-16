---
name: ingest-stitch-output
description: Stitch 결과를 개발 가능한 UI handoff와 화면정의 보정사항으로 변환한다.
---

# Ingest Stitch Output Skill

## 1. 목적

이 스킬은 Stitch에서 생성된 화면 결과를 정리하고, 개발 가능한 UI handoff 문서와 화면정의 보정 제안을 작성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- Stitch 스크린샷 또는 결과 설명
- Stitch export 코드 (참고용)
- 사용자 승인/수정 코멘트
- docs/03_requirements/screen_definition/<domain>.md
- docs/06_design/DESIGN.md (있는 경우)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| Stitch 결과 정리 | docs/06_design/stitch/results/<domain>.md |
| UI handoff | docs/06_design/ui_handoff/<domain>.md |
| 화면정의 보정 제안 | docs/03_requirements/screen_definition/<domain>.md 갱신 제안 |
| DESIGN.md 반영 제안 | docs/06_design/DESIGN.md 갱신 제안 |

## 4. 절차

1. Stitch 결과를 확인한다.
2. `.agents/templates/stitch_result_review.template.md`를 참고한다.
3. `.agents/templates/ui_handoff.template.md`를 참고한다.
4. 결과에서 화면 구조, 컴포넌트, 상태를 추출한다.
5. 화면정의서와 비교한다.
6. 차이점을 정리한다.
7. Stitch 결과에서 DESIGN.md 반영 후보를 추출한다. (신규 디자인 패턴, 컴포넌트, 레이아웃 원칙)
8. UI handoff 문서를 작성한다.
9. 필요시 화면정의 보정을 제안한다.
10. 필요시 DESIGN.md 갱신을 제안한다.
11. 제품 오너에게 Gate 5. Stitch Result Approval과 Gate 6. UI Handoff Approval을 요청한다.

## 5. 검증 항목

```text
- Stitch 결과가 화면정의와 일치하는가
- 추가된 필드가 있는가
- 누락된 버튼/상태가 있는가
- API/DB/상태/에러 명세에 영향이 있는가
- 프론트 TASK로 전달할 컴포넌트/레이아웃 기준이 있는가
```

## 6. Stitch 결과 취급

```text
프로덕션 코드 ❌
UI 구조 참고 ✅
컴포넌트 설계 참고 ✅
프론트 TASK 입력 ✅
DESIGN.md 반영 후보 ✅
```

## 7. 금지

- Stitch 결과 코드를 프로덕션 코드로 채택하지 않는다.
- 소스 코드를 작성하지 않는다.
