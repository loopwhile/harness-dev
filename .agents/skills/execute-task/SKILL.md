---
name: execute-task
description: ops/tasks/TASK-xxx.md 하나를 자율적으로 실행할 때 사용한다. TASK 분석, 구현, 검증, 리뷰, 기록, 커밋까지 진행하되 삭제/파괴성 작업은 사용자 승인을 요구한다.
---

# Execute Task Skill

## 1. 목적

이 스킬은 `ops/tasks/TASK-xxx.md` 파일 하나를 기준으로 전체 작업을 자율 실행한다.

실행 흐름은 다음과 같다.

1. TASK 분석
2. 오케스트레이션
3. 구현
4. 검증
5. 리뷰
6. 기록
7. 최종 커밋

## 2. 기본 원칙

- 한 번에 하나의 TASK만 실행한다.
- TASK 파일 없이 작업하지 않는다.
- TASK의 allowed files 밖은 수정하지 않는다.
- TASK의 forbidden files는 수정하지 않는다.
- TASK가 명시적으로 허용하지 않으면 `docs/01_overview`부터 `docs/09_pm`까지 수정하지 않는다.
- 요구사항을 임의로 만들지 않는다.
- 관련 없는 리팩터링을 하지 않는다.
- 검증 없이 완료 처리하지 않는다.
- 리뷰 없이 커밋하지 않는다.
- 검증과 리뷰가 통과한 경우에만 커밋한다.

## 3. 사용자에게 물어보지 않고 진행해도 되는 작업

다음 작업은 TASK 범위 안이라면 사용자에게 묻지 않고 진행한다.

- 파일 읽기
- 코드 수정
- 문서 수정
- 테스트 파일 추가 또는 수정
- 설정 파일 수정
- 디렉터리 생성
- 새 파일 생성
- formatting
- lint
- type check
- unit test
- integration test
- build
- git status 확인
- git diff 확인
- git add
- TASK 완료 커밋

## 4. 사용자 승인이 필요한 작업

다음 작업은 반드시 사용자에게 먼저 확인한다.

- 파일 삭제
- 디렉터리 삭제
- `rm`
- `rm -r`
- `rm -rf`
- `rmdir`
- `unlink`
- `git rm`
- `git clean`
- `git reset --hard`
- 데이터베이스 삭제
- migration rollback
- force push
- 원격 브랜치 삭제
- 대량 파일 이동 또는 대량 파일명 변경
- TASK allowed files 밖의 파일 변경
- TASK 범위를 넘어서는 구조 변경

## 5. TASK 실행 절차

1. `AGENTS.md`를 읽는다.
2. 지정된 TASK 파일을 읽는다.
3. TASK에서 다음 정보를 추출한다.
   - TASK ID
   - WBS ID
   - objective
   - source context
   - allowed files
   - forbidden files
   - implementation requirements
   - acceptance criteria
   - verification commands
   - commit rule
4. `git status --short`로 현재 작업 상태를 확인한다.
5. 관련 없는 미커밋 변경사항이 있으면 작업을 중단하고 보고한다.
6. 필요한 문서와 소스 파일만 읽는다.
7. 구현 계획을 짧게 정리한다.
8. TASK 범위 안에서 구현한다.
9. verification commands를 실행한다.
10. acceptance criteria를 하나씩 확인한다.
11. git diff를 리뷰한다.
12. `ops/logs/TASK-xxx.log.md`를 작성 또는 갱신한다.
13. 검증과 리뷰가 통과하면 커밋한다.
14. 최종 결과를 보고한다.

## 6. 커밋 규칙

커밋 메시지는 TASK 파일의 commit rule을 따른다.

기본 형식:

```text
TASK-XXX WBS-XX-XXX: short summary
```

예시:

```text
TASK-001 WBS-01-001: implement reservation creation API
```

## 7. 완료 보고 형식

최종 보고에는 다음을 포함한다.

- TASK ID
- WBS ID
- 완료 여부
- 수정 파일 목록
- 검증 명령과 결과
- 리뷰 결과
- 커밋 메시지
- 커밋 해시
- 남은 위험 또는 후속 작업