---
name: antigravity-execute-task
description: Antigravity CLI에서 ops/tasks/TASK-xxx.md 하나를 기준으로 네이티브 custom subagent를 호출해 구현, 검증, 리뷰, 평가, 기록, 커밋 흐름을 통제한다.
---

# Antigravity Execute Task Skill

## 1. 목적

이 스킬은 Antigravity CLI에서 `ops/tasks/TASK-xxx.md` 하나를 기준으로 TASK Execution Mode를 실행하기 위한 절차다.

이 저장소의 실제 작업 단위는 Antigravity 내부 artifact가 아니라 반드시 `ops/tasks/TASK-xxx.md`다.

Antigravity가 생성하는 `task.md`, `implementation_plan.md`, `walkthrough.md`, 내부 task list, brain 파일은 보조 산출물로만 취급한다.

최종 실행 기록은 반드시 다음 경로에 남긴다.

```text
ops/logs/TASK-xxx.log.md
```

## 2. 진실 공급원

작업을 시작하기 전에 다음을 확인한다.

```text
AGENTS.md
.agents/rules/**
.agents/agents/<role>/agent.md
ops/tasks/TASK-xxx.md
```

역할별 시스템 프롬프트와 도구 권한의 진실 공급원은 `.agents/agents/<role>/agent.md`다.

Antigravity는 다음 경로의 custom agent를 자동 탐색한다.

```text
.agents/agents/<name>.md
.agents/agents/<name>/agent.md
```

이 저장소는 두 번째 형식을 표준으로 사용한다.

## 3. 기본 원칙

- 단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.
- TASK 파일에 없는 요구사항을 임의로 만들지 않는다.
- TASK 범위를 임의로 확장하지 않는다.
- TASK의 `allowed files` 안에서만 수정한다.
- TASK의 `forbidden files`는 절대 수정하지 않는다.
- TASK가 명시적으로 허용하지 않으면 `docs/01_overview`부터 `docs/09_pm`까지 수정하지 않는다.
- 관련 없는 리팩터링, 포맷팅, 파일 이동 또는 이름 변경을 하지 않는다.
- 검증 없이 완료 처리하지 않는다.
- Normal TASK는 리뷰 없이 커밋하지 않는다.
- 실행 기록 없이 완료 처리하지 않는다.
- 검증과 리뷰가 통과한 경우에만 커밋한다.

## 4. TASK 실행 중 사용자 승인 없이 허용하는 작업

TASK의 allowed files 범위 안에서 다음 작업은 사용자에게 묻지 않고 진행한다.

- 파일 생성/수정/삭제/이동/이름 변경
- 디렉터리 생성/정리
- 테스트 파일 추가/수정/삭제
- 테스트/빌드/린트/타입 체크
- `git status`, `git diff`, `git add`, `git commit`, `git restore --staged`
- 해당 TASK의 실행 로그 작성/수정

## 5. 절대 금지 또는 사용자 승인 필요

- 프로젝트 루트 밖 파일 생성/수정/삭제
- 프로젝트 루트 전체 삭제
- `.git` 디렉터리 삭제
- `rm -rf /`, `rm -rf .`, `rm -rf ..`, `rm -rf ./*`
- `git clean -fdx`
- `git reset --hard`
- `git push --force`
- 원격 브랜치 삭제
- DB drop, 테이블 drop
- TASK allowed files 밖의 파일 변경

## 6. 네이티브 custom subagent 운영 방식

### 6.1 고정 역할

TASK Execution Mode의 고정 역할은 다음 manifest를 사용한다.

| 역할 | manifest | mainAgent | subagent |
|---|---|---:|---:|
| orchestrator | `.agents/agents/orchestrator/agent.md` | true | false |
| implementer | `.agents/agents/implementer/agent.md` | false | true |
| verifier | `.agents/agents/verifier/agent.md` | false | true |
| reviewer | `.agents/agents/reviewer/agent.md` | false | true |
| evaluator | `.agents/agents/evaluator/agent.md` | false | true |
| recorder | `.agents/agents/recorder/agent.md` | false | true |

메인/root thread는 orchestrator 책임을 수행하며 `orchestrator`를 subagent로 spawn하지 않는다.

### 6.2 실행 전 가용성 검사

Normal TASK에서는 다음 manifest가 모두 존재하고 `subagent: true`여야 한다.

```text
implementer
verifier
reviewer
recorder
```

EVAL TASK에서는 다음 manifest가 모두 존재하고 `subagent: true`여야 한다.

```text
verifier
evaluator
recorder
```

manifest가 없거나 이름이 불일치하거나 필수 역할을 호출할 수 없으면 `BLOCKED`로 중단한다.

### 6.3 invoke_subagent 호출 규칙

고정 역할은 Antigravity의 `invoke_subagent`로 호출한다.

호출 시 각 subagent spec은 다음 의미를 만족해야 한다.

```text
Role: 역할명
TypeName: `.agents/agents/<role>/agent.md`의 name 값
Prompt: TASK별 역할 작업 범위와 필요한 컨텍스트
Workspace: inherit
```

예시 개념:

```text
invoke_subagent
  Role: implementer
  TypeName: implementer
  Workspace: inherit
  Prompt: TASK ID, objective, allowed files, forbidden files, implementation requirements, acceptance criteria 전달
```

`Workspace: inherit`를 사용해 동일 작업 디렉터리와 브랜치에서 순차적으로 handoff한다.

subagent는 부모 대화 기록을 그대로 상속하지 않으므로 Prompt에 해당 역할이 실제로 필요한 TASK 컨텍스트를 명시적으로 전달한다.

### 6.4 고정 역할 재정의 금지

다음 역할을 `define_subagent`로 다시 만들지 않는다.

```text
implementer
verifier
reviewer
evaluator
recorder
```

이 역할들의 시스템 프롬프트와 도구 권한은 `agent.md`가 유일한 진실 공급원이다.

`define_subagent`는 저장소에 영구 manifest가 없는 일회성 보조 역할에만 사용할 수 있다.

일회성 역할은 필수 역할을 대체하거나 병합해서는 안 되며, TASK Execution Mode에서 사용할 경우 TASK 범위와 allowed files 정책을 그대로 따라야 한다.

### 6.5 비동기 실행과 순서 통제

Antigravity subagent는 비동기로 실행될 수 있지만 이 하네스의 필수 단계는 순차적으로 완료한다.

```text
Normal TASK:
orchestrator → implementer → verifier → reviewer → recorder → commit → user report

EVAL TASK:
orchestrator → verifier → evaluator → recorder → commit → user validation guide → STOP
```

- implementer 완료 전 verifier를 시작하지 않는다.
- verifier 완료 전 reviewer를 시작하지 않는다.
- reviewer 완료 전 recorder를 시작하지 않는다.
- EVAL TASK에서는 verifier 완료 전 evaluator를 시작하지 않는다.
- `manage_subagents` 또는 반환 상태로 현재 역할이 완료됐는지 확인한다.
- 필요하면 `send_message`로 추가 정보만 전달한다.
- 필수 역할이 error/killed 상태가 되면 원인을 확인하고 FAIL 또는 BLOCKED로 처리한다.

### 6.6 subagent handoff 필수 정보

각 역할 Prompt에는 최소한 다음을 포함한다.

- TASK ID
- WBS ID
- Domain
- Branch
- TASK Type
- objective
- 역할별 작업 범위
- source context 중 필요한 부분
- allowed files
- forbidden files
- acceptance criteria
- verification commands 또는 선행 역할 결과 중 필요한 부분
- "자신의 역할만 수행할 것"
- "다른 필수 역할을 대행하지 않을 것"
- "직접 커밋하지 않을 것"
- "결과를 orchestrator에게 반환할 것"

## 7. 역할별 책임 경계

### orchestrator

- TASK 계약 추출
- branch/git 상태 확인
- custom agent 가용성 확인
- subagent 호출, 상태 확인, handoff
- 실패 시 이전 단계 복귀 또는 중단 판단
- 최종 diff/status 확인
- 최종 커밋과 사용자 보고

orchestrator는 구현, 독립 검증, 독립 리뷰, 평가, 실행 로그 작성을 직접 대행하지 않는다.

### implementer

- Normal TASK에서만 사용
- allowed files 안에서 최소 구현
- 필요한 테스트 추가/수정
- 커밋 금지

### verifier

- verification commands 실행
- acceptance criteria 검증
- 결과를 PASS / FAIL / BLOCKED로 반환
- 구현 파일 수정 금지
- 커밋 금지

### reviewer

- Normal TASK에서 `git diff`와 검증 결과 검토
- 범위, forbidden files, 요구사항, 보안, 성능, 아키텍처, 계약, 테스트 누락 확인
- PASS / PASS_WITH_NOTES / FAIL 반환
- 파일 수정 및 커밋 금지

### evaluator

- EVAL TASK에서만 사용
- 선행 TASK 로그와 통합 검증 근거 확인
- 평가표 기반 등급과 PASS / CONDITIONAL_PASS / FAIL / BLOCKED 산출
- 사용자 검증 시나리오 생성
- 구현/테스트 수정 및 커밋 금지

### recorder

- `ops/logs/TASK-xxx.log.md` 작성/갱신
- 실제 실행 증거만 기록
- 변경 유형(created/modified/deleted/renamed/moved) 기록
- 커밋 금지

## 8. 실행 절차

### 8.1 준비

1. `AGENTS.md`를 읽는다.
2. `.agents/rules/**`를 읽는다.
3. 지정된 TASK 파일을 읽는다.
4. TASK 계약을 추출한다.
5. 현재 branch와 TASK Branch 일치 여부를 확인한다. 불일치 시 BLOCKED.
6. `git status --short`를 확인한다.
7. 관련 없는 미커밋 변경사항이 있으면 BLOCKED.
8. TASK Type에 필요한 custom agent manifest를 확인한다.

### 8.2 Normal TASK (Mode 3A)

1. implementer를 `TypeName: implementer`, `Workspace: inherit`로 호출한다.
2. implementer 완료 결과와 변경 파일을 확인한다.
3. verifier를 `TypeName: verifier`로 호출해 verification commands와 acceptance criteria를 검증한다.
4. verifier가 FAIL이면 implementer 단계로 되돌린다. BLOCKED면 중단한다.
5. reviewer를 `TypeName: reviewer`로 호출해 diff와 검증 결과를 리뷰한다.
6. reviewer가 FAIL이면 implementer 단계로 되돌린다.
7. recorder를 `TypeName: recorder`로 호출해 실행 기록을 작성한다.
8. orchestrator가 `git status --short`, `git diff`, `git diff --check`로 최종 무결성을 확인한다.
9. 완료 조건을 만족하면 커밋한다.

### 8.3 EVAL TASK (Mode 3B)

1. Evaluation Scope와 선행 TASK 로그를 확인한다.
2. verifier를 `TypeName: verifier`로 호출해 통합 검증을 수행한다.
3. evaluator를 `TypeName: evaluator`로 호출해 평가표 기반 평가와 사용자 검증 안내를 생성한다.
4. recorder를 `TypeName: recorder`로 호출해 평가 결과와 사용자 검증 안내를 기록한다.
5. 완료 조건을 만족하면 EVAL TASK를 커밋한다.
6. TASK Status를 `DONE`, User Validation Status를 `PENDING_USER_VALIDATION`으로 기록한다.
7. 사용자 검증 안내를 출력하고 STOP한다.
8. 사용자 APPROVED 후 다음 기능 그룹으로 진행한다.

EVAL TASK에서는 implementer를 사용하지 않고 구현/리팩터링/테스트 수정을 하지 않는다. 필요하면 correction TASK를 새로 만든다.

## 9. 커밋 조건

Normal TASK:

- acceptance criteria 충족
- verifier PASS
- reviewer PASS 또는 PASS_WITH_NOTES
- 실행 로그 작성 또는 갱신
- forbidden files 수정 없음
- 관련 없는 변경 없음

EVAL TASK:

- Evaluation Scope 확인
- 선행 TASK 로그 확인
- 통합 검증 결과 확인
- evaluator verdict 기록
- 사용자 검증 안내 기록
- 관련 없는 변경 없음

기본 커밋 메시지 형식:

```text
TASK-XXX WBS-XX-XXX: short summary
```

## 10. 최종 보고 형식

```text
TASK ID:
WBS ID:
Domain:
Branch:
Status:
Changed files:
Verification:
Review verdict:
Evaluation verdict: (EVAL TASK만)
User validation status: (EVAL TASK만)
Execution log:
Commit message:
Commit hash:
Remaining risks:
Follow-up:
```

## 11. 실패 또는 중단

필수 subagent manifest 누락, TypeName 호출 실패, subagent error/killed, 검증 실패, 리뷰 실패, 범위 위반 등으로 완료할 수 없으면 다음을 보고한다.

```text
TASK ID:
Status: BLOCKED 또는 FAIL
Reason:
Completed work:
Changed files:
Failed verification:
Blocking issue:
Recommended next action:
```

필수 역할을 spawn할 수 없을 때 단일 에이전트로 대체하지 않는다.
