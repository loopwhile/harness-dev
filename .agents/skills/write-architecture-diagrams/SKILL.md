---
name: write-architecture-diagrams
description: 텍스트 아키텍처를 Mermaid 아키텍처 다이어그램으로 변환한다.
---

# Write Architecture Diagrams Skill

## 1. 목적

이 스킬은 텍스트 기반 아키텍처 문서를 Mermaid 아키텍처 다이어그램으로 시각화한다.

시퀀스 다이어그램은 `write-sequence-diagrams` 스킬이 담당한다.

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

## 4. 절차

1. 아키텍처 문서를 읽는다. (system_architecture.md, module_boundaries.md, runtime_flow.md)
2. `.agents/templates/architecture_diagrams.template.md`를 참고한다.
3. System Context Diagram을 Mermaid로 작성한다.
4. Container Diagram을 Mermaid로 작성한다.
5. Module Boundary Diagram을 Mermaid로 작성한다.
6. Deployment Diagram을 Mermaid로 작성한다.
7. 프론트엔드가 여러 개인 경우 Frontend App Diagram을 작성한다.

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

## 6. 금지

- 소스 코드를 작성하지 않는다.
- 시퀀스 다이어그램을 이 스킬에서 작성하지 않는다. `write-sequence-diagrams`를 사용한다.
- 텍스트만으로 아키텍처를 완료 처리하지 않는다.
- 텍스트 아키텍처 문서 없이 다이어그램을 작성하지 않는다.
