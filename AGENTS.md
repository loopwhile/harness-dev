# AGENTS.md

## 1. 프로젝트 목적

이 저장소는 AI 하네스 엔지니어링을 위한 표준 프로젝트 템플릿이다.

목표는 다음과 같다.

1. Mode 2에서 AI 제품팀이 기획/설계/명세/디자인 전달 문서를 완성한다.
2. Mode 3에서 AI 개발팀이 TASK 단위로 구현/검증/커밋한다.
3. 각 TASK는 `ops/tasks/TASK-xxx.md` 파일 하나로 정의한다.
4. 작업은 오케스트레이션 에이전트가 관리한다.
5. 구현, 검증, 리뷰, 기록은 각각 분리된 에이전트 또는 스킬이 담당한다.
6. 모든 완료 작업은 TASK 번호와 WBS 번호가 포함된 커밋으로 닫는다.
7. 기능 완료 시점에 EVAL TASK로 품질 평가와 사용자 검증 게이트를 운영한다.

## 2. 하네스 작동 모드

하네스는 항상 모든 작업을 막는 전역 족쇄가 아니다.

작동 모드는 다음 3가지로 구분한다.

### Mode 1. General / Analysis Mode

- TASK 없이 가능
- 저장소 분석
- GitHub 확인
- 문서 점검
- 구조 검토
- 수정 계획 작성
- WBS/TASK 작성 전 사전 검토
- 사용자 질문 답변

### Mode 2. Planning / Specification Mode

- TASK 없이 가능
- 제품 정의 (product_brief, PRD, scope, business_rules)
- 요구사항 정리
- 기능명세 작성 (functional_spec)
- 사용자 흐름 작성 (user_flows)
- 화면정의 작성 (screen_definition)
- Stitch 프롬프트 작성
- Stitch 결과 정리
- UI handoff 작성
- 시스템 아키텍처 작성
- 시퀀스 다이어그램 작성
- ERD / 테이블 명세 작성
- API / 상태 / 에러 명세 작성
- WBS / TASK 생성
- EVAL TASK 배치
- 개발 착수 가능성 리뷰

Mode 2에서는 소스 코드 구현을 수행하지 않는다.
Mode 2의 최종 산출물은 Mode 3 TASK Execution Mode의 입력이 된다.

### Mode 3. TASK Execution Mode

- `execute-task` 또는 `antigravity-execute-task` 스킬 사용 시에만 활성화
- `ops/tasks/TASK-xxx.md` 기준으로 실행
- TASK 파일 필수
- allowed files / forbidden files 적용
- 검증 / 리뷰 / 기록 / 커밋 수행

#### Mode 3A. Normal TASK Flow

- Type: feature / fix / refactor / docs / test / infra
- 실행 흐름:

```text
orchestrator → implementer → verifier → reviewer → recorder → commit → user report
```

#### Mode 3B. EVAL TASK Flow

- Type: eval
- 실행 흐름:

```text
orchestrator → verifier → evaluator → recorder → commit → user validation guide → STOP
```

EVAL TASK는 TASK Execution Mode 내부에서 Type: eval일 때 활성화되는 특수 Flow다.

### 핵심 정책

```text
TASK는 TASK Execution Mode에서만 필수다.
General / Analysis Mode와 Planning / Specification Mode에서는 TASK 없이도 분석, 점검, 계획 작성, 기획/설계/명세 작성, WBS/TASK 설계가 가능하다.
Mode 2에서는 코드 구현을 수행하지 않는다. Mode 3 TASK Execution에서만 구현한다.
```

## 3. 진실 공급원

이 프로젝트의 진실 공급원은 다음 순서를 따른다.

1. `docs/`  
   제품, 요구사항, 아키텍처, 계약, 개발, 테스트, 운영, PM 문서

2. `docs/09_pm/wbs/`  
   WBS 항목과 작업 분해 기준

3. `ops/tasks/TASK-xxx.md`  
   실제 CLI 에이전트가 실행할 단위 작업

4. `ops/logs/`  
   TASK 실행 결과, 검증 증거, 리뷰 결과, 커밋 기록

## 4. TASK 실행 흐름

### 일반 TASK (Mode 3A)

1. 오케스트레이션 에이전트가 TASK 파일을 읽는다.
2. 현재 git branch가 TASK의 Branch와 일치하는지 확인한다.
3. 오케스트레이션 에이전트가 TASK 범위, 허용 파일, 금지 파일, 검증 기준을 확인한다.
4. 구현 에이전트가 허용된 범위 안에서만 수정한다.
5. 검증 에이전트가 테스트, 린트, 빌드, 수동 검증 기준을 확인한다.
6. 리뷰 에이전트가 diff, 범위 이탈, 위험 요소를 검토한다.
7. 기록 에이전트가 `ops/logs/`에 실행 기록을 남긴다.
8. 오케스트레이션 에이전트가 최종 커밋을 생성한다.

### EVAL TASK (Mode 3B)

1. 오케스트레이션 에이전트가 EVAL TASK를 읽는다.
2. 현재 git branch가 TASK의 Branch와 일치하는지 확인한다.
3. 통합 검증을 수행한다.
4. 평가 에이전트가 평가표 기반 평가를 수행한다.
5. 평가 에이전트가 사용자 검증 안내를 생성한다.
6. 기록 에이전트가 평가 결과와 사용자 검증 안내를 기록한다.
7. EVAL TASK를 커밋한다.
8. 사용자 검증 안내를 출력하고 중단한다.
9. 사용자 APPROVED 후 다음 기능 그룹으로 진행한다.

## 5. TASK 실행 중 승인 정책

### TASK 실행 중 사용자 승인 없이 허용하는 작업

`execute-task` 또는 `antigravity-execute-task` 실행 중에는 아래 작업을 사용자 승인 없이 수행한다.

- TASK allowed files 내부 파일 생성
- TASK allowed files 내부 파일 수정
- TASK allowed files 내부 파일 삭제
- TASK allowed files 내부 파일 이동/이름 변경
- TASK allowed files 내부 디렉터리 생성
- TASK allowed files 내부 디렉터리 정리
- 테스트 파일 추가/수정/삭제
- 검증 명령 실행
- 빌드 명령 실행
- 린트 명령 실행
- 타입 체크 실행
- git status
- git diff
- git add
- git commit
- git restore --staged
- TASK 로그 작성/수정

### 절대 금지 또는 사용자 승인 필요 작업

아래 작업은 여전히 금지하거나 사용자 승인이 필요하다.

- 프로젝트 루트 밖 파일 생성/수정/삭제
- 프로젝트 루트 전체 삭제
- .git 디렉터리 삭제
- `rm -rf /`, `rm -rf .`, `rm -rf ..`, `rm -rf ./*`
- `git clean -fdx`
- `git reset --hard`
- `git push --force`
- 원격 브랜치 삭제
- DB drop, 테이블 drop
- 운영 서버/외부 서버 파일 삭제
- TASK allowed files 밖 변경

정책 요약:

```text
TASK 내부 변경은 허용한다.
프로젝트 루트 밖 파괴와 원격/외부 시스템 파괴만 막는다.
```

## 6. Active TASK 정책

단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.

단일 브랜치는 한 번에 하나의 Active TASK만 가진다.

프로젝트 전체에서는 여러 도메인 브랜치가 각자 다른 TASK를 병렬로 실행할 수 있다.

```text
전역 Active TASK 1개 ❌
브랜치별 Active TASK 1개 ✅
에이전트 세션별 Active TASK 1개 ✅
```

## 7. 도메인 브랜치 정책

브랜치 기본 구조:

```text
main
└─ dev
   ├─ common
   ├─ auth
   ├─ reservation
   ├─ payment
   ├─ board
   └─ notification
```

공통 모듈은 먼저 `common` 브랜치에서 처리한다.

각 WBS와 TASK는 실행 Branch를 명시한다.

TASK 실행 스킬은 실행 전 현재 git branch가 TASK의 Branch와 일치하는지 확인한다.

일치하지 않으면 작업을 중단하고 보고한다.

## 8. 작업 경계 규칙

### TASK Execution Mode (Mode 3)에서의 규칙

- TASK 파일에 명시된 작업만 수행한다.
- TASK의 allowed files 안에서만 수정한다.
- TASK의 forbidden files는 수정하지 않는다.
- TASK가 명시적으로 허용하지 않으면 `docs/01_overview`부터 `docs/09_pm`까지 수정하지 않는다.
- 요구사항을 임의로 만들지 않는다.
- 대규모 리팩터링을 임의로 수행하지 않는다.
- TASK 범위를 벗어난 개선 작업을 끼워 넣지 않는다.
- 검증을 생략하지 않는다.
- 검증 또는 리뷰가 실패하면 커밋하지 않는다.

### General / Analysis Mode와 Planning / Specification Mode에서의 규칙

- TASK 없이도 저장소 분석, 문서 점검, 계획 작성, 기획/설계/명세 작성이 가능하다.
- 구현 코드 변경은 TASK Execution Mode에서만 수행한다.
- Mode 2에서는 소스 코드 구현을 하지 않는다.

## 9. 커밋 규칙

TASK 완료 커밋은 반드시 TASK 번호를 포함한다.

권장 형식:

```text
TASK-001 WBS-01-001: implement login API boundary
```

문서 작업의 경우:

```text
TASK-002 WBS-01-002: update API contract template
```

## 10. 완료 기준

TASK는 다음 조건을 모두 만족해야 완료로 본다.

- TASK의 acceptance criteria가 충족됨
- 검증 명령 또는 검증 기준이 실행됨
- 검증 결과가 기록됨
- 리뷰 결과가 기록됨
- `ops/logs/TASK-xxx.log.md`가 생성 또는 갱신됨
- 최종 커밋 메시지에 TASK 번호가 포함됨
- 가능하면 WBS 번호도 커밋 메시지에 포함됨
- 관련 없는 변경사항이 남아 있지 않음

## 11. 주요 디렉터리

| 경로 | 역할 |
|---|---|
| `AGENTS.md` | 프로젝트 공통 헌법 |
| `.agents/skills/` | 공통 에이전트 스킬 원본 |
| `.agents/rules/` | Antigravity 행동 규칙 |
| `.agents/agents/` | Antigravity runtime subagent 정의 |
| `.agents/hooks/` | Antigravity lifecycle hook 스크립트 |
| `.agents/templates/` | 기획/설계용 템플릿 (Mode 2) |
| `.codex/agents/` | Codex 전용 custom subagent 정의 |
| `.codex/hooks/` | Codex lifecycle hook 스크립트 |
| `.codex/rules/` | Codex 작업 정책 문서 |
| `docs/` | 프로젝트 상위 문서 |
| `docs/09_pm/wbs/` | WBS 문서 |
| `ops/tasks/` | 실행 가능한 TASK 파일 |
| `ops/logs/` | TASK 실행 기록 |
| `ops/templates/` | TASK, log, 평가표, 사용자 검증, WBS 분해 템플릿 |

## 12. 기본 에이전트 행동

에이전트는 다음 순서로 행동한다.

1. 먼저 `AGENTS.md`를 확인한다.
2. 현재 모드(General / Planning / TASK Execution)를 판단한다.
3. TASK Execution Mode라면 지정된 TASK 파일을 확인한다.
4. TASK가 참조하는 WBS, 요구사항, 계약, 아키텍처 문서만 읽는다.
5. 필요한 소스 파일만 읽는다.
6. 허용된 파일만 수정한다.
7. 검증 결과를 명확히 남긴다.
8. 최종 보고 전에 git diff와 git status를 확인한다.

## 13. 금지 사항

- 허용 파일 외 수정 금지 (TASK Execution Mode)
- 상위 문서 임의 수정 금지
- 임의 요구사항 생성 금지
- 검증 없는 완료 처리 금지 (TASK Execution Mode)
- 실패한 작업 커밋 금지
- 여러 TASK를 하나의 커밋에 섞기 금지

## 14. Evaluation and User Validation Policy

Full evaluation and user validation are not required for every TASK.

Each normal TASK must still pass:

- implementation boundary check
- verification
- review
- execution logging
- commit rule

Full evaluation is required at feature completion checkpoints.

Feature completion checkpoints are represented as explicit EVAL TASKs.

Examples:

- TASK-026 EVAL: 회원가입 기능 평가 및 사용자 검증 안내
- TASK-032 EVAL: 로그인 기능 평가 및 사용자 검증 안내
- TASK-099 EVAL: 회원 도메인 전체 통합 평가 및 사용자 검증 안내

User validation is required only after a feature-level or WBS-level EVAL TASK.

The agent must not continue to the next feature group until user validation is APPROVED.

EVAL TASK는 평가 완료 시점에 평가 로그와 사용자 검증 안내를 커밋한다.

커밋하되 TASK Status는 `DONE`으로 둔다. User Validation Status는 `PENDING_USER_VALIDATION`으로 둔다.

사용자가 APPROVED를 명시하기 전까지 다음 feature group 또는 WBS group으로 진행하지 않는다.

## 15. 상태 체계

### TASK / WBS Status

```text
TODO
READY
IN_PROGRESS
BLOCKED
DONE
```

### User Validation Status

```text
PENDING_USER_VALIDATION
APPROVED
REQUEST_CHANGES
REJECTED
DEFERRED
```

TASK 상태와 사용자 검증 상태는 별도 필드다.

## 16. 최종 정책 문구

하네스는 항상 모든 작업을 막는 전역 족쇄가 아니다.

General / Analysis Mode에서는 TASK 없이도 저장소 분석, 문서 점검, 계획 작성이 가능하다.

Planning / Specification Mode에서는 TASK 없이도 기획/설계/명세/디자인 전달 문서 작성, WBS/TASK 설계가 가능하다. 소스 코드 구현은 수행하지 않는다.

TASK Execution Mode는 사용자가 execute-task 또는 antigravity-execute-task 스킬로 특정 ops/tasks/TASK-xxx.md 실행을 요청한 경우에만 활성화된다.

TASK Execution Mode에서는 에이전트가 TASK 완료에 필요한 코드 작성, 수정, 삭제, 테스트, 빌드, git add, git commit을 사용자 승인 없이 진행한다.

사용자 승인은 프로젝트 루트 밖 변경, 프로젝트 전체 삭제, .git 삭제, 원격 파괴 작업, 외부 시스템 파괴 작업에만 필요하다.

단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.

단일 브랜치는 한 번에 하나의 Active TASK만 가진다.

프로젝트 전체에서는 여러 도메인 브랜치가 각자 다른 TASK를 병렬로 실행할 수 있다.

각 WBS와 TASK는 실행 Branch를 명시한다.

TASK 실행 스킬은 실행 전 현재 git branch가 TASK의 Branch와 일치하는지 확인한다.

EVAL TASK는 TASK Execution Mode 내부에서 Type: eval일 때 활성화되는 특수 Flow다.

ops/에는 tasks, logs, templates만 둔다.

기획/설계용 템플릿은 `.agents/templates/`에 둔다.