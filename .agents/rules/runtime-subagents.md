---
trigger: always_on
---

# Runtime Subagents Rule

## 목적

이 규칙은 Antigravity CLI에서 TASK 실행 중 runtime subagent를 사용할 때의 역할, 책임, 출력 형식을 정의한다.

Antigravity 작업에서 `.agents/agents/*/agent.json` 파일은 런타임 서브에이전트의 시스템 프롬프트와 도구 권한 정의의 진실 공급원이다. (probe 제외)

메인 에이전트(orchestrator)는 `define_subagent` 호출 시 해당 agent.json의 설정을 읽어서 주입한다.

신뢰 가능한 실행 경로는 다음이다.

```text
.agents/skills/antigravity-execute-task/SKILL.md   ← 실행 절차
.agents/agents/*/agent.json                        ← 서브에이전트 정의
.agents/rules/**                                   ← 행동 규칙
runtime subagent orchestration                     ← 실행 엔진
```

## 기본 원칙

- subagent는 TASK 범위 안에서만 동작한다.
- subagent는 각자 역할을 명확히 분리한다.
- subagent 결과는 메인 agent가 최종 검토한다.
- subagent가 완료했다고 해서 TASK가 완료된 것은 아니다.
- 최종 완료 판단은 검증, 리뷰, 기록, 커밋 조건을 모두 확인한 뒤 수행한다.

## 권장 역할

TASK 실행 시 필요한 경우 다음 역할을 runtime subagent로 정의한다.

```text
orchestrator
implementer
verifier
reviewer
evaluator
recorder
```

작업 규모가 작으면 하나의 agent가 여러 역할을 수행할 수 있다.

그러나 결과 보고에서는 역할별 책임을 분리해서 기록해야 한다.

## orchestrator 출력 형식

orchestrator는 다음 형식으로 결과를 낸다.

```text
Role: orchestrator
TASK ID:
WBS ID:
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

implementer는 다음 형식으로 결과를 낸다.

```text
Role: implementer
TASK ID:
Status:
Changed files:
Implementation summary:
Notes:
Risks:
```

## verifier 출력 형식

verifier는 다음 형식으로 결과를 낸다.

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

reviewer는 다음 형식으로 결과를 낸다.

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

## recorder 출력 형식

recorder는 다음 형식으로 결과를 낸다.

```text
Role: recorder
TASK ID:
Log path:
Recorded sections:
Missing information:
Status:
```

## subagent 간 책임 제한

### implementer는 커밋하지 않는다

implementer는 구현만 수행한다.

커밋은 메인 agent가 검증, 리뷰, 기록 완료 후 수행한다.

### verifier는 구현하지 않는다

verifier는 검증 실패 원인을 설명할 수 있지만 직접 구현을 수정하지 않는다.

수정이 필요하면 implementer 단계로 되돌린다.

### reviewer는 구현하지 않는다

reviewer는 문제를 지적하고 verdict를 낸다.

직접 구현을 수정하지 않는다.

### recorder는 사실만 기록한다

recorder는 실행하지 않은 검증을 기록하지 않는다.

실패한 작업을 성공으로 기록하지 않는다.

## evaluator 출력 형식

evaluator는 다음 형식으로 결과를 낸다.

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

### evaluator는 구현하지 않는다

evaluator는 품질 평가만 수행한다.

구현 파일을 수정하지 않는다.

리팩터링을 하지 않는다.

테스트를 수정하지 않는다.

커밋하지 않는다.

FAIL 또는 BLOCKED 시 보고하고 중단한다.

자동으로 이전 TASK를 재실행하지 않는다.

## 병렬 실행 기준

다음 작업은 병렬 실행할 수 있다.

- 독립적인 파일 조사
- 독립적인 테스트 분석
- 문서 확인
- 코드 리뷰와 위험 분석

다음 작업은 순차 실행한다.

```text
일반 TASK:
TASK 분석 -> 구현 -> 검증 -> 리뷰 -> 기록 -> 커밋

EVAL TASK:
TASK 분석 -> 통합 검증 -> 평가 -> 기록 -> 커밋 -> 사용자 검증 안내 -> STOP
```

검증은 구현 이후에 수행한다.

리뷰는 구현 diff와 검증 결과가 나온 뒤 수행한다.

기록은 검증과 리뷰 결과가 나온 뒤 수행한다.

커밋은 모든 조건 충족 후 수행한다.

## 최종 완료 판단

runtime subagent 결과가 모두 나와도 다음 조건을 만족하지 않으면 완료가 아니다.

- implementation 완료
- verification PASS
- review verdict PASS 또는 PASS_WITH_NOTES
- execution log 작성 또는 갱신
- forbidden files 수정 없음
- 관련 없는 변경 없음
- 커밋 조건 충족

## 실패 시 처리

subagent 중 하나가 FAIL 또는 BLOCKED를 반환하면 다음을 수행한다.

1. 실패 역할을 식별한다.
2. 실패 이유를 요약한다.
3. 수정 가능한 경우 해당 단계로 되돌아간다.
4. 수정 불가능한 경우 TASK를 FAIL 또는 BLOCKED로 보고한다.
5. 실패 내용을 `ops/logs/TASK-xxx.log.md`에 기록한다.