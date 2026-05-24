---
name: verify-task
description: 구현 이후 테스트, 린트, 빌드, acceptance criteria를 검증할 때 사용한다.
---

# Verify Task Skill

## 1. 목적

이 스킬은 TASK 구현 결과가 실제로 완료 기준을 만족하는지 검증한다.

## 2. 입력

필수 입력:

- TASK 파일
- verification commands
- acceptance criteria
- 변경 파일 목록
- 구현 요약

## 3. 절차

1. TASK의 verification commands를 확인한다.
2. 명시된 검증 명령을 실행한다.
3. 검증 명령이 없으면 프로젝트 구조에 맞는 최소 검증을 추론한다.
4. acceptance criteria를 하나씩 확인한다.
5. 실패한 검증이 있으면 원인과 재현 방법을 기록한다.
6. 검증 결과를 요약한다.

## 4. 검증 종류

가능한 경우 다음을 확인한다.

- unit test
- integration test
- e2e test
- lint
- type check
- build
- migration check
- API contract check
- manual acceptance check

## 5. 출력 형식

검증 결과는 다음 형식으로 보고한다.

| 항목 | 내용 |
|---|---|
| 실행 명령 |  |
| 결과 | PASS / FAIL / SKIPPED |
| 주요 출력 |  |
| 실패 원인 |  |
| 후속 조치 |  |

## 6. 하드 룰

- 검증을 실행하지 않고 PASS 처리하지 않는다.
- 실패한 명령을 숨기지 않는다.
- 검증이 실패하면 완료로 판단하지 않는다.
- 구현 코드를 임의로 수정하지 않는다.
- 커밋하지 않는다.