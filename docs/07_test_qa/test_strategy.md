# Test Strategy

## 1. 테스트 레벨
- unit
- integration
- e2e

## 2. 기본 원칙
- 작은 범위부터 검증한다.
- 변경 범위와 가까운 테스트를 우선한다.
- 실패 원인을 기록한다.

## 3. 작업 유형별 권장 검증
- 문서 작업: doc consistency
- 구조 변경: typecheck + build
- 기능 변경: test + typecheck + build
