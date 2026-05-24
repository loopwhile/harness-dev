---
name: review-task
description: TASK 구현 diff를 기준으로 정확성, 범위 준수, 테스트, 보안, 유지보수성을 리뷰할 때 사용한다.
---

# Review Task Skill

## 1. 목적

이 스킬은 구현 결과를 최종 커밋하기 전에 검토한다.

검토 대상은 다음이다.

- TASK 범위 준수
- acceptance criteria 충족 여부
- 테스트 누락 여부
- 보안 위험
- 성능 위험
- 아키텍처 위반
- 계약 위반
- 불필요한 변경사항

## 2. 입력

필수 입력:

- TASK 파일
- git diff
- 구현 요약
- 검증 결과
- 변경 파일 목록

## 3. 절차

1. TASK objective를 확인한다.
2. allowed files와 forbidden files를 확인한다.
3. git diff를 검토한다.
4. acceptance criteria와 구현 결과를 비교한다.
5. 검증 결과를 확인한다.
6. 위험 요소를 기록한다.
7. 최종 verdict를 반환한다.

## 4. 리뷰 체크리스트

- TASK 범위를 벗어난 변경이 없는가?
- forbidden files가 수정되지 않았는가?
- acceptance criteria가 충족되었는가?
- 테스트 또는 검증이 충분한가?
- 기존 기능을 깨뜨릴 가능성은 없는가?
- 에러 처리는 적절한가?
- 보안 위험은 없는가?
- 성능 위험은 없는가?
- public contract 변경이 있는가?
- 변경이 과도하게 크지 않은가?
- 커밋에 포함되면 안 되는 파일이 없는가?

## 5. Verdict

리뷰 결과는 다음 중 하나로 반환한다.

| Verdict | 의미 |
|---|---|
| PASS | 커밋 가능 |
| PASS_WITH_NOTES | 커밋 가능하지만 후속 개선사항 있음 |
| FAIL | 커밋 불가 |

## 6. 하드 룰

- 검증 실패 상태를 PASS로 처리하지 않는다.
- forbidden files 수정이 있으면 FAIL 처리한다.
- 관련 없는 변경사항이 있으면 FAIL 처리한다.
- 코드를 직접 수정하지 않는다.
- 커밋하지 않는다.