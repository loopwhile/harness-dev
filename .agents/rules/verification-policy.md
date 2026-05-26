---
trigger: always_on
---

# Verification Policy

## 목적

이 규칙은 Antigravity CLI가 검증 없이 작업을 완료 처리하지 않도록 강제한다.

TASK 완료는 구현이 아니라 검증 통과를 기준으로 판단한다.

## 기본 원칙

- 검증 없이 완료 처리하지 않는다.
- 실행하지 않은 검증을 성공으로 기록하지 않는다.
- 실패한 검증을 성공으로 기록하지 않는다.
- acceptance criteria를 확인하지 않고 완료 처리하지 않는다.
- 환경 문제로 검증하지 못한 경우 BLOCKED로 기록한다.

## 검증 기준

검증 기준은 TASK 파일의 다음 항목을 따른다.

```text
acceptance criteria
verification commands
```

verification commands가 명시되어 있으면 반드시 실행한다.

verification commands가 없으면 다음 순서로 적절한 검증을 찾는다.

1. README 또는 AGENTS.md의 검증 명령
2. package.json, pyproject.toml, build.gradle, pom.xml 등 프로젝트 설정의 테스트 명령
3. docs/07_test_qa/** 문서
4. 코드 변경 범위에 맞는 최소 검증 명령

그래도 검증 명령을 찾을 수 없으면 임의로 PASS 처리하지 않고 `BLOCKED`로 기록한다.

## 검증 명령 기록

검증 결과에는 반드시 다음을 포함한다.

- 실행 명령
- 실행 위치
- 실행 결과
- 성공 여부
- 실패한 경우 오류 요약
- 실행하지 못한 경우 사유

예시:

```text
Command: npm test
Result: PASS
Notes: All tests passed.
```

예시:

```text
Command: npm run build
Result: FAIL
Reason: Type error in src/app.ts
```

예시:

```text
Command: pytest
Result: BLOCKED
Reason: pytest is not installed in the current environment.
```

## 검증 결과 상태

검증 결과는 다음 중 하나로 표기한다.

```text
PASS
FAIL
BLOCKED
```

### PASS

다음 조건을 모두 만족할 때만 PASS다.

- verification commands를 실행했다.
- 모든 필수 검증 명령이 성공했다.
- acceptance criteria를 충족했다.
- 확인하지 못한 필수 항목이 없다.

### FAIL

다음 중 하나라도 해당하면 FAIL이다.

- 테스트 실패
- 빌드 실패
- 타입 체크 실패
- 린트 실패
- acceptance criteria 미충족
- 필수 검증 명령 실패

### BLOCKED

다음 중 하나라도 해당하면 BLOCKED다.

- 의존성 미설치
- 로컬 환경 미구성
- 인증 정보 없음
- 외부 서비스 접근 불가
- 네트워크 문제
- TASK에 검증 명령 없음
- 검증 방법을 결정할 수 없음

BLOCKED는 PASS가 아니다.

BLOCKED 상태에서는 커밋하지 않는다.

## acceptance criteria 확인

acceptance criteria는 항목별로 확인한다.

각 항목은 다음 중 하나로 표시한다.

```text
PASS
FAIL
NOT_CHECKED
```

NOT_CHECKED가 하나라도 있으면 TASK는 완료할 수 없다.

## 검증 실패 시 처리

검증이 실패하면 다음 순서로 처리한다.

1. 실패 명령을 기록한다.
2. 실패 원인을 요약한다.
3. 재현 방법을 기록한다.
4. 수정 가능한 경우 구현 단계로 돌아간다.
5. 수정 불가능한 경우 FAIL 또는 BLOCKED로 보고한다.

## 검증과 리뷰의 관계

reviewer는 verifier의 결과를 확인해야 한다.

검증 결과가 FAIL 또는 BLOCKED이면 review verdict는 PASS가 될 수 없다.

## 완료 조건

TASK 완료를 위해 검증 측면에서 필요한 조건은 다음과 같다.

- 모든 verification commands 실행
- 모든 필수 검증 PASS
- 모든 acceptance criteria PASS
- 검증 결과가 `ops/logs/TASK-xxx.log.md`에 기록됨