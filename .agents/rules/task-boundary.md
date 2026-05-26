---
trigger: always_on
---

# Task Boundary Rule

## 목적

이 규칙은 Antigravity CLI가 TASK 범위를 벗어난 작업을 수행하지 않도록 제한한다.

이 저장소의 실제 작업 단위는 반드시 다음 파일이다.

```text
ops/tasks/TASK-xxx.md
```

Antigravity 내부의 `task.md`, task list, `implementation_plan.md`, `walkthrough.md`는 보조 artifact일 뿐이다.

## 기본 원칙

- 한 번에 하나의 TASK만 실행한다.
- TASK 파일에 명시된 작업만 수행한다.
- TASK 범위를 임의로 확장하지 않는다.
- TASK에 없는 요구사항을 만들지 않는다.
- TASK에 없는 리팩터링을 하지 않는다.
- TASK에 없는 문서 수정을 하지 않는다.
- TASK에 없는 파일 이동, 파일명 변경, 삭제를 하지 않는다.

## 기준 파일

작업 시작 전 반드시 다음 파일을 읽는다.

```text
AGENTS.md
ops/tasks/TASK-xxx.md
```

Antigravity 작업에서는 추가로 다음 rules를 따른다.

```text
.agents/rules/**
```

## allowed files 규칙

TASK의 `allowed files`에 명시된 파일만 수정할 수 있다.

allowed files가 디렉터리 단위로 지정된 경우 해당 디렉터리 내부만 수정할 수 있다.

allowed files가 명시되지 않았거나 모호하면 작업을 중단하고 보고한다.

단, TASK 로그 파일은 예외적으로 다음 경로에 생성 또는 갱신할 수 있다.

```text
ops/logs/TASK-xxx.log.md
```

## forbidden files 규칙

TASK의 `forbidden files`에 명시된 파일은 절대 수정하지 않는다.

forbidden files가 디렉터리 단위로 지정된 경우 해당 디렉터리 내부를 수정하지 않는다.

forbidden files 수정이 필요해 보이면 작업을 중단하고 사용자에게 보고한다.

## 문서 수정 제한

TASK가 명시적으로 허용하지 않으면 다음 문서 영역을 수정하지 않는다.

```text
docs/01_overview/**
docs/02_product/**
docs/03_requirements/**
docs/04_architecture/**
docs/05_contracts/**
docs/06_dev/**
docs/07_test_qa/**
docs/08_ops/**
docs/09_pm/**
```

특히 다음 문서는 TASK가 허용한 경우에만 수정한다.

```text
docs/04_architecture/adrs/**
docs/05_contracts/**
docs/09_pm/wbs/**
```

## 관련 없는 변경 금지

다음 변경은 TASK 범위에 명시되지 않았다면 금지한다.

- 대규모 리팩터링
- 디렉터리 구조 변경
- 파일명 변경
- 파일 이동
- 포맷터 일괄 적용
- 의존성 추가
- 설정 파일 변경
- 빌드 시스템 변경
- 테스트 프레임워크 변경
- API 계약 변경
- DB 스키마 변경
- 마이그레이션 변경
- UI 디자인 토큰 변경

## 미커밋 변경사항 보호

작업 시작 전 반드시 다음 명령을 실행한다.

```bash
git status --short
```

관련 없는 미커밋 변경사항이 있으면 작업을 중단하고 보고한다.

사용자의 기존 변경사항을 덮어쓰거나 되돌리지 않는다.

## TASK 계약 추출

작업 시작 시 TASK에서 다음 항목을 추출한다.

- TASK ID
- WBS ID
- objective
- source context
- allowed files
- forbidden files
- implementation requirements
- acceptance criteria
- verification commands
- commit rule

이 항목 중 핵심 정보가 누락되어 있으면 임의로 보완하지 말고 보고한다.

## 완료 조건

TASK는 다음 조건을 만족해야 완료할 수 있다.

- allowed files 안에서만 수정했다.
- forbidden files를 수정하지 않았다.
- TASK 요구사항을 충족했다.
- acceptance criteria를 충족했다.
- verification commands를 실행했다.
- 검증 결과가 PASS다.
- 리뷰 결과가 PASS 또는 PASS_WITH_NOTES다.
- 실행 로그를 작성 또는 갱신했다.

## 위반 시 처리

TASK 범위 위반이 발견되면 다음 순서로 처리한다.

1. 즉시 작업을 중단한다.
2. 위반 파일을 보고한다.
3. 위반 사유를 설명한다.
4. 수정 또는 되돌림이 필요한 경우 사용자 승인을 요청한다.
5. 승인 없이 파괴적 복구 작업을 수행하지 않는다.