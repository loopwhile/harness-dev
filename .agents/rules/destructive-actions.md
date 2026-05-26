---
trigger: always_on
---

# Destructive Actions Rule

## 목적

이 규칙은 Antigravity CLI가 사용자 승인 없이 삭제 또는 파괴성 작업을 수행하지 않도록 제한한다.

## 자율 진행 가능 작업

TASK의 allowed files 범위 안에서 아래 작업은 사용자에게 묻지 않고 진행할 수 있다.

- 파일 읽기
- 파일 수정
- 새 파일 생성
- 디렉터리 생성
- 테스트 실행
- 린트 실행
- 타입 체크 실행
- 빌드 실행
- `git status` 확인
- `git diff` 확인
- `git add`
- 조건을 충족한 TASK 완료 커밋

단, 위 작업도 TASK 범위를 벗어나면 진행하지 않는다.

## 사용자 승인이 필요한 작업

아래 작업은 반드시 사용자에게 먼저 확인한다.

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
- `git checkout -- <file>`
- `git restore <file>`
- `git restore --staged <file>`
- force push
- branch 삭제
- tag 삭제
- migration rollback
- 데이터베이스 삭제
- 테이블 삭제
- 컬렉션 삭제
- 대량 데이터 삭제
- 대량 파일 이동
- 대량 파일명 변경
- TASK allowed files 밖의 변경
- TASK 범위를 넘어서는 구조 변경

## 특히 금지되는 작업

명시적 승인 없이 다음 작업은 절대 수행하지 않는다.

```bash
rm -rf
git clean -fd
git clean -fdx
git reset --hard
git push --force
git push --force-with-lease
drop database
drop table
truncate table
```

## 승인 요청 형식

삭제 또는 파괴성 작업이 필요한 경우 아래 형식으로 사용자에게 질문한다.

```text
삭제 또는 파괴성 작업 승인이 필요합니다.

대상:
- path/to/file

작업:
- 수행하려는 명령 또는 변경

이유:
- 해당 작업이 필요한 이유

위험:
- 되돌릴 수 없는 영향 또는 주의점

진행해도 될까요?
```

## 승인 전 대안 검토

파괴성 작업을 요청하기 전에 가능한 경우 다음 대안을 먼저 검토한다.

- 삭제 대신 비활성화
- 삭제 대신 백업 파일 생성
- 파일 이동 대신 새 파일 생성
- reset 대신 patch 수정
- clean 대신 대상 파일 목록 보고
- DB 삭제 대신 dry-run 또는 select 확인

## 승인 없는 경우

사용자 승인이 없으면 다음과 같이 처리한다.

- 파괴성 작업을 수행하지 않는다.
- 현재까지 완료한 작업을 보고한다.
- 필요한 후속 조치를 설명한다.
- TASK 상태를 BLOCKED로 기록한다.

## 로그 기록

파괴성 작업 승인을 받은 경우 `ops/logs/TASK-xxx.log.md`에 다음을 기록한다.

- 승인받은 작업
- 승인 시점
- 대상 파일 또는 리소스
- 수행한 명령
- 결과