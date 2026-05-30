# AGENTS.md

## 1. 프로젝트 목적

이 저장소는 AI 하네스 엔지니어링을 위한 표준 프로젝트 템플릿이다.

목표는 다음과 같다.

1. 웹브라우저 ChatGPT에서 상위 문서와 WBS를 작성한다.
2. Codex CLI, Antigravity CLI 같은 로컬 AI 개발 도구는 TASK 단위로만 작업한다.
3. 각 TASK는 `ops/tasks/TASK-xxx.md` 파일 하나로 정의한다.
4. 작업은 오케스트레이션 에이전트가 관리한다.
5. 구현, 검증, 리뷰, 기록은 각각 분리된 에이전트 또는 스킬이 담당한다.
6. 모든 완료 작업은 TASK 번호와 WBS 번호가 포함된 커밋으로 닫는다.
7. 기능 완료 시점에 EVAL TASK로 품질 평가와 사용자 검증 게이트를 운영한다.

## 2. 진실 공급원

이 프로젝트의 진실 공급원은 다음 순서를 따른다.

1. `docs/`  
   제품, 요구사항, 아키텍처, 계약, 개발, 테스트, 운영, PM 문서

2. `docs/09_pm/wbs/`  
   WBS 항목과 작업 분해 기준

3. `ops/tasks/TASK-xxx.md`  
   실제 CLI 에이전트가 실행할 단위 작업

4. `ops/logs/`  
   TASK 실행 결과, 검증 증거, 리뷰 결과, 커밋 기록

## 3. 기본 작업 흐름

모든 TASK는 다음 순서로 진행한다.

1. 오케스트레이션 에이전트가 TASK 파일을 읽는다.
2. 오케스트레이션 에이전트가 TASK 범위, 허용 파일, 금지 파일, 검증 기준을 확인한다.
3. 구현 에이전트가 허용된 범위 안에서만 수정한다.
4. 검증 에이전트가 테스트, 린트, 빌드, 수동 검증 기준을 확인한다.
5. 리뷰 에이전트가 diff, 범위 이탈, 위험 요소를 검토한다.
6. 기록 에이전트가 `ops/logs/`에 실행 기록을 남긴다.
7. 오케스트레이션 에이전트가 최종 커밋을 생성한다.

EVAL TASK의 경우 다음 순서로 진행한다.

1. 오케스트레이션 에이전트가 EVAL TASK를 읽는다.
2. 통합 검증을 수행한다.
3. 평가 에이전트가 평가표 기반 평가를 수행한다.
4. 평가 에이전트가 사용자 검증 안내를 생성한다.
5. 기록 에이전트가 평가 결과와 사용자 검증 안내를 기록한다.
6. EVAL TASK를 커밋한다.
7. 사용자 검증 안내를 출력하고 중단한다.
8. 사용자 APPROVED 후 다음 기능 그룹으로 진행한다.

## 4. 작업 경계 규칙

다음 규칙은 반드시 지킨다.

- 명시적인 `ops/tasks/TASK-xxx.md` 없이 작업하지 않는다.
- 한 번에 하나의 TASK만 실행한다.
- TASK에 명시되지 않은 파일을 수정하지 않는다.
- `docs/01_overview`부터 `docs/09_pm`까지의 상위 문서는 TASK에서 허용한 경우에만 수정한다.
- 요구사항을 임의로 만들지 않는다.
- 대규모 리팩터링을 임의로 수행하지 않는다.
- TASK 범위를 벗어난 개선 작업을 끼워 넣지 않는다.
- 검증을 생략하지 않는다.
- 검증 또는 리뷰가 실패하면 커밋하지 않는다.

## 5. 커밋 규칙

TASK 완료 커밋은 반드시 TASK 번호를 포함한다.

권장 형식:

```text
TASK-001 WBS-01-001: implement login API boundary
```

문서 작업의 경우:

```text
TASK-002 WBS-01-002: update API contract template
```

## 6. 완료 기준

TASK는 다음 조건을 모두 만족해야 완료로 본다.

- TASK의 acceptance criteria가 충족됨
- 검증 명령 또는 검증 기준이 실행됨
- 검증 결과가 기록됨
- 리뷰 결과가 기록됨
- `ops/logs/TASK-xxx.log.md`가 생성 또는 갱신됨
- 최종 커밋 메시지에 TASK 번호가 포함됨
- 가능하면 WBS 번호도 커밋 메시지에 포함됨
- 관련 없는 변경사항이 남아 있지 않음

## 7. 주요 디렉터리

| 경로 | 역할 |
|---|---|
| `.agents/skills/` | 공통 에이전트 스킬 원본 |
| `.codex/agents/` | Codex 전용 custom subagent 정의 |
| `.codex/hooks/` | Codex lifecycle hook 스크립트 |
| `.codex/rules/` | 사람이 읽는 Codex 작업 정책 문서. 실행 정책은 별도 Codex Rules 또는 Hooks로 관리 |
| `docs/` | 프로젝트 상위 문서 |
| `docs/09_pm/wbs/` | WBS 문서 |
| `ops/tasks/` | 실행 가능한 TASK 파일 |
| `ops/logs/` | TASK 실행 기록 |
| `ops/templates/` | TASK, queue, log, 평가표, 사용자 검증, WBS 분해 템플릿 |
| `.agents/agents/evaluator/` | Antigravity evaluator 에이전트 정의 |
| `.codex/agents/evaluator.toml` | Codex evaluator 에이전트 정의 |

## 8. 기본 에이전트 행동

에이전트는 다음 순서로 행동한다.

1. 먼저 `AGENTS.md`를 확인한다.
2. 그 다음 지정된 TASK 파일을 확인한다.
3. TASK가 참조하는 WBS, 요구사항, 계약, 아키텍처 문서만 읽는다.
4. 필요한 소스 파일만 읽는다.
5. 허용된 파일만 수정한다.
6. 검증 결과를 명확히 남긴다.
7. 최종 보고 전에 git diff와 git status를 확인한다.

## 9. 금지 사항

- TASK 없이 임의 작업 금지
- 허용 파일 외 수정 금지
- 상위 문서 임의 수정 금지
- 임의 요구사항 생성 금지
- 검증 없는 완료 처리 금지
- 실패한 작업 커밋 금지
- 여러 TASK를 하나의 커밋에 섞기 금지

## 삭제 및 파괴성 작업 승인 규칙

에이전트는 TASK 범위 안에서 일반적인 읽기, 수정, 생성, 테스트, 빌드, 검증, 기록, 커밋은 자율적으로 진행할 수 있다.

다만 아래 작업은 반드시 사용자에게 먼저 확인해야 한다.

- 파일 삭제
- 디렉터리 삭제
- `rm`
- `rm -r`
- `rm -rf`
- `rmdir`
- `unlink`
- `git rm`
- `git clean`
- `git reset --hard`
- force push
- migration rollback
- 데이터베이스 삭제
- 테이블 삭제
- 대량 파일 이동
- 대량 파일명 변경
- TASK allowed files 밖의 변경
- TASK 범위를 넘어서는 구조 변경

삭제가 필요한 경우 에이전트는 다음 형식으로 사용자에게 질문한다.

```text
삭제 승인이 필요합니다.

대상:
- path/to/file

이유:
- 삭제가 필요한 이유

진행해도 될까요?
```

사용자 승인이 없으면 삭제 또는 파괴성 작업을 진행하지 않는다.

## Evaluation and User Validation Policy

Full evaluation and user validation are not required for every TASK.

Each normal TASK must still pass:

- implementation boundary check
- verification
- review
- execution logging
- commit rule

Full evaluation is required at feature completion checkpoints.

Feature completion checkpoints are represented as explicit EVAL TASKs.

Examples:

- TASK-026 EVAL: 회원가입 기능 평가 및 사용자 검증 안내
- TASK-032 EVAL: 로그인 기능 평가 및 사용자 검증 안내
- TASK-099 EVAL: 회원 도메인 전체 통합 평가 및 사용자 검증 안내

User validation is required only after a feature-level or WBS-level EVAL TASK.

The agent must not continue to the next feature group until user validation is APPROVED.

EVAL TASK는 평가 완료 시점에 평가 로그와 사용자 검증 안내를 커밋한다.

커밋하되 TASK 상태를 `PENDING_USER_VALIDATION`으로 남긴다.

사용자가 APPROVED를 명시하기 전까지 다음 feature group 또는 WBS group으로 진행하지 않는다.