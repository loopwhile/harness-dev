---
name: execute-task
description: Codex CLI 또는 Codex App에서 ops/tasks/TASK-xxx.md 하나를 역할별 runtime subagent로 실행한다. TASK 분석, 구현, 검증, 리뷰, 평가, 기록, 커밋까지 오케스트레이션한다.
---

# Execute Task Skill

## 1. 목적

이 스킬은 `ops/tasks/TASK-xxx.md` 파일 하나를 기준으로 전체 작업을 자율 실행한다.

이 스킬이 호출되면 **TASK Execution Mode**가 활성화된다.

메인 에이전트는 orchestrator 역할만 수행한다.

구현, 검증, 리뷰, 평가, 기록은 `.codex/config.toml`에 등록된 역할별 custom agent를 실제 runtime subagent로 spawn하여 수행한다.

### 실행 흐름

```text
Normal TASK (Mode 3A):
  orchestrator → implementer → verifier → reviewer → recorder → commit → user report

EVAL TASK (Mode 3B):
  orchestrator → verifier → evaluator → recorder → commit → user validation guide → STOP
```

## 2. 기본 원칙

TASK 범위, 허용/금지 파일, 사용자 승인 정책, 파괴성 작업 금지는 다음 규칙을 따른다.

- `AGENTS.md` §5, §8, §13, §14
- `.codex/rules/task-boundary.md`
- `.codex/rules/commit-policy.md`
- `.codex/rules/verification-policy.md`
- `.codex/rules/evaluation-policy.md`

이 스킬 고유의 추가 원칙은 다음과 같다.

- 메인 에이전트는 orchestrator 역할만 수행한다.
- 메인 에이전트가 implementer, verifier, reviewer, evaluator, recorder 역할을 직접 대행하지 않는다.
- 역할 이름만 바꾸면서 하나의 에이전트가 모든 단계를 수행하지 않는다.
- 역할별 custom agent를 실제 별도의 runtime subagent로 spawn한다.
- TASK가 작아도 필수 역할을 하나의 에이전트로 합치지 않는다.
- 이전 subagent가 완료된 뒤 다음 subagent를 실행한다.
- 필수 subagent를 spawn할 수 없으면 단일 에이전트로 대체하지 않고 `BLOCKED`로 보고한다.
- `FAIL` 또는 `BLOCKED` 상태에서는 커밋하지 않는다.
- 해당 TASK의 `ops/logs/TASK-xxx.log.md`는 실행 기록을 위한 implicit allowed file로 간주하며 recorder만 수정할 수 있다.
- 다른 TASK의 로그는 수정하지 않는다.

## 3. Runtime Subagent 규칙

### 3.1 진실 공급원

역할별 subagent 정의의 진실 공급원은 다음과 같다.

```text
.codex/config.toml           ← agent 등록 및 전역 설정
.codex/agents/<role>.toml    ← 역할별 시스템 프롬프트와 도구 정의
```

현재 Codex root/main thread가 orchestrator 역할을 수행한다.

`orchestrator` custom agent를 별도로 spawn하지 않는다.

root/main orchestrator가 implementer, verifier, reviewer, evaluator, recorder를 직접 spawn한다.

이 스킬은 Codex root/main thread에서만 실행한다.

implementer, verifier, reviewer, evaluator, recorder subagent는 `execute-task` 스킬을 다시 호출하거나 다른 역할의 subagent를 spawn하지 않는다.

역할별 subagent는 자신에게 지정된 역할만 수행하고 결과를 root/main orchestrator에게 반환한다.

orchestrator는 모든 subagent handoff에 다음 제한을 명시적으로 포함한다.

- 자신에게 지정된 역할만 수행한다.
- `execute-task` 스킬을 다시 호출하지 않는다.
- 다른 subagent를 spawn하지 않는다.
- 직접 커밋하지 않는다.
- 결과를 root/main orchestrator에게 반환한다.

### 3.2 실행 인정 조건

다음 조건을 모두 충족해야 역할이 실행된 것으로 인정한다.

- 역할별 별도 subagent가 실제 생성되었다.
- subagent에 TASK ID와 역할별 작업 범위가 전달되었다.
- subagent가 독립된 결과를 반환했다.
- orchestrator가 결과를 받은 뒤 다음 단계로 이동했다.

"이제 implementer 역할로 구현한다" 같은 텍스트 선언만으로는 실행으로 인정하지 않는다.

각 subagent를 spawn할 때 역할, TASK ID, 작업 범위, RUNNING 상태를 표시한다.

각 subagent가 완료되면 역할, 최종 상태, 핵심 결과, 다음 단계를 표시한다.

표시된 역할 상태는 실제 runtime subagent 실행 결과와 일치해야 한다.

### 3.3 역할 병합 금지

Normal TASK에서 implementer, verifier, reviewer, recorder는 각각 별도 subagent로 실행한다.

EVAL TASK에서 verifier, evaluator, recorder는 각각 별도 subagent로 실행한다.

다음은 금지한다.

- 서로 다른 역할을 하나의 subagent로 병합
- 메인 orchestrator가 역할을 대행
- TASK가 작다는 이유로 subagent 생략
- spawn 실패 후 단일 에이전트 방식으로 계속 진행

### 3.4 orchestrator의 책임 범위

orchestrator는 다음을 수행한다.

- TASK 파일 읽기 및 계약 추출
- 브랜치 및 git 상태 확인
- subagent 결정, spawn, 완료 대기
- 결과 확인 및 다음 단계 결정
- 실패 시 수정 단계로 반환
- 최종 diff/상태 확인, 커밋, 사용자 보고

orchestrator는 다음을 직접 수행하지 않는다.

- 구현/테스트 파일 작성 및 수정
- TASK에 정의된 빌드, 테스트, 린트, 타입 체크 verification commands 실행
- 독립적인 acceptance criteria 판정
- 독립 코드 리뷰
- 평가표 기반 평가
- TASK 실행 로그 작성

단, 최종 커밋 전 read-only 확인과 diff 무결성 확인은 허용한다.

- `git status --short`
- `git diff`
- `git diff --check`

## 4. 실행 준비 절차

1. `AGENTS.md`를 읽는다.
2. 지정된 TASK 파일을 읽는다.
3. `.codex/config.toml`을 읽고 필요한 custom agent 등록 여부를 확인한다.
4. TASK에서 다음 정보를 추출한다.
   - TASK ID, WBS ID, Domain, Branch, Type
   - objective, source context
   - allowed files, forbidden files
   - implementation requirements, acceptance criteria
   - verification commands, commit rule
   - evaluation scope, dependencies (EVAL TASK)
5. 현재 브랜치를 확인한다.
   ```bash
   git branch --show-current
   ```
6. TASK Branch와 불일치하면 `BLOCKED`로 보고하고 즉시 중단한다.
   - subagent를 spawn하지 않는다.
   - 파일을 수정하지 않는다.
   - 커밋하지 않는다.
7. `git status --short`로 현재 상태를 확인한다.
8. 관련 없는 미커밋 변경사항이 있으면 `BLOCKED`로 보고하고 즉시 중단한다.
   - subagent를 spawn하지 않는다.
   - 기존 변경사항을 수정하거나 정리하지 않는다.
   - 커밋하지 않는다.
9. TASK Type에 따라 분기한다.
   - `Type != eval` → Normal TASK Flow (§5)
   - `Type == eval` → EVAL TASK Flow (§6)

필수 agent가 등록되지 않았거나 spawn할 수 없으면 `BLOCKED`로 보고하고 즉시 중단한다. 메인 orchestrator가 해당 역할을 대행하지 않으며 파일을 수정하거나 커밋하지 않는다.

## 5. Normal TASK Flow (Mode 3A)

### 5.1 Implementer

`implementer` subagent를 spawn한다.

전달 정보: TASK 계약 전체 + 관련 문서/소스 경로 + 커밋 금지 지시.

implementer는 다음을 수행한다.

1. 필요한 문서와 소스 파일을 읽는다.
2. allowed files 안에서 구현한다.
3. 필요한 테스트를 추가하거나 수정한다.
4. 변경 파일과 구현 결과를 반환한다.

결과: `PASS | FAIL | BLOCKED`

`PASS`가 아니면 다음 역할을 실행하지 않고 중단한다.

### 5.2 Verifier

implementer `PASS` 후 `verifier` subagent를 spawn한다.

전달 정보: TASK 계약 + implementer 결과 + 변경 파일 목록 + TASK 구현/테스트 소스 수정 금지 + 검증 과정의 build/cache/temp 산출물 생성 허용 + 커밋 금지.

검증 과정에서 생성되는 build/cache/temp 산출물은 Git으로 추적되지 않는 생성물만 허용한다.

verification command가 tracked source, test, config 또는 document 파일을 변경하면 verifier는 해당 변경을 승인하지 않는다.

검증 명령 자체가 tracked 파일 수정을 요구하면 `BLOCKED`로 반환하거나 implementer 수정 단계가 필요하다고 보고한다.

verifier는 다음을 수행한다.

1. verification commands를 실제 실행한다.
2. acceptance criteria를 하나씩 확인한다.
3. 실행 명령, 결과, 성공 여부를 반환한다.

결과: `PASS | FAIL | BLOCKED`

`FAIL`이고 수정 가능하면 새로운 implementer → verifier 순서로 재실행한다.

`BLOCKED`이거나 수정 불가능하면 중단한다.

### 5.3 Reviewer

verifier `PASS` 후 `reviewer` subagent를 spawn한다.

전달 정보: TASK 계약 + implementer/verifier 결과 + 현재 git diff + 파일 수정 금지 + 커밋 금지.

reviewer는 다음을 확인한다.

- TASK 범위/allowed files/forbidden files 준수
- 요구사항 누락, 관련 없는 변경
- 보안/성능/아키텍처 위험
- 테스트/검증 누락, 유지보수성

결과: `PASS | PASS_WITH_NOTES | FAIL | BLOCKED`

`PASS_WITH_NOTES`는 커밋을 막지 않는 비차단성 의견이 있을 때만 사용한다.

`FAIL`이고 수정 가능하면 implementer → verifier → reviewer 순서로 재실행한다.

`BLOCKED`이거나 수정 불가능한 `FAIL`이면 recorder를 실행하지 않고 중단한다.

### 5.4 Recorder

verifier `PASS` + reviewer `PASS`/`PASS_WITH_NOTES` 후 `recorder` subagent를 spawn한다.

전달 정보: TASK 계약 + 변경 파일 목록 + implementer/verifier/reviewer 결과 + 로그 경로 + `ops/logs/TASK-xxx.log.md` 외 모든 파일 수정 금지 + 커밋 금지.

recorder는 `ops/logs/TASK-xxx.log.md`만 수정할 수 있다. 구현 파일, 테스트 파일, 설정 파일, 상위 문서 및 다른 TASK 로그는 수정하지 않는다.

recorder는 `ops/logs/TASK-xxx.log.md`에 다음을 기록한다.

- 구현 결과, 변경 파일, 변경 유형
- 검증 명령/결과, acceptance criteria 결과
- 리뷰 verdict, 남은 위험, 최종 TASK 상태

결과: `PASS | FAIL | BLOCKED`

`PASS`가 아니면 커밋하지 않는다.

### 5.5 커밋

모든 필수 subagent가 성공하면 orchestrator가 최종 확인 후 커밋한다.

```bash
git status --short
git diff --check
git diff
git diff --cached
```

orchestrator는 TASK allowed files와 해당 TASK 로그만 명시적으로 stage한다. `git add .` 또는 `git add -A`로 작업 트리 전체를 stage하지 않는다.

커밋 조건:

- implementer `PASS`
- verifier `PASS`
- verifier가 모든 acceptance criteria를 `PASS`로 판정함
- reviewer `PASS` 또는 `PASS_WITH_NOTES`
- recorder `PASS`
- allowed files 밖 변경 없음
- forbidden files 변경 없음
- 관련 없는 변경 없음
- TASK 로그 작성 완료
- TASK allowed files와 해당 TASK 로그 외의 tracked/untracked 변경 없음

커밋 메시지는 `.codex/rules/commit-policy.md`와 TASK의 commit rule을 따른다.

기본 형식: `TASK-XXX WBS-XX-XXX: short summary`

## 6. EVAL TASK Flow (Mode 3B)

EVAL TASK에서는 implementer를 사용하지 않으며 다음을 금지한다.

- 기능 구현, 리팩터링, 구현/테스트 파일 수정
- 누락 기능 자동 보완, 선행 TASK 자동 재실행

### 6.1 Verifier

`verifier` subagent를 spawn한다.

전달 정보: EVAL TASK 계약 + Evaluation Scope + 선행 TASK 목록/로그 + 구현/테스트 소스 수정 금지 + 검증 과정의 build/cache/temp 산출물 생성 허용 + 커밋 금지.

검증 과정에서 생성되는 build/cache/temp 산출물은 Git으로 추적되지 않는 생성물만 허용한다.

verification command가 tracked source, test, config 또는 document 파일을 변경하면 verifier는 해당 변경을 승인하지 않는다.

검증 명령 자체가 tracked 파일 수정을 요구하면 `BLOCKED`로 반환한다.

구현 또는 테스트 수정이 필요하면 현재 EVAL TASK에서 수정하지 않고 correction TASK 필요성을 보고한다.

verifier는 다음을 수행한다.

1. 선행 TASK 로그를 확인한다.
2. EVAL TASK에 정의된 통합 verification commands를 실제 실행한다.
3. 통합 acceptance criteria를 하나씩 확인한다.
4. 실행 명령, 결과, 주요 출력과 실패 원인을 반환한다.
5. 구현/테스트 소스는 수정하지 않는다.

결과: `PASS | FAIL | BLOCKED`

`PASS`가 아니면 evaluator를 실행하지 않고 중단한다.

### 6.2 Evaluator

verifier `PASS` 후 `evaluator` subagent를 spawn한다.

전달 정보: EVAL TASK 계약 + Evaluation Type/Scope + 평가 기준 + 선행 TASK 로그 + verifier 결과 + 파일 수정 금지 + 커밋 금지.

evaluator는 다음을 수행한다.

- 평가표 기반 품질 평가 및 기준별 근거 작성
- Critical Issues, Improvement Suggestions 정리
- User Validation Scenarios 작성

결과: `PASS | CONDITIONAL_PASS | FAIL | BLOCKED`

`FAIL` 또는 `BLOCKED`이면 correction TASK 필요 여부를 보고하고 중단한다.

### 6.3 Recorder

evaluator `PASS`/`CONDITIONAL_PASS` 후 `recorder` subagent를 spawn한다.

recorder는 `ops/logs/TASK-xxx.log.md`만 수정할 수 있다. 구현 파일, 테스트 파일, 설정 파일, 상위 문서 및 다른 TASK 로그는 수정하지 않는다.

recorder는 `ops/logs/TASK-xxx.log.md`에 다음을 기록한다.

- 통합 검증 결과, 평가 결과, evaluator verdict
- Critical Issues, Improvement Suggestions
- 사용자 검증 안내
- TASK Status: `DONE`, User Validation Status: `PENDING_USER_VALIDATION`

결과: `PASS | FAIL | BLOCKED`

`PASS`가 아니면 커밋하지 않는다.

### 6.4 커밋과 STOP

커밋 조건:

- verifier `PASS`
- evaluator `PASS` 또는 `CONDITIONAL_PASS`
- recorder `PASS`
- 평가 결과 및 사용자 검증 안내 기록 완료
- TASK Status가 `DONE`
- User Validation Status가 `PENDING_USER_VALIDATION`
- 구현/테스트 소스 파일 변경 없음
- TASK 로그 외의 tracked/untracked 변경 없음

커밋 후:

1. 사용자 검증 안내를 출력한다.
2. 다음 기능 그룹으로 진행하지 않고 즉시 STOP한다.
3. 사용자가 `APPROVED`를 명시한 뒤에만 다음 단계로 진행한다.

## 7. 실패 및 재시도 규칙

### Subagent spawn 실패

메인 에이전트가 해당 역할을 대신 수행하지 않는다.

TASK를 `BLOCKED`로 판정하고 실패한 역할과 원인을 보고한다.

이미 이전 subagent가 변경을 생성했다면 해당 변경을 임의로 되돌리지 않고 보존한다.

추가 파일 수정과 다음 역할 실행을 중단하며 커밋하지 않는다.

### Subagent 응답 실패

동일 역할의 새로운 subagent를 한 번 다시 spawn한다. 재시도 실패 시 `BLOCKED`로 판정한다. 메인 에이전트가 결과를 임의로 작성하지 않는다.

### 검증 또는 리뷰 실패

수정 가능하면 새로운 implementer → verifier (→ reviewer) 순서로 재실행한다. 통과 전에는 recorder와 commit을 실행하지 않는다.

### EVAL 실패

구현/테스트를 직접 수정하지 않는다. 선행 TASK를 자동 재실행하지 않는다. correction TASK 필요 여부를 보고하고 커밋하지 않는다.

### 수정 반복 제한

하나의 correction cycle은 실패 결과를 받은 뒤 새로운 implementer를 spawn하고, verifier 또는 reviewer가 다시 결과를 반환할 때까지의 과정을 의미한다.

동일 TASK에서 correction cycle은 총 2회까지만 허용한다.

두 번째 correction cycle 이후에도 verifier가 `PASS`하지 못하거나 reviewer가 `PASS` 또는 `PASS_WITH_NOTES`를 반환하지 못하면 TASK를 `BLOCKED`로 판정한다.

orchestrator는 동일한 실패를 무한 반복하지 않는다.

## 8. 완료 보고 형식

### Normal TASK

```text
TASK Execution Result

TASK ID:
WBS ID:
Domain:
Branch:
Status:

Subagents:
- implementer:
- verifier:
- reviewer:
- recorder:

Changed files:
Verification:
Acceptance criteria:
Review verdict:
Commit:
Remaining risks:
```

### EVAL TASK

```text
EVAL TASK Execution Result

TASK ID:
WBS ID:
Domain:
Branch:
Status:

Subagents:
- verifier:
- evaluator:
- recorder:

Evaluation verdict:
User validation status:
Commit:
User validation guide:
Next action: STOP until user APPROVED
```