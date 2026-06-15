# TASK Boundary Rule

## 적용 범위

이 규칙은 **TASK Execution Mode**에서만 강하게 적용한다.

General / Analysis Mode에서는 TASK 없이도 저장소 분석, 문서 점검, 계획 작성이 가능하다.

## 규칙

- TASK Execution Mode에서의 모든 구현 작업은 `ops/tasks/TASK-xxx.md` 하나를 기준으로 한다.
- 단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.
- 단일 브랜치는 한 번에 하나의 Active TASK만 가진다.
- TASK 파일에 없는 요구사항은 구현하지 않는다.
- TASK의 allowed files 안에서만 수정한다.
- forbidden files는 수정하지 않는다.
- 상위 문서는 TASK에서 명시적으로 허용한 경우에만 수정한다.
- 여러 TASK를 한 번에 처리하지 않는다.
- 관련 없는 리팩터링을 추가하지 않는다.

## 브랜치 확인

TASK 실행 전 현재 git branch가 TASK의 Branch와 일치하는지 확인한다.

불일치 시 BLOCKED.

## 중단 조건

다음 상황에서는 작업을 중단하고 보고한다.

- TASK 파일이 없음
- allowed files가 비어 있음
- forbidden files와 allowed files가 충돌함
- acceptance criteria가 없음
- 현재 git 상태에 관련 없는 변경사항이 있음
- 현재 branch가 TASK의 Branch와 다름