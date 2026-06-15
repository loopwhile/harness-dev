---
name: execute-task
description: ops/tasks/TASK-xxx.md 하나를 자율적으로 실행할 때 사용한다. TASK 분석, 구현, 검증, 리뷰, 기록, 커밋까지 진행한다.
---

# Execute Task Skill

## 1. 목적

이 스킬은 `ops/tasks/TASK-xxx.md` 파일 하나를 기준으로 전체 작업을 자율 실행한다.

이 스킬이 호출되면 **TASK Execution Mode**가 활성화된다.

실행 흐름은 다음과 같다.

1. TASK 분석
2. 브랜치 확인
3. 오케스트레이션
4. 구현 (Normal TASK) 또는 통합 검증 (EVAL TASK)
5. 검증
6. 리뷰 (Normal TASK)
7. 평가 (EVAL TASK)
8. 기록
9. 최종 커밋

## 2. 기본 원칙

- 단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.
- TASK 파일 없이 작업하지 않는다.
- TASK의 allowed files 밖은 수정하지 않는다.
- TASK의 forbidden files는 수정하지 않는다.
- TASK가 명시적으로 허용하지 않으면 `docs/01_overview`부터 `docs/09_pm`까지 수정하지 않는다.
- 요구사항을 임의로 만들지 않는다.
- 관련 없는 리팩터링을 하지 않는다.
- 검증 없이 완료 처리하지 않는다.
- 리뷰 없이 커밋하지 않는다. (Normal TASK)
- 검증과 리뷰가 통과한 경우에만 커밋한다.

## 3. TASK 실행 중 사용자 승인 없이 허용하는 작업

다음 작업은 TASK 범위 안이라면 사용자에게 묻지 않고 진행한다.

- TASK allowed files 내부 파일 생성
- TASK allowed files 내부 파일 수정
- TASK allowed files 내부 파일 삭제
- TASK allowed files 내부 파일 이동/이름 변경
- TASK allowed files 내부 디렉터리 생성
- TASK allowed files 내부 디렉터리 정리
- 테스트 파일 추가/수정/삭제
- 검증 명령 실행
- 빌드 명령 실행
- 린트 명령 실행
- 타입 체크 실행
- git status
- git diff
- git add
- git commit
- git restore --staged
- TASK 로그 작성/수정

## 4. 절대 금지 또는 사용자 승인 필요

- 프로젝트 루트 밖 파일 생성/수정/삭제
- 프로젝트 루트 전체 삭제
- .git 디렉터리 삭제
- `rm -rf /`, `rm -rf .`, `rm -rf ..`, `rm -rf ./*`
- `git clean -fdx`
- `git reset --hard`
- `git push --force`
- 원격 브랜치 삭제
- DB drop, 테이블 drop
- TASK allowed files 밖의 파일 변경

## 5. TASK 실행 절차

1. `AGENTS.md`를 읽는다.
2. 지정된 TASK 파일을 읽는다.
3. TASK에서 다음 정보를 추출한다.
   - TASK ID
   - WBS ID
   - Domain
   - Branch
   - Type
   - objective
   - source context
   - allowed files
   - forbidden files
   - implementation requirements
   - acceptance criteria
   - verification commands
   - commit rule
4. 현재 git branch를 확인한다.
   ```bash
   git branch --show-current
   ```
5. 현재 branch가 TASK의 Branch와 일치하는지 확인한다. 불일치 시 BLOCKED.
6. `git status --short`로 현재 작업 상태를 확인한다.
7. 관련 없는 미커밋 변경사항이 있으면 작업을 중단하고 보고한다.
8. TASK Type에 따라 분기한다.
   - Type != eval → Normal TASK Flow (Mode 3A)
   - Type == eval → EVAL TASK Flow (Mode 3B)

### Normal TASK Flow (Mode 3A)

1. 필요한 문서와 소스 파일만 읽는다.
2. 구현 계획을 짧게 정리한다.
3. TASK 범위 안에서 구현한다.
4. verification commands를 실행한다.
5. acceptance criteria를 하나씩 확인한다.
6. git diff를 리뷰한다.
7. `ops/logs/TASK-xxx.log.md`를 작성 또는 갱신한다.
8. 검증과 리뷰가 통과하면 커밋한다.
9. 최종 결과를 보고한다.

### EVAL TASK Flow (Mode 3B)

1. EVAL TASK의 Evaluation Scope를 확인한다.
2. 선행 TASK 로그(`ops/logs/TASK-xxx.log.md`)를 읽는다.
3. 통합 검증이 필요하면 verification commands를 실행한다.
4. 평가표 기반 평가를 수행한다.
5. 사용자 검증 안내를 생성한다.
6. `ops/logs/TASK-xxx.log.md`에 평가 결과와 사용자 검증 안내를 기록한다.
7. EVAL TASK를 커밋한다. (TASK Status: DONE, User Validation Status: PENDING_USER_VALIDATION)
8. 사용자 검증 안내를 출력하고 STOP한다.
9. 사용자 APPROVED 후 다음 기능 그룹으로 진행한다.

EVAL TASK에서 평가가 FAIL 또는 BLOCKED이면:

- 사용자에게 보고하고 중단한다.
- 자동으로 이전 TASK를 재실행하지 않는다.
- 필요하면 correction TASK를 새로 만들거나 사용자 승인 후 진행한다.

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
- Domain
- Branch
- 완료 여부
- 수정 파일 목록
- 검증 명령과 결과
- 리뷰 결과
- 커밋 메시지
- 커밋 해시
- 남은 위험 또는 후속 작업
- Evaluation verdict (EVAL TASK만)
- User validation status (EVAL TASK만)