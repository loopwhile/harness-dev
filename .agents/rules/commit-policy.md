---
trigger: always_on
---

# Commit Policy

## 목적

이 규칙은 Antigravity CLI가 검증과 리뷰 없이 커밋하지 않도록 제한한다.

커밋은 TASK 완료의 마지막 단계다.

## 기본 원칙

- 구현 직후 바로 커밋하지 않는다.
- 검증 실패 상태에서 커밋하지 않는다.
- 리뷰 실패 상태에서 커밋하지 않는다.
- 실행 로그 없이 커밋하지 않는다.
- 관련 없는 변경사항을 함께 커밋하지 않는다.
- 사용자 기존 변경사항을 커밋하지 않는다.

## 커밋 가능 조건

다음 조건을 모두 만족할 때만 커밋할 수 있다.

- TASK 요구사항 충족
- acceptance criteria 충족
- verification result가 PASS
- review verdict가 PASS 또는 PASS_WITH_NOTES
- `ops/logs/TASK-xxx.log.md` 작성 또는 갱신
- forbidden files 수정 없음
- allowed files 밖 수정 없음
- 관련 없는 변경사항 없음

## 커밋 금지 조건

다음 중 하나라도 해당하면 커밋하지 않는다.

- verification result가 FAIL
- verification result가 BLOCKED
- review verdict가 FAIL
- acceptance criteria 미충족
- forbidden files 수정
- allowed files 밖 수정
- 관련 없는 변경 포함
- 실행 로그 없음
- 커밋 메시지에 TASK ID 없음
- 사용자 기존 변경사항과 섞임

## 커밋 메시지 형식

커밋 메시지는 TASK 파일의 commit rule을 따른다.

TASK에 별도 commit rule이 없으면 다음 형식을 사용한다.

```text
TASK-XXX WBS-XX-XXX: short summary
```

WBS ID가 없는 경우 다음 형식을 사용한다.

```text
TASK-XXX: short summary
```

예시:

```text
TASK-001 WBS-01-003: add task execution guard rules
```

예시:

```text
TASK-002: update Antigravity execute task skill
```

## 커밋 전 확인 명령

커밋 전 다음을 확인한다.

```bash
git status --short
git diff --stat
git diff
```

필요하면 staged diff도 확인한다.

```bash
git diff --cached --stat
git diff --cached
```

## 커밋 대상 제한

커밋에는 다음만 포함한다.

- TASK allowed files 안의 변경
- TASK 실행 로그
- TASK가 허용한 테스트 변경
- TASK가 허용한 문서 변경

커밋에 포함하면 안 되는 것:

- 사용자 기존 변경사항
- unrelated formatting
- unrelated refactoring
- forbidden files
- allowed files 밖 변경
- 로컬 환경 파일
- 임시 파일
- 캐시 파일
- 빌드 산출물

## 커밋 후 확인

커밋 후 다음을 확인한다.

```bash
git status --short
git log -1 --oneline
```

최종 보고에는 다음을 포함한다.

- 커밋 메시지
- 커밋 해시
- 커밋에 포함된 주요 파일
- 검증 결과
- 리뷰 verdict

## 커밋하지 않는 경우

다음 상황에서는 커밋하지 않고 보고한다.

- 사용자가 커밋하지 말라고 지시한 경우
- 검증을 실행할 수 없는 경우
- 검증이 실패한 경우
- 리뷰가 실패한 경우
- TASK 범위가 불명확한 경우
- 관련 없는 미커밋 변경사항이 있는 경우
- destructive action 승인이 필요한데 승인받지 못한 경우

보고 형식:

```text
Commit: SKIPPED
Reason:
Required next action:
```