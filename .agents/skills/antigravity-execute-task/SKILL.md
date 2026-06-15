---
name: antigravity-execute-task
description: Antigravity CLI에서 ops/tasks/TASK-xxx.md 하나를 기준으로 작업을 실행한다. 런타임 subagent를 동적으로 정의해 계획, 구현, 검증, 리뷰, 기록, 커밋 흐름을 통제한다.
---

# Antigravity Execute Task Skill

## 1. 목적

이 스킬은 Antigravity CLI에서 `ops/tasks/TASK-xxx.md` 하나를 기준으로 작업을 실행하기 위한 절차다.

이 스킬이 호출되면 **TASK Execution Mode**가 활성화된다.

이 저장소의 실제 작업 단위는 Antigravity 내부 artifact가 아니라 반드시 `ops/tasks/TASK-xxx.md`다.

Antigravity가 생성하는 다음 artifact는 보조 산출물로만 사용한다.

- `task.md`
- `implementation_plan.md`
- `walkthrough.md`
- Antigravity 내부 task list
- Antigravity brain 내부 파일

최종 실행 기록은 반드시 다음 경로에 남긴다.

```text
ops/logs/TASK-xxx.log.md
```

## 2. 반드시 따라야 할 기준 파일

작업을 시작하기 전에 반드시 아래 파일과 디렉터리를 확인한다.

```text
AGENTS.md
.agents/rules/**
ops/tasks/TASK-xxx.md
```

`AGENTS.md`는 프로젝트 공통 헌법이다.

`.agents/rules/**`는 Antigravity workspace rule이다.

`ops/tasks/TASK-xxx.md`는 해당 작업의 실제 계약서다.

## 3. 기본 원칙

- 단일 에이전트 세션은 한 번에 하나의 TASK만 실행한다.
- TASK 파일에 없는 요구사항을 임의로 만들지 않는다.
- TASK 범위를 임의로 확장하지 않는다.
- TASK의 `allowed files` 안에서만 수정한다.
- TASK의 `forbidden files`는 절대 수정하지 않는다.
- TASK가 명시적으로 허용하지 않으면 `docs/01_overview`부터 `docs/09_pm`까지 수정하지 않는다.
- 관련 없는 리팩터링을 하지 않는다.
- 관련 없는 포맷팅 변경을 하지 않는다.
- 관련 없는 파일 이동 또는 이름 변경을 하지 않는다.
- 검증 없이 완료 처리하지 않는다.
- 리뷰 없이 커밋하지 않는다. (Normal TASK)
- 실행 기록 없이 완료 처리하지 않는다.
- 검증과 리뷰가 통과한 경우에만 커밋한다.

## 4. TASK 실행 중 사용자 승인 없이 허용하는 작업

TASK의 allowed files 범위 안에서 아래 작업은 사용자에게 묻지 않고 진행한다.

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

## 5. 절대 금지 또는 사용자 승인 필요

- 프로젝트 루트 밖 파일 생성/수정/삭제
- 프로젝트 루트 전체 삭제
- .git 디렉터리 삭제
- `rm -rf /`, `rm -rf .`, `rm -rf ..`, `rm -rf ./*`
- `git clean -fdx`
- `git reset --hard`
- `git push --force`
- 원격 브랜치 삭제
- DB drop, 테이블 drop
- TASK allowed files 밖의 파일 변경

## 6. Antigravity 런타임 subagent 운영 방식

Antigravity CLI는 `.agents/agents/*/agent.json` 파일을 서브에이전트 정의의 진실 공급원으로 사용한다.

메인 에이전트(orchestrator)는 TASK 실행 중 다음 절차로 runtime subagent를 정의하고 호출한다.

1. `.agents/agents/<role>/agent.json` 파일을 읽는다. (대상: implementer, verifier, reviewer, evaluator, recorder)
2. `config.customAgent.systemPromptSections[0].content` 값을 시스템 프롬프트로 추출한다.
3. `config.customAgent.toolNames` 배열을 확인하여 도구 권한을 결정한다.
   - `write_to_file`, `replace_file_content`, `multi_replace_file_content` 중 하나라도 포함되면 `enable_write_tools = true`
   - 포함되지 않으면 `enable_write_tools = false`
4. `define_subagent`를 호출하여 런타임 서브에이전트를 등록한다.
5. `invoke_subagent`로 해당 서브에이전트를 실행한다.

agent.json 파일이 없는 역할은 SKILL.md에 정의된 기본 역할 정의를 사용한다.

### 도구 권한 매핑

agent.json의 `toolNames`를 `define_subagent` 파라미터로 매핑한다.

| agent.json toolNames 포함 여부 | define_subagent 파라미터 |
|:---|:---|
| `write_to_file` 또는 `replace_file_content` 포함 | `enable_write_tools = true` |
| 위 도구 미포함 | `enable_write_tools = false` |
| `search_web` 또는 `read_url_content` 포함 | 시스템 프롬프트에 웹 조사 허용 명시 |
| MCP 도구 참조 | `enable_mcp_tools = true` |
| `invoke_subagent` 또는 `define_subagent` 포함 | `enable_subagent_tools = true` |

### 기본 역할별 도구 권한 (현재 agent.json 기준)

| 역할 | write_tools | mcp_tools | subagent_tools |
|:---|:---|:---|:---|
| implementer | ✅ true | false | false |
| verifier | ❌ false | false | false |
| reviewer | ❌ false | false | false |
| evaluator | ❌ false | false | false |
| recorder | ✅ true | false | false |

권장 runtime subagent 역할은 다음과 같다.

```text
orchestrator
implementer
verifier
reviewer
evaluator
recorder
```

작업 규모가 작으면 모든 역할을 반드시 별도 subagent로 나누지 않아도 된다.

그러나 다음 역할의 책임은 반드시 분리해서 수행해야 한다.

- 구현 책임
- 검증 책임
- 리뷰 책임
- 평가 책임 (EVAL TASK)
- 기록 책임
- 최종 완료 판단 책임

## 7. runtime subagent 역할 정의

### 7.1 orchestrator

#### 역할

orchestrator는 TASK 전체 흐름을 조율한다.

TASK Execution Mode에서만 강한 하네스를 적용한다.

반드시 다음 정보를 TASK에서 추출한다.

- TASK ID
- WBS ID
- Domain
- Branch
- objective
- source context
- allowed files
- forbidden files
- implementation requirements
- acceptance criteria
- verification commands
- commit rule

orchestrator는 다음을 확인한다.

- 현재 git branch와 TASK Branch 일치 여부
- 작업 전 `git status --short`
- 관련 없는 미커밋 변경사항 존재 여부
- TASK 범위 준수 여부
- TASK Type에 따른 분기 (Normal TASK vs EVAL TASK)
- 구현 결과
- 검증 결과
- 리뷰 결과
- 기록 결과
- 커밋 가능 여부

TASK allowed files 내부 변경/삭제/git commit은 사용자 승인 없이 진행한다.

프로젝트 루트 밖 변경/전체 삭제/원격 파괴만 사용자 승인이 필요하다.

#### 금지

- TASK 범위 확장
- TASK에 없는 요구사항 추가
- 검증 실패 상태에서 완료 처리
- 리뷰 실패 상태에서 완료 처리
- 실행 기록 없이 완료 처리
- 커밋 조건 미충족 상태에서 커밋

### 7.2 implementer

#### 역할

implementer는 TASK의 implementation requirements를 구현한다. Normal TASK Flow에서만 사용한다.

반드시 다음 원칙을 따른다.

- allowed files 안에서만 수정한다.
- forbidden files는 수정하지 않는다.
- allowed files 내부 생성/수정/삭제/이동/이름 변경은 사용자 승인 없이 수행한다.
- 필요한 경우에만 테스트를 추가하거나 수정한다.
- 변경사항은 최소 단위로 유지한다.
- 설계 문서, 계약 문서, WBS 문서는 TASK가 허용한 경우에만 수정한다.
- 구현 후 변경 파일 목록을 보고한다.

#### 금지

- forbidden files 수정
- allowed files 밖 수정
- 프로젝트 루트 밖 변경
- 관련 없는 리팩터링
- 관련 없는 포맷팅
- 불필요한 의존성 추가
- 불필요한 파일 생성
- 커밋
- EVAL TASK에서 사용

### 7.3 verifier

#### 역할

verifier는 TASK의 verification commands를 실행하고 acceptance criteria를 확인한다.

Normal TASK에서는 verification commands를 실행한다.

EVAL TASK에서는 선행 TASK 로그와 통합 검증 결과를 확인한다.

반드시 다음을 기록한다.

- 실행한 명령어
- 실행 결과
- 성공 여부
- 실패 시 오류 요약
- 실패 시 재현 방법
- 실행하지 못한 명령이 있다면 그 이유

검증 결과는 다음 중 하나로 정리한다.

```text
PASS
FAIL
BLOCKED
```

#### 금지

- 실행하지 않은 검증을 PASS 처리
- 실패한 검증을 PASS 처리
- acceptance criteria 미확인 상태에서 PASS 처리
- 커밋

### 7.4 reviewer

#### 역할

reviewer는 `git diff`를 기준으로 변경사항을 검토한다. Normal TASK에서는 필수. EVAL TASK에서는 선택 사항.

반드시 다음을 확인한다.

- TASK 범위 준수 여부
- allowed files 준수 여부
- forbidden files 수정 여부
- 관련 없는 변경 포함 여부
- 요구사항 누락 여부
- 보안 위험
- 성능 위험
- 아키텍처 경계 위반
- API/data/UI 계약 위반
- 테스트 또는 검증 누락
- 유지보수성 문제

리뷰 verdict는 다음 중 하나여야 한다.

```text
PASS
PASS_WITH_NOTES
FAIL
```

#### 금지

- 검증 실패 상태를 PASS 처리
- forbidden files 수정 승인
- 관련 없는 변경 승인
- 커밋

### 7.5 recorder

#### 역할

recorder는 최종 실행 기록을 작성한다.

기록 파일 경로는 반드시 다음 형식을 따른다.

```text
ops/logs/TASK-xxx.log.md
```

기록에는 다음을 포함한다.

- TASK ID
- WBS ID
- Domain
- Branch
- 작업 요약
- 수정 파일 목록 (변경 유형 포함: created, modified, deleted, renamed, moved)
- 구현 내용 요약
- 검증 명령과 결과
- acceptance criteria 충족 여부
- 리뷰 verdict
- 남은 위험
- 후속 작업
- 커밋 메시지
- 커밋 해시

#### 금지

- 실행하지 않은 검증 기록
- 실패한 검증을 성공으로 기록
- 리뷰 실패를 성공으로 기록
- 커밋하지 않았는데 커밋한 것처럼 기록
- TASK 범위 밖 문서 수정
- 커밋

### 7.6 evaluator

#### 역할

evaluator는 EVAL TASK에서 기능 또는 도메인 단위의 구현 품질을 평가한다. Type: eval TASK에서만 사용한다.

반드시 다음을 수행한다.

- 선행 TASK 로그를 읽어 구현, 검증, 리뷰 결과를 확인한다.
- 평가표 템플릿(ops/templates/feature-evaluation.template.md)에 맞춰 8개 영역을 평가한다.
- 각 영역에 등급(EXCELLENT/GOOD/ACCEPTABLE/NEEDS_IMPROVEMENT/FAIL)을 부여한다.
- 최종 verdict(PASS/CONDITIONAL_PASS/FAIL/BLOCKED)를 결정한다.
- 사용자 검증 안내(ops/templates/user-validation.template.md)를 생성한다.

#### 금지

- 구현 파일 수정
- 리팩터링
- 테스트 수정
- 커밋
- 삭제/파괴성 작업
- TASK 범위 확장
- 평가 증거 조작
- FAIL 시 자동 재실행

## 8. 실행 절차

### 8.1 준비

1. `AGENTS.md`를 읽는다.
2. `.agents/rules/**`를 읽는다.
3. 지정된 `ops/tasks/TASK-xxx.md`를 읽는다.
4. TASK 계약을 추출한다. (TASK ID, WBS ID, Domain, Branch, Type 포함)
5. 현재 git branch를 확인한다.
   ```bash
   git branch --show-current
   ```
6. 현재 branch가 TASK의 Branch와 일치하는지 확인한다. 불일치 시 BLOCKED.
7. `git status --short`를 실행한다.
8. 관련 없는 미커밋 변경사항이 있으면 작업을 중단하고 보고한다.

### 8.2 계획

1. TASK objective를 확인한다.
2. source context를 확인한다.
3. allowed files와 forbidden files를 확인한다.
4. implementation requirements를 작업 단위로 나눈다.
5. acceptance criteria를 검증 가능한 체크리스트로 변환한다.
6. verification commands를 확인한다.
7. TASK Type에 따라 필요한 runtime subagent 역할을 정한다.
   - Normal TASK (Mode 3A): implementer, verifier, reviewer, recorder
   - EVAL TASK (Mode 3B): verifier(통합 검증), evaluator, recorder
8. 각 역할의 `.agents/agents/<role>/agent.json`을 읽어 시스템 프롬프트와 도구 권한을 확인한다.
9. `define_subagent`로 각 역할의 런타임 서브에이전트를 등록한다.

### 8.3 구현 (Normal TASK, Mode 3A)

1. implementer 역할로 구현한다.
2. allowed files 안에서만 수정한다.
3. 필요한 경우 테스트를 추가하거나 수정한다.
4. 구현 후 `git diff --stat`을 확인한다.
5. 구현 후 `git diff`를 확인한다.

### 8.4 검증

1. TASK의 verification commands를 실행한다.
2. acceptance criteria를 하나씩 확인한다.
3. 실패한 항목이 있으면 구현 단계로 되돌아간다.
4. 환경 문제로 실행하지 못한 검증은 BLOCKED로 기록하고 이유를 설명한다.

### 8.5 리뷰 (Normal TASK, Mode 3A)

1. reviewer 역할로 `git diff`를 검토한다.
2. TASK 범위 준수 여부를 확인한다.
3. forbidden files 수정 여부를 확인한다.
4. 검증 결과를 확인한다.
5. PASS, PASS_WITH_NOTES, FAIL 중 하나의 verdict를 낸다.
6. FAIL이면 구현 단계로 되돌아간다.

### 8.6 기록

1. recorder 역할로 `ops/logs/TASK-xxx.log.md`를 작성 또는 갱신한다.
2. 구현, 검증, 리뷰 결과를 기록한다.
3. 남은 위험과 후속 작업을 기록한다.

### 8.7 EVAL TASK 분기 (EVAL TASK 전용, Mode 3B)

TASK Type이 `eval`인 경우 일반 TASK 흐름(8.3~8.6) 대신 다음 경로를 따른다.

1. EVAL TASK의 Evaluation Scope를 확인한다.
2. 선행 TASK 로그(`ops/logs/TASK-xxx.log.md`)를 읽는다.
3. 통합 검증이 필요하면 verifier 역할로 verification commands를 실행한다.
4. evaluator 역할로 평가표 기반 평가를 수행한다.
5. evaluator가 사용자 검증 안내를 생성한다.
6. recorder 역할로 평가 결과와 사용자 검증 안내를 `ops/logs/TASK-xxx.log.md`에 기록한다.
7. EVAL TASK를 커밋한다. (TASK Status: DONE, User Validation Status: PENDING_USER_VALIDATION)
8. 사용자 검증 안내를 출력한다.
9. STOP한다.
10. 사용자 APPROVED 후 다음 기능 그룹으로 진행한다.

EVAL TASK에서 evaluator가 FAIL 또는 BLOCKED를 반환하면:

1. 평가 결과를 기록한다.
2. 사용자에게 보고하고 중단한다.
3. 자동으로 이전 TASK를 재실행하지 않는다.
4. 필요하면 correction TASK를 새로 만들거나 사용자가 재작업 방향을 승인한 뒤 진행한다.

### 8.8 커밋

검증과 리뷰가 통과한 경우에만 커밋한다.

커밋 조건은 다음과 같다.

- acceptance criteria 충족
- verification result가 PASS
- review verdict가 PASS 또는 PASS_WITH_NOTES (Normal TASK)
- `ops/logs/TASK-xxx.log.md` 작성 또는 갱신
- 관련 없는 변경사항 없음
- forbidden files 수정 없음

커밋 메시지는 TASK의 commit rule을 따른다.

기본 형식은 다음과 같다.

```text
TASK-XXX WBS-XX-XXX: short summary
```

## 9. 완료 조건

TASK는 다음 조건을 모두 만족해야 완료로 본다.

- `AGENTS.md`를 확인했다.
- `.agents/rules/**`를 확인했다.
- 지정된 `ops/tasks/TASK-xxx.md`를 기준으로 작업했다.
- 현재 git branch가 TASK의 Branch와 일치했다.
- allowed files 안에서만 수정했다.
- forbidden files를 수정하지 않았다.
- acceptance criteria를 충족했다.
- verification commands를 실행했다.
- 검증 결과가 PASS다.
- 리뷰 verdict가 PASS 또는 PASS_WITH_NOTES다. (Normal TASK)
- `ops/logs/TASK-xxx.log.md`를 작성 또는 갱신했다.
- 관련 없는 변경사항이 없다.
- 필요한 경우 최종 커밋을 생성했다.
- 커밋 메시지에 TASK ID가 포함되어 있다.
- 가능하면 커밋 메시지에 WBS ID가 포함되어 있다.

## 10. 최종 보고 형식

최종 응답에는 다음을 포함한다.

```text
TASK ID:
WBS ID:
Domain:
Branch:
Status:
Changed files:
Verification:
Review verdict:
Evaluation verdict: (EVAL TASK만)
User validation status: (EVAL TASK만)
Execution log:
Commit message:
Commit hash:
Remaining risks:
Follow-up:
```

## 11. 실패 또는 중단 시 보고 형식

작업을 완료할 수 없으면 다음 형식으로 보고한다.

```text
TASK ID:
Status: BLOCKED 또는 FAIL
Reason:
Completed work:
Changed files:
Failed verification:
Blocking issue:
Recommended next action:
```