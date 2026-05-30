# Evaluation Policy

## 목적

이 규칙은 Codex CLI에서 EVAL TASK 실행 시 평가와 사용자 검증 게이트를 정의한다.

## 일반 TASK

일반 TASK에는 full evaluation을 실행하지 않는다.

일반 TASK는 기존 흐름을 따른다.

```text
orchestrator → implementer → verifier → reviewer → recorder → commit
```

## EVAL TASK

EVAL TASK는 다음 순서로 실행한다.

```text
1. orchestrator가 EVAL TASK를 읽는다.
2. 통합 검증을 수행한다.
3. evaluator가 평가표 기반 평가를 수행한다.
4. evaluator가 사용자 검증 안내를 생성한다.
5. recorder가 평가 결과와 사용자 검증 안내를 기록한다.
6. EVAL TASK를 커밋한다.
7. 사용자 검증 안내를 출력한다.
8. STOP한다.
9. 사용자 APPROVED 후 다음 기능 그룹으로 진행한다.
```

## evaluator 역할 제한

evaluator는 품질 평가자다.

금지:

- 구현 파일 수정
- 리팩터링
- 테스트 수정
- 커밋
- 삭제/파괴성 작업
- TASK 범위 확장

## EVAL 실패 시

보고하고 중단한다.

자동으로 이전 TASK를 재실행하지 않는다.

## 사용자 검증 상태

```text
PENDING_USER_VALIDATION: 사용자 검증 대기 중
APPROVED: 검증 통과. 다음 기능 그룹 진행 가능.
REJECTED: 검증 실패. 수정 후 재평가 필요.
REQUEST_CHANGES: 부분 수정 필요. 지적된 항목만 수정 후 재검증.
DEFERRED: 보류. 후속 조치 결정 후 진행.
```

사용자 APPROVED 전까지 다음 기능 그룹으로 진행하지 않는다.
