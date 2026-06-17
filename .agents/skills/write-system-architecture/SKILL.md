---
name: write-system-architecture
description: 시스템 아키텍처, 모듈 경계, 런타임 흐름 문서를 작성한다.
---

# Write System Architecture Skill

## 1. 목적

이 스킬은 기능명세, 화면정의, 제품 정의를 기반으로 시스템 아키텍처, 모듈 경계, 런타임 흐름 문서를 작성한다.

Mode 2. Planning / Specification Mode에서 사용한다.

아키텍처 다이어그램(write-architecture-diagrams)과 시퀀스 다이어그램(write-sequence-diagrams)의 입력이 되는 텍스트 아키텍처 문서를 생성한다.

## 2. 입력

- docs/01_overview/project_overview.md
- docs/02_product/product_brief.md
- docs/02_product/prd.md
- docs/02_product/scope.md
- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/03_requirements/user_flows.md
- docs/06_design/DESIGN.md (있는 경우)
- docs/06_design/ui_handoff/<domain>.md (있는 경우)

## 3. 출력

| 산출물 | 경로 |
|---|---|
| 시스템 아키텍처 | docs/04_architecture/system_architecture.md |
| 모듈 경계 | docs/04_architecture/module_boundaries.md |
| 런타임 흐름 | docs/04_architecture/runtime_flow.md |

## 4. 절차

1. 프로젝트 개요와 제품 정의를 읽는다.
2. 기능명세와 화면정의를 읽는다.
3. `.agents/templates/system_architecture.template.md`를 참고한다.
4. 기술 스택을 정리한다.
5. 시스템 구성도를 작성한다.
6. 배포 구조를 정리한다.
7. `.agents/templates/module_boundaries.template.md`를 참고한다.
8. 도메인별 모듈 목록을 정의한다.
9. 모듈 간 의존/통신을 정리한다.
10. `.agents/templates/runtime_flow.template.md`를 참고한다.
11. 요청 처리 흐름을 정리한다.
12. 인증/인가 흐름을 정리한다.
13. 에러 처리 흐름을 정리한다.
14. 비동기/배치 흐름이 있으면 정리한다.

## 5. system_architecture.md 필수 내용

```text
1. 기술 스택 (계층별)
2. 시스템 구성도 (텍스트 또는 간략 Mermaid)
3. 배포 구조
4. 외부 연동
5. 보안 기준
6. 성능/확장성 고려사항
```

## 6. module_boundaries.md 필수 내용

```text
1. 모듈 목록 (도메인, 책임, 의존)
2. 모듈 간 통신 방식
3. 공유 모듈 정책
4. 모듈 분리 원칙
```

## 7. runtime_flow.md 필수 내용

```text
1. 요청 처리 흐름 (Client → API → Service → Repository → DB)
2. 인증/인가 흐름
3. 에러 처리 흐름
4. 비동기/이벤트 흐름 (있는 경우)
5. 배치/스케줄러 흐름 (있는 경우)
```

## 8. 금지

- 소스 코드를 작성하지 않는다.
- 기능명세 없이 아키텍처를 작성하지 않는다.
- 아키텍처 다이어그램을 이 단계에서 완성하지 않는다. 텍스트 아키텍처만 작성한다.
- 시퀀스 다이어그램을 이 단계에서 작성하지 않는다.
- API/DB 계약을 이 단계에서 작성하지 않는다.
