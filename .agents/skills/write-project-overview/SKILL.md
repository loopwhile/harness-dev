---
name: write-project-overview
description: docs/01_overview/project_overview.md를 생성하거나 갱신하는 Mode 2 초기 스킬이다.
---

# Write Project Overview Skill

## 1. 목적

이 스킬은 프로젝트 개요 문서를 작성하거나 갱신한다.

Mode 2. Planning / Specification Mode의 가장 첫 단계에서 사용한다.

제품 정의(plan-commercial-v1) 이전에 프로젝트의 상위 컨텍스트를 정리한다.

## 2. 입력

- 사용자 서비스 아이디어
- 저장소명 / 프로젝트명
- 프로젝트 유형
- 예상 사용자
- 핵심 문제
- 핵심 가치
- 확정 또는 후보 기술 스택
- 프론트엔드 구성
- 현재 진행 단계

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 프로젝트 개요 | docs/01_overview/project_overview.md |

## 4. 절차

1. 사용자 입력을 정리한다.
2. `.agents/templates/project_overview.template.md`를 참고한다.
3. docs/01_overview/project_overview.md를 작성하거나 갱신한다.
4. 프로젝트명, 한 줄 설명, 문제 정의, 핵심 사용자, 핵심 가치, 현재 상태를 명확히 작성한다.
5. 기술 스택은 확정/후보 상태를 구분하여 정리한다.
6. 프론트엔드가 여러 개인 경우 Frontend ID와 대상 사용자를 정리한다.
7. 이후 plan-commercial-v1이 참고할 수 있도록 제품 정의 이전의 상위 컨텍스트를 정리한다.
8. 제품 오너에게 Overview 확인을 요청한다.

## 5. 핵심 기준

- 제품 상세 PRD로 들어가기 전의 상위 개요만 작성한다.
- 프로젝트 목적, 문제 정의, 핵심 사용자, 핵심 가치, 현재 상태를 명확히 정리한다.
- 기술 스택은 확정/후보 상태를 구분한다.
- v1 방향성 요약을 간결하게 작성한다. 포함/제외 방향을 명시한다.
- 이후 plan-commercial-v1이 참고할 수 있게 작성한다.

## 6. 금지

- 제품 상세 PRD를 이 단계에서 작성하지 않는다.
- 기능명세를 이 단계에서 작성하지 않는다.
- WBS/TASK를 이 단계에서 만들지 않는다.
- 소스 코드를 작성하지 않는다.
