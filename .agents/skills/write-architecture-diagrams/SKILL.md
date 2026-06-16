---
name: write-architecture-diagrams
description: 텍스트 아키텍처를 Mermaid 다이어그램으로 변환하고, 도메인별 시퀀스 다이어그램을 생성한다.
---

# Write Architecture Diagrams Skill

## 1. 목적

이 스킬은 텍스트 기반 아키텍처 문서를 Mermaid 다이어그램으로 시각화하고, 도메인별 핵심 시퀀스 다이어그램을 생성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/04_architecture/system_architecture.md
- docs/04_architecture/module_boundaries.md (있는 경우)
- docs/04_architecture/runtime_flow.md (있는 경우)
- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/03_requirements/user_flows.md
- docs/05_contracts/api/api_contract.md (있는 경우)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 아키텍처 다이어그램 | docs/04_architecture/architecture_diagrams.md |
| 시퀀스 다이어그램 | docs/04_architecture/sequence_diagrams.md |

## 4. 절차

1. 아키텍처 문서를 읽는다.
2. `.agents/templates/architecture_diagrams.template.md`를 참고한다.
3. System Context Diagram을 Mermaid로 작성한다.
4. Container Diagram을 Mermaid로 작성한다.
5. Module Boundary Diagram을 Mermaid로 작성한다.
6. Deployment Diagram을 Mermaid로 작성한다.
7. 프론트엔드가 여러 개인 경우 Frontend App Diagram을 작성한다.
8. 기능명세와 화면정의를 읽는다.
9. 도메인별 핵심 시퀀스 다이어그램을 Mermaid로 작성한다.
10. API 계약이 있으면 시퀀스와 API ID를 연결한다.

## 5. 아키텍처 다이어그램 필수 포함

```text
1. System Context Diagram
   - 사용자 유형, 외부 시스템, 서비스 관계

2. Container Diagram
   - frontend, backend, DB, storage, external API, batch, queue

3. Module Boundary Diagram
   - 도메인별 내부 모듈 경계와 의존

4. Deployment Diagram
   - 실제 배포 인프라 구조
```

필요시 추가:

```text
5. Data Flow Diagram
6. Security Boundary Diagram
7. Frontend App Architecture Diagram
8. Event / Async Flow Diagram
```

## 6. 시퀀스 다이어그램 작성 기준

대표 시퀀스 하나만 만들지 않는다. 도메인별 핵심 흐름을 작성한다.

반드시 작성하는 흐름:

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

시퀀스 ID 체계:

```text
SEQ-{DOMAIN}-{SEQ}

예:
SEQ-AUTH-001 이메일 회원가입
SEQ-AUTH-002 로그인
SEQ-RESERVATION-001 예약 생성
SEQ-PAYMENT-001 결제 요청
```

기능명세/API 계약과의 연결:

```text
FUNC-{DOMAIN}-{FEATURE}-{SEQ}
→ SCREEN-{DOMAIN}-{NAME}
→ SEQ-{DOMAIN}-{SEQ}
→ API-{DOMAIN}-{SEQ}
→ tables
→ TASK
```

## 7. 파일 구조

초기에는 단일 파일 + 도메인별 섹션:

```text
docs/04_architecture/architecture_diagrams.md
docs/04_architecture/sequence_diagrams.md
```

커졌을 때 디렉터리 분리:

```text
docs/04_architecture/sequence/<domain>.md
```

## 8. 금지

- 소스 코드를 작성하지 않는다.
- 기능명세 없이 시퀀스 다이어그램을 작성하지 않는다.
- 텍스트만으로 아키텍처를 완료 처리하지 않는다.
