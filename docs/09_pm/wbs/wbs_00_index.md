# WBS Index

## 1. 목적
현재 프로젝트의 WBS 구조와 활성 작업을 관리한다.

## 2. 상태 규칙
- READY: 시작 가능
- IN_PROGRESS: 현재 진행 중
- BLOCKED: 외부 결정 또는 수정 필요
- DONE: 완료

## 3. 현재 활성 WBS
- 활성 WBS 파일:
- 활성 항목:
- 상태:

## 4. WBS 목록
- `wbs_01_xxx.md`
- `wbs_02_xxx.md`
- `wbs_03_xxx.md`
- `wbs_04_xxx.md`
- `wbs_05_xxx.md`
- `wbs_06_xxx.md`

## 5. 운영 규칙
- 한 턴에 하나의 WBS 항목만 처리한다.
- 완료 처리는 검증 후 수행한다.
- blocker는 status report에도 반영한다.
- 사용자 승인 전에는 같은 턴에서 다음 `READY` task를 자동 실행하지 않는다.
- 종료 시 다음 실행을 위한 active pointer 준비는 허용한다.
- `HEAD@close`를 사용한 commit reference는 final report 또는 후속 sync task에서 resolved SHA로 보정할 수 있다.
