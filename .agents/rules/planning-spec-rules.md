---
trigger: always_on
---

# Planning Specification Rules

## 적용 범위

이 규칙은 **Mode 2. Planning / Specification Mode**에서 적용한다.

## 핵심 원칙

- AI는 코드 생성기가 아니라 가상 제품팀 역할을 수행한다.
- 사용자는 제품 오너이자 최종 승인자다.
- 문서량이 아니라 개발 가능성이 기준이다.
- MVP로 핵심 기능을 축소하지 않는다.
- Enterprise 문서처럼 과설계하지 않는다.
- Lean Commercial v1 기준으로 작성한다.

## 역할 분배

```text
사용자 = 제품 오너 / 최종 승인자
AI = 제품팀 / 기획자 / BA / UX 설계자 / 아키텍트 / 계약 설계자 / QA 준비자
Stitch = 화면 프레임 생성 도구
하네스 = 개발 실행 단계에서 TASK 단위로 통제하는 장치
```

## 작성 순서

1. 제품 정의 (product_brief, PRD, scope, business_rules)
2. 기능명세 (functional_spec)
3. 사용자 흐름 (user_flows)
4. 화면정의 (screen_definition)
5. DESIGN.md 작성 (전역 + 프론트엔드별)
6. Stitch 프롬프트 작성
7. Stitch 결과 정리
8. UI handoff 작성
9. 아키텍처 / 모듈 경계 / 아키텍처 다이어그램
10. 도메인별 시퀀스 다이어그램
11. API / DB / 상태 / 에러 계약
12. WBS / TASK 생성
13. 개발 착수 가능성 리뷰

## 사용자 승인 Gate

```text
Gate 1. Product Scope Approval
- 이 제품 범위로 갈 것인가?

Gate 2. Functional Spec Approval
- 이 기능 목록과 정책으로 갈 것인가?

Gate 3. Screen Definition Approval
- 이 화면 목록과 화면 흐름으로 갈 것인가?

Gate 4. Stitch Prompt Approval
- 이 프롬프트로 Stitch를 돌릴 것인가?

Gate 5. Stitch Result Approval
- 이 화면 방향으로 갈 것인가?

Gate 6. UI Handoff Approval
- 이 결과를 프론트 구현 TASK로 넘길 것인가?

Gate 7. Contract Approval
- API/DB/상태/에러 계약으로 개발해도 되는가?

Gate 8. Development Readiness Approval
- WBS/TASK로 개발 착수해도 되는가?
```

## 기능명세 작성 기준

기능은 구현 가능한 하위 기능 ID까지 내려간다.

금지:

```text
"회원 기능", "결제 기능"처럼 큰 덩어리로 끝내지 않는다.
```

권장:

```text
AUTH-SIGNUP-001 이메일 회원가입 폼 입력
AUTH-SIGNUP-002 비밀번호 정책 검증
AUTH-SIGNUP-003 이메일 중복 확인
AUTH-SIGNUP-004 약관 동의 검증
AUTH-SIGNUP-005 가입 완료 후 이메일 인증 안내
```

## 화면정의 작성 기준

화면정의서는 최종 화면 기준이다.

Stitch 결과보다 screen_definition이 우선한다.

각 화면은 다음 상태를 모두 정의한다.

```text
기본 상태
로딩 상태
빈 상태
에러 상태
권한 없음 상태
성공 상태
```

## Stitch 결과 취급

Stitch 결과 코드는 다음처럼 취급한다.

```text
프로덕션 코드 ❌
UI 구조 참고 ✅
컴포넌트 설계 참고 ✅
프론트 TASK 입력 ✅
DESIGN.md 반영 후보 ✅
```

## DESIGN.md 작성 기준

DESIGN.md는 프론트엔드 UI/UX의 기준 문서다.

구조:

```text
docs/06_design/DESIGN.md
= 프로젝트 전체 UI/UX 기준 문서

docs/06_design/frontends/<frontend>/DESIGN.md
= 특정 프론트엔드 앱의 UI/UX 기준 문서
```

필수 내용:

```text
Design Principles
Brand Tone
Color / Typography / Spacing
Layout Principles
Navigation Rules
Responsive Rules
Component Guidelines
Form / Validation UX
Error / Empty / Loading States
Accessibility Rules
Screen Pattern Rules
Stitch Extraction Notes
Frontend Implementation Notes
```

진실 공급원 우선순위:

```text
1. screen_definition/<domain>.md
2. docs/06_design/DESIGN.md
3. docs/06_design/frontends/<frontend>/DESIGN.md
4. ui_handoff/<domain>.md
5. Stitch results
6. Stitch prompts
```

## 시퀀스 다이어그램 작성 기준

시퀀스 다이어그램은 대표 하나만 만들지 않는다. 도메인별 핵심 흐름을 작성한다.

반드시 작성하는 흐름:

```text
- 인증/인가가 개입되는 흐름
- 결제/환불/정산 흐름
- 예약/주문/승인처럼 상태가 바뀌는 흐름
- 외부 API 연동 흐름
- 알림/이메일/FCM 흐름
- 배치/스케줄러 흐름
- 실패/보상 처리 흐름
```

초기에는 단일 파일 + 도메인별 섹션, 커지면 디렉토리 분리:

```text
기본: docs/04_architecture/sequence_diagrams.md
커졌을 때: docs/04_architecture/sequence/<domain>.md
```

## 아키텍처 다이어그램 작성 기준

텍스트 아키텍처만으로는 부족하다. Mermaid 기반 다이어그램을 포함한다.

최소 필수 다이어그램:

```text
1. System Context Diagram - 사용자, 관리자, 외부 시스템, 서비스 관계
2. Container Diagram - frontend, backend, DB, storage, external API, batch, queue
3. Module Boundary Diagram - 도메인별 내부 모듈 경계
4. Deployment Diagram - 실제 배포 구조
```

필요시 추가:

```text
5. Data Flow Diagram
6. Security Boundary Diagram
7. Frontend App Architecture Diagram
8. Event / Async Flow Diagram
```

## 문서 구조 기준

기능명세와 화면정의는 도메인별 파일로 관리한다.

```text
기능 하나당 파일 하나 ❌
화면 하나당 파일 하나 ❌
도메인별 기능명세 파일 ✅
도메인별 화면정의 파일 ✅
```

도메인 파일이 너무 커지면 기능 그룹별로 분리한다.

## 금지

- 기능명세 없이 WBS/TASK를 만들지 않는다.
- 화면정의 없이 프론트엔드 TASK를 만들지 않는다.
- API/DB 명세 없이 백엔드 TASK를 만들지 않는다.
- UI handoff 없이 프론트엔드 구현 TASK를 만들지 않는다.
- DESIGN.md 없이 프론트엔드 구현 TASK를 만들지 않는다.
- "회원 기능", "결제 기능"처럼 큰 단위로 TASK를 만들지 않는다.
- 기능 ID → 화면 ID → API ID → 테이블 → 테스트 → TASK 연결이 없는 산출물을 만들지 않는다.
- Stitch 결과 코드를 프로덕션 코드로 바로 사용하지 않는다.
- Mode 2에서 소스 코드 구현을 수행하지 않는다.
- 아키텍처 다이어그램 없이 아키텍처 문서를 완료하지 않는다.
- 도메인별 시퀀스 없이 API 계약을 완료하지 않는다.

## WBS/TASK 생성 기준

WBS에서 TASK를 생성할 때 다음 수준으로 분해한다.

금지:

```text
WBS-01-001 회원가입
WBS-01-002 로그인
WBS-01-003 비밀번호 재설정
```

권장:

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

## 개발 착수 가능성 판정

spec-reviewer가 최종 검수 시 다음 값을 산출한다.

```text
PASS - 개발 착수 가능
CONDITIONAL_PASS - 일부 보강 후 착수 가능
NEEDS_SPEC - 명세 보강 필요
BLOCKED - 결정 필요한 사항이 있어 착수 불가
```

`PASS`가 나와야 Mode 3 TASK Execution으로 넘어간다.
