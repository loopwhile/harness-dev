---
name: orchestrate-task
description: 하나의 ops/tasks/TASK-xxx.md 파일을 기준으로 오케스트레이션, 구현, 검증, 리뷰, 기록, 최종 커밋까지 진행할 때 사용한다.
---

# Orchestrate Task Skill

## 1. 목적

이 스킬은 TASK Execution Mode에서 `ops/tasks/TASK-xxx.md` 하나를 기준으로 전체 작업 흐름을 통제한다.

이 스킬이 호출되면 TASK Execution Mode가 활성화된다.

작업 순서는 TASK Type에 따라 분기한다.

### Normal TASK (Mode 3A)

1. 오케스트레이션 (브랜치 확인 포함)
2. 구현
3. 검증
4. 리뷰
5. 기록
6. 최종 커밋

### EVAL TASK (Mode 3B)

1. 오케스트레이션 (브랜치 확인 포함)
2. 통합 검증
3. 평가
4. 기록
5. 최종 커밋
6. 사용자 검증 안내 → STOP

## 2. 입력

필수 입력:

- 실행할 TASK 파일 경로
- 현재 git 상태
- TASK와 연결된 WBS ID
- TASK에서 참조하는 문서
- TASK에서 허용한 파일 목록
- TASK에서 금지한 파일 목록
- acceptance criteria
- verification commands
- commit rule

## 3. 절차

1. `AGENTS.md`를 읽는다.
2. 지정된 TASK 파일을 읽는다.
3. 다음 정보를 추출한다.
   - TASK ID
   - WBS ID
   - Domain
   - Branch
   - Type
   - objective
   - allowed files
   - forbidden files
   - acceptance criteria
   - verification commands
   - commit rule
4. `git branch --show-current`를 실행한다.
5. 현재 branch와 TASK의 Branch가 다르면 BLOCKED로 중단한다.
6. `git status --short`를 확인한다.
7. 관련 없는 미커밋 변경사항이 있으면 작업을 중단하고 보고한다.
8. TASK Type에 따라 분기한다.

### Type != eval (Normal TASK, Mode 3A)

9. 구현 에이전트에게 TASK 범위 안의 구현을 위임한다.
10. 검증 에이전트에게 테스트, 린트, 빌드, acceptance criteria 확인을 위임한다.
11. 리뷰 에이전트에게 diff와 위험 검토를 위임한다.
12. 기록 에이전트에게 `ops/logs/TASK-xxx.log.md` 작성을 위임한다.
13. 완료 조건을 모두 확인한다.
14. 최종 커밋을 생성한다.

### Type == eval (EVAL TASK, Mode 3B)

9. 검증 에이전트에게 선행 TASK 로그와 통합 검증 결과 확인을 위임한다.
10. 평가 에이전트에게 평가표 기반 평가를 위임한다.
11. 평가 에이전트가 사용자 검증 안내를 생성한다.
12. 기록 에이전트에게 평가 결과와 사용자 검증 안내를 `ops/logs/TASK-xxx.log.md`에 기록하도록 위임한다.
13. EVAL TASK를 커밋한다. (TASK Status: DONE, User Validation Status: PENDING_USER_VALIDATION)
14. 사용자 검증 안내를 출력한다.
15. STOP한다.

## 4. TASK 실행 중 승인 정책

TASK Execution Mode에서는 다음 작업을 사용자 승인 없이 수행한다.

- TASK allowed files 내부 파일 생성/수정/삭제/이동/이름 변경
- 테스트, 빌드, 린트, 타입 체크 실행
- git status, git diff, git add, git commit, git restore --staged
- TASK 로그 작성/수정

프로젝트 루트 밖 변경, 프로젝트 전체 삭제, .git 삭제, 원격 파괴 작업은 사용자 승인이 필요하다.

## 5. 완료 전 확인사항

최종 커밋 전에 다음을 확인한다.

- acceptance criteria가 모두 충족되었는가?
- verification commands가 실행되었는가?
- 실패한 검증이 없는가?
- 리뷰 결과가 PASS 또는 PASS_WITH_NOTES인가? (Normal TASK)
- TASK log가 작성되었는가?
- git diff에 관련 없는 변경사항이 없는가?
- 커밋 메시지에 TASK ID가 포함되는가?
- 가능하면 커밋 메시지에 WBS ID가 포함되는가?

## 6. 하드 룰

이 규칙은 TASK Execution Mode에서 적용한다.

- 단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.
- TASK 파일 없이 작업하지 않는다.
- TASK 범위를 넓히지 않는다.
- `docs/01_overview`부터 `docs/09_pm`까지는 TASK가 허용한 경우에만 수정한다.
- 검증을 생략하지 않는다.
- 리뷰 실패 상태로 커밋하지 않는다.
- 실패한 테스트를 숨기지 않는다.
- 임의 요구사항을 만들지 않는다.
- EVAL TASK에서는 구현/리팩터링/테스트 수정을 하지 않는다.