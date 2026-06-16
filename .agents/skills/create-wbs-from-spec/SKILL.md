---
name: create-wbs-from-spec
description: 기능명세/화면정의/API/DB/UI handoff를 기반으로 WBS/TASK를 생성한다.
---

# Create WBS from Spec Skill

## 1. 목적

이 스킬은 완성된 기획/설계/명세 산출물을 기반으로 WBS와 TASK 파일을 생성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

기존 `write-wbs` 스킬이 정의한 Domain → Feature → TASK → EVAL TASK 구조를 따르되, 실제 산출물에서 TASK를 도출한다.

## 2. 입력

- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/05_contracts/api/api_contract.md
- docs/05_contracts/data/erd.md
- docs/06_design/DESIGN.md (있는 경우)
- docs/06_design/ui_handoff/<domain>.md (있는 경우)
- docs/04_architecture/system_architecture.md
- docs/04_architecture/architecture_diagrams.md (있는 경우)
- docs/04_architecture/sequence_diagrams.md (있는 경우)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 도메인별 WBS | docs/09_pm/wbs/wbs_XX_<domain>.md |
| WBS 인덱스 갱신 | docs/09_pm/wbs/wbs_00_index.md |
| TASK 파일 | ops/tasks/TASK-XXX.md |

## 4. 절차

1. 기능명세, 화면정의, 계약 문서를 읽는다.
2. `write-wbs` 스킬의 분해 원칙을 따른다.
3. 도메인을 식별한다.
4. 각 도메인에서 Feature를 나열한다.
5. 각 Feature를 TASK로 분해한다.
6. 각 Feature 마지막에 EVAL TASK를 배치한다.
7. 각 Domain 마지막에 도메인 통합 EVAL TASK를 배치한다.
8. WBS 파일과 TASK 파일을 생성한다.
9. WBS 인덱스를 갱신한다.
10. 제품 오너에게 Gate 8. Development Readiness Approval 준비를 안내한다.

## 5. TASK 분해 예시

```text
Feature: AUTH-001 이메일 회원가입

TASK:
- WBS-01-001 회원가입 기능명세/화면정의 보강
- WBS-01-002 회원가입 API/DB 계약 보강
- WBS-01-003 회원가입 백엔드 구현
- WBS-01-004 회원가입 프론트엔드 구현
- WBS-01-005 회원가입 테스트/E2E 작성
- WBS-01-006 EVAL 회원가입 기능 평가 및 사용자 검증 안내
```

## 6. TASK 분해 기준

금지:

```text
WBS-01-001 회원가입
WBS-01-002 로그인
WBS-01-003 비밀번호 재설정
```

기준:

- 하나의 TASK는 하나의 명확한 목표가 있다.
- 에이전트가 단일 실행으로 완료할 수 있는 크기다.
- acceptance criteria가 구체적이다.
- verification commands로 검증 가능하다.

## 7. 연결 확인

TASK를 생성할 때 다음 연결이 존재하는지 확인한다.

```text
기능 ID → 화면 ID → SEQ ID → API ID → 테이블 → TASK
```

연결이 없으면 명세 보강 TASK를 먼저 배치한다.

## 8. 금지

- 소스 코드를 작성하지 않는다.
- 기능명세 없이 TASK를 만들지 않는다.
- 화면정의 없이 프론트엔드 TASK를 만들지 않는다.
- API/DB 명세 없이 백엔드 TASK를 만들지 않는다.
- DESIGN.md 없이 프론트엔드 구현 TASK를 만들지 않는다.
