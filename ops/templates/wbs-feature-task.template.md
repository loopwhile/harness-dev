# WBS-XX [도메인명]

## Metadata

| Field | Value |
|---|---|
| WBS ID | WBS-XX |
| Domain |  |
| Created At | YYYY-MM-DD |
| Updated At | YYYY-MM-DD |
| Status | TODO |

## WBS 분해 구조

WBS는 아래 3계층으로 분해한다.

```text
Domain (WBS-XX)
└── Feature (WBS-XX-XXX)
    ├── Feature-internal TASK (계약, 백엔드, 프론트엔드, 테스트 등)
    ├── Feature-internal TASK
    ├── Feature-internal TASK
    └── EVAL TASK: 기능 평가 및 사용자 검증 안내
```

도메인 마지막에는 도메인 전체 통합 EVAL TASK를 배치한다.

---

## WBS-XX-001 [기능명]

| Order | TASK ID | Title | Type | Priority | Dependencies | Notes |
|---:|---|---|---|---|---|---|
| 1 | TASK-XXX | 요청/응답 계약 정의 | feature | P1 |  |  |
| 2 | TASK-XXX | 백엔드 기본 흐름 구현 | feature | P1 | TASK-XXX |  |
| 3 | TASK-XXX | 예외/검증 처리 | feature | P1 | TASK-XXX |  |
| 4 | TASK-XXX | 프론트엔드 연결 | feature | P2 | TASK-XXX |  |
| 5 | TASK-XXX | 테스트 보강 | test | P2 | TASK-XXX |  |
| 6 | TASK-XXX | EVAL: [기능명] 평가 및 사용자 검증 안내 | eval | P1 | TASK-XXX ~ TASK-XXX |  |

---

## WBS-XX-002 [기능명]

| Order | TASK ID | Title | Type | Priority | Dependencies | Notes |
|---:|---|---|---|---|---|---|
| 1 | TASK-XXX |  | feature | P1 |  |  |
| 2 | TASK-XXX |  | feature | P1 | TASK-XXX |  |
| N | TASK-XXX | EVAL: [기능명] 평가 및 사용자 검증 안내 | eval | P1 | 선행 TASK 전부 |  |

---

## WBS-XX-999 EVAL: [도메인명] 전체 통합 평가 및 사용자 검증 안내

| Order | TASK ID | Title | Type | Priority | Dependencies | Notes |
|---:|---|---|---|---|---|---|
| 1 | TASK-XXX | EVAL: [도메인명] 전체 통합 평가 및 사용자 검증 안내 | eval | P1 | 도메인 내 모든 TASK |  |

---

## TASK 번호 체계

```text
WBS-01: TASK-001 ~ TASK-019
WBS-02: TASK-020 ~ TASK-039
WBS-03: TASK-040 ~ TASK-059
...
```

도메인 전체 EVAL TASK는 해당 WBS 번호 범위의 마지막 번호(예: TASK-019, TASK-039)를 사용하거나 999를 사용한다.

## EVAL TASK 배치 규칙

1. 기능 마지막에 기능 EVAL TASK를 배치한다.
2. 도메인 마지막에 도메인 통합 EVAL TASK를 배치한다.
3. EVAL TASK의 dependencies에는 해당 범위의 모든 선행 TASK를 명시한다.
4. EVAL TASK의 Type은 반드시 `eval`로 표기한다.

## 예시

```text
WBS-02 회원 도메인

WBS-02-001 회원가입 기능
  TASK-021 회원가입 요청/응답 계약 정의
  TASK-022 회원가입 백엔드 기본 흐름 구현
  TASK-023 회원가입 예외/검증 처리
  TASK-024 회원가입 프론트엔드 연결
  TASK-025 회원가입 테스트 보강
  TASK-026 EVAL: 회원가입 기능 평가 및 사용자 검증 안내

WBS-02-002 로그인 기능
  TASK-027 로그인 요청/응답 계약 정의
  TASK-028 로그인 백엔드 구현
  TASK-029 로그인 프론트엔드 연결
  TASK-030 로그인 인증 상태 처리
  TASK-031 로그인 테스트 보강
  TASK-032 EVAL: 로그인 기능 평가 및 사용자 검증 안내

WBS-02-999 EVAL: 회원 도메인 전체 통합 평가 및 사용자 검증 안내
```
