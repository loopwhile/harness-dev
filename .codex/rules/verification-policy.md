# Verification Policy

## 기본 원칙

검증하지 않은 작업은 완료로 판단하지 않는다.

## 검증 대상

가능한 경우 다음을 확인한다.

- unit test
- integration test
- e2e test
- lint
- type check
- build
- migration
- API contract
- UI behavior
- manual acceptance criteria

## 기록해야 할 내용

검증 결과에는 다음이 포함되어야 한다.

- 실행한 명령
- 실행 결과
- 주요 출력
- 실패 원인
- 생략한 검증과 생략 사유

## 금지 사항

- 실행하지 않은 테스트를 실행했다고 기록하지 않는다.
- 실패한 테스트를 숨기지 않는다.
- 검증 실패 상태를 PASS로 처리하지 않는다.
- 단순히 "문제없음"이라고만 기록하지 않는다.