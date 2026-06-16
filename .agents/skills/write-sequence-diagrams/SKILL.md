---
name: write-sequence-diagrams
description: 핵심 사용자 흐름과 시스템 흐름을 Mermaid 시퀀스 다이어그램으로 작성한다.
---

# Write Sequence Diagrams Skill

## 1. 목적

이 스킬은 기능명세와 화면정의를 기반으로 핵심 흐름의 시퀀스 다이어그램을 작성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

## 2. 입력

- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/03_requirements/user_flows.md
- docs/04_architecture/system_architecture.md (있는 경우)

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
3. 핵심 사용자 흐름을 식별한다.
4. 각 흐름의 Mermaid 시퀀스 다이어그램을 작성한다.
5. 시스템 아키텍처를 보강한다. (없으면 초안 작성)
6. 모듈 경계를 정의한다.
7. 런타임 흐름을 정리한다.

## 5. 대상 흐름 예시

```text
회원가입
로그인
비밀번호 재설정
예약 생성
결제
환불
관리자 승인
알림 발송
배치 처리
```

## 6. 금지

- 소스 코드를 작성하지 않는다.
- 기능명세 없이 다이어그램을 작성하지 않는다.
