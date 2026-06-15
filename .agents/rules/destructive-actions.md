---
trigger: always_on
---

# Destructive Actions Rule

## 적용 범위

이 규칙은 **TASK Execution Mode**에서의 파괴성 작업 정책을 정의한다.

General / Analysis Mode에서는 이 규칙의 대부분이 적용되지 않는다. 단, 프로젝트 루트 밖 파괴와 원격/외부 시스템 파괴는 모든 모드에서 금지한다.

## 목적

이 규칙은 프로젝트 루트 밖 변경, 전체 삭제, 원격/외부 시스템 파괴만 차단한다.

TASK Execution Mode에서 TASK allowed files 내부 변경은 사용자 승인 없이 자율 진행한다.

## TASK Execution Mode에서 사용자 승인 없이 허용하는 작업

TASK의 allowed files 범위 안에서 아래 작업은 사용자에게 묻지 않고 진행한다.

- 파일 읽기
- 파일 수정
- 새 파일 생성
- 파일 삭제
- 파일 이동/이름 변경
- 디렉터리 생성
- 디렉터리 정리
- 테스트 파일 추가/수정/삭제
- 테스트 실행
- 린트 실행
- 타입 체크 실행
- 빌드 실행
- `git status` 확인
- `git diff` 확인
- `git add`
- `git commit`
- `git restore --staged`
- 조건을 충족한 TASK 완료 커밋
- TASK 로그 작성/수정

단, 위 작업도 TASK 범위를 벗어나면 진행하지 않는다.

## 절대 금지 작업

명시적 승인 없이 다음 작업은 절대 수행하지 않는다.

```bash
rm -rf /
rm -rf .
rm -rf ..
rm -rf ./*
rm -rf "$PROJECT_ROOT"
rm -rf "$(pwd)"
find / -delete
find .. -delete
git clean -fdx
git reset --hard
git push --force
git push --force-with-lease
drop database
drop table
truncate table
```

## 사용자 승인이 필요한 작업

아래 작업은 반드시 사용자에게 먼저 확인한다.

- 프로젝트 루트 밖 파일 생성/수정/삭제
- 프로젝트 루트 전체 삭제
- .git 디렉터리 삭제
- `git clean -fdx`
- `git reset --hard`
- `git push --force`
- 원격 브랜치 삭제
- tag 삭제
- migration rollback
- 데이터베이스 삭제
- 테이블 삭제
- 컬렉션 삭제
- 대량 데이터 삭제
- 운영 서버/외부 서버 파일 삭제
- TASK allowed files 밖의 변경
- TASK 범위를 넘어서는 구조 변경

## 승인 요청 형식

사용자 승인이 필요한 작업의 경우 아래 형식으로 질문한다.

```text
파괴성 작업 승인이 필요합니다.

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