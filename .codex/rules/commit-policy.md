# Commit Policy

## 적용 범위

이 규칙은 **TASK Execution Mode**에서 적용한다.

## 기본 원칙

하나의 TASK는 하나의 커밋으로 닫는다.

## 커밋 메시지 형식

```text
TASK-XXX WBS-XX-XXX: short summary
```

예시:

```text
TASK-001 WBS-01-001: implement reservation creation API
```

## 규칙

- TASK ID는 필수다.
- WBS ID는 가능하면 포함한다.
- 커밋 메시지는 작업 결과를 짧고 명확하게 설명한다.
- 검증 실패 상태로 커밋하지 않는다.
- 리뷰 실패 상태로 커밋하지 않는다.
- 관련 없는 변경사항을 같은 커밋에 포함하지 않는다.

## 금지 예시

```text
fix stuff
```

```text
update files
```

```text
TASK done
```