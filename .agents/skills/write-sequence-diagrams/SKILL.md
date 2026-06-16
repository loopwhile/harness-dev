---
name: write-sequence-diagrams
description: 핵심 사용자 흐름과 시스템 흐름을 Mermaid 시퀀스 다이어그램으로 작성한다.
---

# Write Sequence Diagrams Skill

## 1. 목적

이 스킬은 기능명세와 화면정의를 기반으로 도메인별 핵심 흐름의 시퀀스 다이어그램을 작성한다.

대표 시퀀스 하나만 만들지 않는다. 도메인별 핵심 흐름을 모두 작성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/03_requirements/user_flows.md
- docs/04_architecture/system_architecture.md (있는 경우)
- docs/04_architecture/architecture_diagrams.md (있는 경우)
- docs/05_contracts/api/api_contract.md (있는 경우)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 시퀀스 다이어그램 | docs/04_architecture/sequence_diagrams.md |
| 시스템 아키텍처 (보강) | docs/04_architecture/system_architecture.md |
| 모듈 경계 | docs/04_architecture/module_boundaries.md |
| 런타임 흐름 | docs/04_architecture/runtime_flow.md |

## 4. 절차

1. 기능명세와 화면정의를 읽는다.
2. `.agents/templates/architecture_spec.template.md`를 참고한다.
3. 도메인별 핵심 흐름을 식별한다.
4. 각 흐름에 시퀀스 ID를 부여한다 (SEQ-{DOMAIN}-{SEQ}).
5. 각 흐름의 Mermaid 시퀀스 다이어그램을 작성한다.
6. API 계약이 있으면 시퀀스와 API ID를 연결한다.
7. 시스템 아키텍처를 보강한다. (없으면 초안 작성)
8. 모듈 경계를 정의한다.
9. 런타임 흐름을 정리한다.

## 5. 반드시 작성하는 흐름

```text
- 인증/인가가 개입되는 흐름
- 결제/환불/정산 흐름
- 예약/주문/승인처럼 상태가 바뀌는 흐름
- 외부 API 연동 흐름
- 알림/이메일/FCM 흐름
- 배치/스케줄러 흐름
- 실패/보상 처리 흐름
- 사용자 화면과 API/DB 상태가 함께 변하는 흐름
```

## 6. 시퀀스 ID 체계

```text
SEQ-{DOMAIN}-{SEQ}

예:
SEQ-AUTH-001 이메일 회원가입
SEQ-AUTH-002 로그인
SEQ-AUTH-003 비밀번호 재설정
SEQ-RESERVATION-001 예약 생성
SEQ-RESERVATION-002 예약 변경
SEQ-PAYMENT-001 결제 요청
SEQ-PAYMENT-002 환불
```

## 7. 기능명세/API와의 연결

```text
FUNC-{DOMAIN}-{FEATURE}-{SEQ}
→ SCREEN-{DOMAIN}-{NAME}
→ SEQ-{DOMAIN}-{SEQ}
→ API-{DOMAIN}-{SEQ}
→ tables
→ TASK
```

## 8. 파일 구조

초기에는 단일 파일 + 도메인별 섹션:

```text
docs/04_architecture/sequence_diagrams.md
```

커졌을 때 디렉터리 분리:

```text
docs/04_architecture/sequence/<domain>.md
```

## 9. 금지

- 소스 코드를 작성하지 않는다.
- 기능명세 없이 다이어그램을 작성하지 않는다.
- 대표 시퀀스 하나만 만들고 완료 처리하지 않는다.
