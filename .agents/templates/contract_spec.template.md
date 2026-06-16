# Contract Specification

## Metadata

| Field | Value |
|---|---|
| Version | v1 |
| Created At | YYYY-MM-DD |
| Updated At | YYYY-MM-DD |
| Status | DRAFT / REVIEW / APPROVED |

---

# API Contract

## API 목록

| API ID | 메서드 | 엔드포인트 | 기능 ID | SEQ ID | 설명 |
|---|---|---|---|---|---|
| API-{DOMAIN}-001 |  |  |  |  |  |

## API-{DOMAIN}-001

### Request

| Field | Type | Required | Description |
|---|---|---|---|
|  |  |  |  |

### Response (Success)

```json
{
}
```

### Response (Error)

| 에러 코드 | HTTP Status | 설명 |
|---|---|---|
|  |  |  |

---

# ERD

```mermaid
erDiagram
```

---

# Table Specification

## [테이블명]

| 컬럼 | 타입 | Null | Default | PK/FK | 설명 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 인덱스

| 인덱스명 | 컬럼 | 유형 |
|---|---|---|
|  |  |  |

---

# State Model

## [엔티티명] 상태 전이

```mermaid
stateDiagram-v2
```

| 이전 상태 | 이벤트 | 이후 상태 | 조건 |
|---|---|---|---|
|  |  |  |  |

---

# Error Specification

## 에러 코드 체계

```text
{DOMAIN}-{CATEGORY}-{SEQ}

예: AUTH-VALIDATION-001
```

## 에러 목록

| 에러 코드 | HTTP Status | 메시지 | 설명 | 관련 기능 ID |
|---|---|---|---|---|
|  |  |  |  |  |
