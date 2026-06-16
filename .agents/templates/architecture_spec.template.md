# Architecture Specification

## Metadata

| Field | Value |
|---|---|
| Version | v1 |
| Created At | YYYY-MM-DD |
| Updated At | YYYY-MM-DD |
| Status | DRAFT / REVIEW / APPROVED |

---

# System Architecture

## 기술 스택

| 계층 | 기술 | 비고 |
|---|---|---|
| Frontend |  |  |
| Backend |  |  |
| Database |  |  |
| Infra |  |  |

## 시스템 구성도

```mermaid
graph TB
    subgraph Client
    end
    subgraph Server
    end
    subgraph Database
    end
```

---

# Module Boundaries

## 모듈 목록

| 모듈 | 도메인 | 책임 | 의존 |
|---|---|---|---|
|  |  |  |  |

## 모듈 간 통신

-

---

# Runtime Flow

## 요청 처리 흐름

```text
Client → API Gateway → Controller → Service → Repository → Database
```

## 인증 흐름

-

## 에러 처리 흐름

-

---

# Sequence Diagrams

도메인별 핵심 흐름을 작성한다. 대표 시퀀스 하나만 만들지 않는다.

별도 다이어그램 파일: `docs/04_architecture/architecture_diagrams.md`

## [도메인명]

### SEQ-{DOMAIN}-001 [흐름명]

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database
```

| 연결 | ID |
|---|---|
| 관련 기능 ID |  |
| 관련 화면 ID |  |
| 관련 API ID |  |

## Notes

-
