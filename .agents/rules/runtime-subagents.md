---
trigger: always_on
---

# Runtime Subagents Rule

## 적용 범위

이 규칙은 Antigravity의 **TASK Execution Mode**에서 runtime subagent를 사용할 때 적용한다.

## 진실 공급원

Antigravity custom agent의 시스템 프롬프트, 도구 권한, 실행 정책의 진실 공급원은 다음 파일이다.

```text
.agents/agents/<role>/agent.md
```

Antigravity는 workspace의 `.agents/agents/<name>.md` 또는 `.agents/agents/<name>/agent.md`를 자동 탐색한다.

이 저장소는 다음 실행 경로를 표준으로 사용한다.

```text
.agents/skills/antigravity-execute-task/SKILL.md   ← 실행 절차
.agents/agents/*/agent.md                          ← 네이티브 custom agent 정의
.agents/rules/**                                   ← 행동 규칙
invoke_subagent                                    ← 고정 역할 실행
```

고정 역할에 대해 별도의 JSON manifest를 사용하지 않는다.

## 기본 원칙

- subagent는 TASK 범위 안에서만 동작한다.
- 역할별 책임을 분리한다.
- 고정 역할의 시스템 프롬프트와 도구 권한을 handoff Prompt에서 재정의하지 않는다.
- subagent 결과는 orchestrator가 최종 검토한다.
- subagent 완료만으로 TASK 완료로 판단하지 않는다.
- 검증, 리뷰, 기록, 커밋 조건을 모두 확인한 뒤 완료 판단한다.
- 필수 역할 호출 실패 시 단일 에이전트 실행으로 우회하지 않는다.

## 고정 역할

| 역할 | mainAgent | subagent | 목적 |
|---|---:|---:|---|
| orchestrator | true | false | TASK 전체 조율과 최종 완료 판단 |
| implementer | false | true | Normal TASK 구현 |
| verifier | false | true | 검증 및 acceptance criteria 확인 |
| reviewer | false | true | Normal TASK diff 리뷰 |
| evaluator | false | true | EVAL TASK 품질 평가 |
| recorder | false | true | 실행 증거와 로그 기록 |

메인/root thread가 orchestrator 책임을 수행하며 `orchestrator` custom agent를 subagent로 호출하지 않는다.

## native invocation 계약

필수 역할은 `invoke_subagent`로 호출한다.

각 호출은 다음을 만족해야 한다.

```text
Role: 역할명
TypeName: 역할의 agent.md name 값
Workspace: inherit
Prompt: TASK별 역할 컨텍스트
```

예:

```text
Role: verifier
TypeName: verifier
Workspace: inherit
```

`TypeName`은 `.agents/agents/<role>/agent.md`의 `name`과 정확히 일치해야 한다.

필수 manifest가 없거나 `subagent: true`가 아니거나 TypeName 호출에 실패하면 `BLOCKED`로 처리한다.

## define_subagent 제한

다음 고정 역할은 `define_subagent`로 재정의하지 않는다.

```text
implementer
verifier
reviewer
evaluator
recorder
```

`define_subagent`는 영구 manifest가 없는 일회성 보조 역할에만 허용한다.

일회성 역할은 다음을 만족해야 한다.

- 필수 역할을 대체하지 않는다.
- 여러 필수 역할을 하나로 병합하지 않는다.
- TASK allowed files와 forbidden files를 그대로 따른다.
- 필수 단계의 완료 판정을 대신하지 않는다.

## subagent 재귀 제한

implementer, verifier, reviewer, evaluator, recorder는 다른 필수 subagent를 호출하지 않는다.

각 역할의 `agent.md`에는 `invoke_subagent` 권한을 부여하지 않는 것을 기본으로 한다.

모든 필수 handoff는 orchestrator가 직접 수행한다.

## 실행 흐름

### Normal TASK Flow (Mode 3A)

```text
orchestrator → implementer → verifier → reviewer → recorder → commit → user report
```

### EVAL TASK Flow (Mode 3B)

```text
orchestrator → verifier → evaluator → recorder → commit → user validation guide → STOP
```

EVAL TASK에서는 implementer를 사용하지 않는다.

EVAL TASK에서는 구현/리팩터링/테스트 수정 금지. 필요하면 correction TASK를 새로 만든다.

## 비동기 실행 제어

Antigravity의 subagent는 비동기로 시작될 수 있으나 이 하네스의 필수 역할은 순차 완료한다.

- implementer 완료 후 verifier
- verifier 완료 후 reviewer
- reviewer 완료 후 recorder
- EVAL TASK에서는 verifier 완료 후 evaluator, evaluator 완료 후 recorder

`manage_subagents` 또는 실행 반환 상태로 완료 여부를 확인한다.

필수 역할이 `error` 또는 `killed`가 되면 원인을 확인해 FAIL 또는 BLOCKED로 처리하고 다음 단계로 진행하지 않는다.

## handoff 필수 정보

orchestrator가 subagent에 전달하는 Prompt에는 최소한 다음을 포함한다.

- TASK ID
- WBS ID
- Domain
- Branch
- TASK Type
- objective
- 역할별 작업 범위
- 필요한 source context
- allowed files
- forbidden files
- acceptance criteria
- verification commands 또는 선행 역할 결과 중 필요한 부분
- 자신에게 지정된 역할만 수행한다는 제한
- 다른 필수 역할을 대행하거나 spawn하지 않는다는 제한
- 직접 커밋하지 않는다는 제한
- 결과를 orchestrator에게 반환한다는 요구

## orchestrator 출력 형식

```text
Role: orchestrator
TASK ID:
WBS ID:
Domain:
Branch:
Objective:
Allowed files:
Forbidden files:
Acceptance criteria:
Verification commands:
Execution plan:
Risks:
Next role:
```

## implementer 출력 형식

```text
Role: implementer
TASK ID:
Status:
Changed files:
  - path/to/file (created / modified / deleted / renamed / moved)
Implementation summary:
Notes:
Risks:
```

## verifier 출력 형식

```text
Role: verifier
TASK ID:
Verification result: PASS | FAIL | BLOCKED
Commands:
- command:
  result:
  notes:
Acceptance criteria:
- criterion:
  result:
  notes:
Failure summary:
```

## reviewer 출력 형식

```text
Role: reviewer
TASK ID:
Review verdict: PASS | PASS_WITH_NOTES | FAIL
Scope check:
Forbidden files check:
Verification check:
Architecture check:
Security check:
Performance check:
Maintainability check:
Notes:
Required fixes:
```

## evaluator 출력 형식

```text
Role: evaluator
TASK ID:
Evaluation Type: feature_eval / domain_eval / epic_eval
Verdict: PASS / CONDITIONAL_PASS / FAIL / BLOCKED
Criteria Results:
  1. 기능 목표 정합성: [등급] - [근거]
  2. Acceptance Criteria 충족도: [등급] - [근거]
  3. 구현 완성도: [등급] - [근거]
  4. 통합 안정성: [등급] - [근거]
  5. 테스트/검증 충분성: [등급] - [근거]
  6. 범위 통제 여부: [등급] - [근거]
  7. 유지보수성: [등급] - [근거]
  8. 사용자 검증 가능성: [등급] - [근거]
Integration Checks: (domain_eval/epic_eval만)
Critical Issues:
Improvement Suggestions:
User Validation Scenarios:
```

## recorder 출력 형식

```text
Role: recorder
TASK ID:
Log path:
Recorded sections:
Missing information:
Status:
```

## 책임 제한

### implementer

- 구현만 수행한다.
- TASK allowed files 내부 변경만 수행한다.
- 커밋하지 않는다.
- EVAL TASK에서는 사용하지 않는다.

### verifier

- 검증 실패 원인을 설명할 수 있지만 구현 파일을 수정하지 않는다.
- Normal TASK에서는 verification commands와 acceptance criteria를 검증한다.
- EVAL TASK에서는 통합 검증과 선행 TASK 증거를 확인한다.
- 커밋하지 않는다.

### reviewer

- 문제를 지적하고 verdict를 낸다.
- 직접 구현을 수정하지 않는다.
- Normal TASK에서는 필수다.
- EVAL TASK에서는 선택 사항이다.
- 커밋하지 않는다.

### evaluator

- Type: eval TASK에서만 품질 평가를 수행한다.
- 구현/리팩터링/테스트 수정 금지.
- 평가 증거를 조작하지 않는다.
- 커밋하지 않는다.

### recorder

- 실제 실행된 사실만 기록한다.
- 실패한 작업을 성공으로 기록하지 않는다.
- 파일 변경 유형을 명확히 기록한다.
- 커밋하지 않는다.

## 최종 완료 판단

### 일반 TASK 완료 조건

- implementation 완료
- verification PASS
- review verdict PASS 또는 PASS_WITH_NOTES
- execution log 작성 또는 갱신
- forbidden files 수정 없음
- 관련 없는 변경 없음
- 커밋 조건 충족

### EVAL TASK 완료 조건

- Evaluation Scope 확인 완료
- 선행 TASK 로그 확인 완료
- 통합 검증 결과 확인 완료
- evaluator verdict 산출 완료
- 평가 결과와 사용자 검증 안내 기록 완료
- EVAL TASK 커밋 완료
- TASK Status `DONE`
- User Validation Status `PENDING_USER_VALIDATION`
- 사용자 검증 안내 출력 완료
- 다음 기능 그룹 진행 중단(STOP)

EVAL TASK는 사용자가 APPROVED를 명시하기 전까지 다음 feature group 또는 WBS group으로 진행하지 않는다.

## 실패 시 처리

subagent 중 하나가 FAIL 또는 BLOCKED를 반환하거나 호출 자체가 실패하면:

1. 실패 역할을 식별한다.
2. 실패 이유를 요약한다.
3. 수정 가능한 Normal TASK 실패는 implementer 단계로 되돌아갈 수 있다.
4. 수정 불가능하거나 manifest/호출 문제면 BLOCKED로 중단한다.
5. 실패 내용을 `ops/logs/TASK-xxx.log.md`에 기록한다.
