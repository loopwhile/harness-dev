---
name: write-wbs
description: WBS를 도메인-기능-TASK 3계층으로 분해하고 EVAL TASK를 배치하는 표준 가이드다. ChatGPT, Codex, Antigravity 모두에서 참조한다.
---

# Write WBS Skill

## 1. 목적

이 스킬은 WBS(Work Breakdown Structure)를 작성할 때 따르는 표준 가이드다.

WBS는 다음 도구 모두에서 참조할 수 있다.

- 웹 ChatGPT (GitHub 연결 환경)
- Codex CLI / Codex App
- Antigravity CLI / Antigravity 2.0

## 2. WBS 분해 원칙

WBS는 아래 3계층으로 분해한다.

```text
Domain (WBS-XX)
└── Feature (WBS-XX-XXX)
    ├── Feature-internal TASK
    ├── Feature-internal TASK
    ├── Feature-internal TASK
    └── EVAL TASK: 기능 평가 및 사용자 검증 안내
```

### 2.1 Domain

비즈니스 도메인 단위다.

예시:

- 회원 도메인
- 결제 도메인
- 알림 도메인
- 관리자 도메인

### 2.2 Feature

도메인 안의 기능 단위다.

예시:

- 회원가입
- 로그인
- 비밀번호 재설정
- 프로필 관리

### 2.3 Feature-internal TASK

기능 안의 실행 가능한 작업 단위다.

일반적인 분해 순서:

1. 요청/응답 계약 정의
2. 백엔드 기본 흐름 구현
3. 예외/검증 처리
4. 프론트엔드 연결
5. 테스트 보강

순서는 기능 특성에 맞게 조정할 수 있다.

### 2.4 EVAL TASK

기능 마지막에 배치하는 평가 및 사용자 검증 TASK다.

EVAL TASK는 다음을 수행한다.

- 통합 검증
- 평가표 기반 품질 평가
- 사용자 검증 안내 생성

## 3. EVAL TASK 배치 규칙

1. **기능 마지막**: 기능 내 모든 TASK가 끝난 뒤 기능 EVAL TASK를 배치한다.
2. **도메인 마지막**: 도메인 내 모든 기능이 끝난 뒤 도메인 통합 EVAL TASK를 배치한다.
3. EVAL TASK의 Type은 반드시 `eval`로 표기한다.
4. EVAL TASK의 dependencies에는 해당 범위의 모든 선행 TASK를 명시한다.

## 4. TASK 번호 체계

도메인별로 TASK 번호 범위를 할당한다.

```text
WBS-01: TASK-001 ~ TASK-019
WBS-02: TASK-020 ~ TASK-039
WBS-03: TASK-040 ~ TASK-059
...
```

도메인 전체 EVAL TASK는 해당 범위의 마지막 번호 또는 999를 사용한다.

## 5. WBS 작성 절차

1. 프로젝트의 비즈니스 도메인을 식별한다.
2. 각 도메인에서 기능을 나열한다.
3. 각 기능을 실행 가능한 TASK로 분해한다.
4. 각 기능 마지막에 EVAL TASK를 배치한다.
5. 각 도메인 마지막에 도메인 통합 EVAL TASK를 배치한다.
6. TASK 간 의존성을 명시한다.
7. 우선순위를 할당한다.

## 6. TASK 분해 기준

TASK 하나가 다음 조건을 만족하도록 분해한다.

- 하나의 명확한 목표가 있다.
- 에이전트가 단일 실행으로 완료할 수 있는 크기다.
- acceptance criteria가 구체적으로 작성 가능하다.
- verification commands로 검증할 수 있다.
- 다른 TASK와 독립적이거나 의존성이 명확하다.

다음 경우에는 TASK를 더 분할한다.

- 수정 파일이 10개를 초과한다.
- 여러 계층(API, 서비스, 데이터, UI)을 동시에 변경한다.
- acceptance criteria가 5개를 초과한다.
- 서로 다른 검증 방법이 필요한 변경이 섞여 있다.

## 7. EVAL TASK 작성 규칙

EVAL TASK에는 다음 정보를 포함한다.

- Type: `eval`
- Evaluation Scope: 평가 대상 TASK 목록
- Evaluation Type: `feature_eval` / `domain_eval` / `epic_eval`
- Dependencies: 선행 TASK 전체
- Acceptance Criteria: 평가표 작성 완료, 사용자 검증 안내 생성 완료

EVAL TASK의 allowed files:

- `ops/logs/TASK-xxx.log.md`
- 선행 TASK 로그 파일 (읽기 전용)

EVAL TASK의 forbidden files:

- 소스 코드
- 테스트 코드
- 설정 파일
- 상위 문서

## 8. 출력 형식

WBS 작성 결과는 `ops/templates/wbs-feature-task.template.md` 형식을 따른다.

각 기능의 TASK 테이블에는 다음 열을 포함한다.

```text
| Order | TASK ID | Title | Type | Priority | Dependencies | Notes |
```

## 9. 예시

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

## 10. 하드 룰

- EVAL TASK 없이 기능을 닫지 않는다.
- 도메인 통합 EVAL TASK 없이 도메인을 닫지 않는다.
- EVAL TASK의 Type은 반드시 `eval`이다.
- EVAL TASK에서 구현을 수행하지 않는다.
- TASK 분해 시 하나의 TASK가 여러 기능에 걸치지 않도록 한다.
- TASK 번호는 도메인별 할당 범위 안에서 사용한다.
- 도메인, 기능, TASK 간 계층 구조를 깨뜨리지 않는다.
