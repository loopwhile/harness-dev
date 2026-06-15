---
name: implement-task
description: TASK 파일의 허용 범위 안에서 최소 변경으로 구현을 수행할 때 사용한다. Normal TASK Flow에서만 사용한다.
---

# Implement Task Skill

## 1. 목적

이 스킬은 지정된 TASK의 acceptance criteria를 만족하는 최소 구현을 수행한다.

Normal TASK Flow (Mode 3A)에서만 사용한다. EVAL TASK에서는 사용하지 않는다.

## 2. 입력

필수 입력:

- TASK 파일
- objective
- allowed files
- forbidden files
- implementation requirements
- acceptance criteria
- 관련 문서 또는 계약

## 3. 절차

1. TASK 파일을 읽는다.
2. objective와 acceptance criteria를 확인한다.
3. allowed files와 forbidden files를 확인한다.
4. 필요한 문서와 소스 파일만 읽는다.
5. 최소 변경 계획을 세운다.
6. 허용된 파일만 수정한다.
7. allowed files 내부 생성/수정/삭제/이동/이름 변경은 사용자 승인 없이 수행한다.
8. 동작 변경이 있으면 필요한 테스트를 추가하거나 수정한다.
9. 구현 결과를 요약한다.

## 4. 구현 원칙

- 작고 명확한 변경을 선호한다.
- 기존 아키텍처를 존중한다.
- 기존 네이밍 컨벤션을 따른다.
- public contract 변경은 TASK가 명시한 경우에만 수행한다.
- 테스트 가능한 구조를 우선한다.
- 불필요한 추상화는 추가하지 않는다.
- 지금 필요한 구현만 수행한다.

## 5. 출력

구현 완료 후 다음을 보고한다.

- 수정한 파일 목록 (변경 유형 포함: created, modified, deleted, renamed, moved)
- 각 파일의 변경 요약
- acceptance criteria 충족 방식
- 추가한 테스트
- 남은 위험 또는 주의사항

## 6. 하드 룰

- forbidden files를 수정하지 않는다.
- 프로젝트 루트 밖 파일을 변경하지 않는다.
- TASK에 없는 리팩터링을 하지 않는다.
- TASK에 없는 기능을 추가하지 않는다.
- 상위 문서를 임의로 수정하지 않는다.
- 커밋하지 않는다.
- 검증 결과를 조작하지 않는다.
- EVAL TASK에서 사용하지 않는다.