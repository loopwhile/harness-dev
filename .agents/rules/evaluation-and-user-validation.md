# Evaluation and User Validation Rule

## 적용 범위

이 규칙은 **TASK Execution Mode** 내부에서 Type: eval일 때 활성화되는 특수 Flow(Mode 3B)에서 적용한다.

EVAL TASK는 별도 Mode 4가 아니라 TASK Execution Mode 내부의 분기다.

## 목적

이 규칙은 EVAL TASK의 실행 흐름, evaluator의 역할, 사용자 검증 게이트를 정의한다.

## 기본 원칙

- 일반 TASK에는 full evaluation을 실행하지 않는다.
- EVAL TASK에서만 evaluator와 사용자 검증 안내를 실행한다.
- 사용자 APPROVED 전까지 다음 기능 그룹으로 진행하지 않는다.

## 일반 TASK 흐름 (Mode 3A)

일반 TASK는 기존 방식 그대로 유지한다.

```text
orchestrator → implementer → verifier → reviewer → recorder → commit → user report
```

일반 TASK도 다음은 반드시 통과해야 한다.

- implementation boundary check
- verification
- review
- execution logging
- commit rule

## EVAL TASK 흐름 (Mode 3B)

EVAL TASK는 다음 순서로 실행한다.

```text
1. orchestrator가 EVAL TASK를 읽는다.
2. 현재 git branch가 TASK의 Branch와 일치하는지 확인한다.
3. 통합 검증을 수행한다.
4. evaluator가 평가표 기반 평가를 수행한다.
5. evaluator가 사용자 검증 안내를 생성한다.
6. recorder가 평가 결과와 사용자 검증 안내를 ops/logs/TASK-xxx.log.md에 기록한다.
7. EVAL TASK를 커밋한다. (평가 로그 + 사용자 검증 안내)
8. 사용자 검증 안내를 출력한다.
9. STOP한다. (상태: PENDING_USER_VALIDATION)
10. 사용자 APPROVED 후 다음 기능 그룹으로 진행한다.
```

EVAL TASK에서는 implementer를 사용하지 않는다.

EVAL TASK에서는 구현/리팩터링/테스트 수정 금지. 필요하면 correction TASK를 새로 만든다.

reviewer는 EVAL TASK에서 선택 사항이다.

## EVAL TASK 커밋 정책

EVAL TASK는 평가 완료 시점에 평가 로그와 사용자 검증 안내를 커밋한다.

사용자 승인 전까지 커밋을 보류하지 않는다.

커밋하되 TASK 상태를 `PENDING_USER_VALIDATION`으로 남긴다.

사용자가 APPROVED를 명시하기 전까지 다음 feature group 또는 WBS group으로 진행하지 않는다.

## EVAL TASK 대상 시점

기능 완료 체크포인트에서 EVAL TASK를 실행한다.

예시:

```text
TASK-026 EVAL: 회원가입 기능 평가 및 사용자 검증 안내
TASK-032 EVAL: 로그인 기능 평가 및 사용자 검증 안내
TASK-099 EVAL: 회원 도메인 전체 통합 평가 및 사용자 검증 안내
```

## evaluator 역할

evaluator는 품질 평가자다. 구현자가 아니다.

evaluator의 책임:

- 기능 목표 정합성 평가
- acceptance criteria 충족도 평가
- 구현 완성도 평가
- 통합 안정성 평가
- 테스트/검증 충분성 평가
- 범위 통제 여부 평가
- 유지보수성 평가
- 사용자 검증 가능성 평가

evaluator가 해서는 안 되는 일:

- 구현 파일 수정
- 리팩터링
- 테스트 수정
- 커밋
- 삭제/파괴성 작업
- TASK 범위 확장

## 등급 체계

각 평가 영역의 등급:

```text
EXCELLENT
GOOD
ACCEPTABLE
NEEDS_IMPROVEMENT
FAIL
```

## Verdict 체계

최종 verdict:

```text
PASS: 모든 영역이 ACCEPTABLE 이상이고 FAIL 없음
CONDITIONAL_PASS: 일부 NEEDS_IMPROVEMENT가 있으나 FAIL 없음
FAIL: 하나 이상 FAIL이 있거나 핵심 영역이 NEEDS_IMPROVEMENT 이하
BLOCKED: 평가에 필요한 정보 부족
```

## EVAL 실패 시 처리

evaluator가 FAIL 또는 BLOCKED를 반환하면 다음을 수행한다.

1. 평가 결과를 기록한다.
2. 실패 이유를 보고한다.
3. 사용자에게 보고하고 중단한다.
4. 자동으로 이전 TASK를 재실행하지 않는다.
5. 필요하면 correction TASK를 새로 만들거나 사용자가 재작업 방향을 승인한 뒤 진행한다.

## 사용자 검증 상태

사용자 검증 상태는 다음 중 하나다.

```text
PENDING_USER_VALIDATION: 사용자 검증 대기 중
APPROVED: 검증 통과. 다음 기능 그룹 진행 가능.
REJECTED: 검증 실패. 수정 후 재평가 필요.
REQUEST_CHANGES: 부분 수정 필요. 지적된 항목만 수정 후 재검증.
DEFERRED: 보류. 후속 조치 결정 후 진행.
```

TASK 상태와 사용자 검증 상태는 별도 필드다.

## Evaluation Type

평가 유형은 다음 중 하나다.

```text
feature_eval: 단일 기능 내 TASK들만 평가
domain_eval: 도메인 내 모든 기능과 기능 간 통합 평가
epic_eval: 여러 도메인에 걸친 대규모 통합 평가
```

모든 유형에 동일한 평가표 템플릿(ops/templates/feature-evaluation.template.md)을 사용한다.

domain_eval 또는 epic_eval에서는 통합 관점 항목을 추가로 확인한다.

## 평가표 위치

평가표 원본:

```text
ops/templates/feature-evaluation.template.md
```

실제 평가 결과:

```text
ops/logs/TASK-xxx.log.md
```

## 사용자 검증 안내 위치

사용자 검증 안내 원본:

```text
ops/templates/user-validation.template.md
```

실제 사용자 검증 안내:

```text
ops/logs/TASK-xxx.log.md
```
