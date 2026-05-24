# TASK Boundary Rule

## 목적

TASK 단위 실행 중 범위 오염을 막는다.

## 규칙

- 모든 작업은 `ops/tasks/TASK-xxx.md` 하나를 기준으로 한다.
- TASK 파일에 없는 요구사항은 구현하지 않는다.
- TASK의 allowed files 안에서만 수정한다.
- forbidden files는 수정하지 않는다.
- 상위 문서는 TASK에서 명시적으로 허용한 경우에만 수정한다.
- 여러 TASK를 한 번에 처리하지 않는다.
- 관련 없는 리팩터링을 추가하지 않는다.

## 중단 조건

다음 상황에서는 작업을 중단하고 보고한다.

- TASK 파일이 없음
- allowed files가 비어 있음
- forbidden files와 allowed files가 충돌함
- acceptance criteria가 없음
- 현재 git 상태에 관련 없는 변경사항이 있음