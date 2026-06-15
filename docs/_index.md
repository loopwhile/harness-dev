# docs/_index.md

## 목적 (Purpose)
이 파일은 **문서 라우팅 맵(Document Routing Map)**입니다.
현재 작업에 필요한 내용만 선택적으로 읽으십시오.

## 핵심 경로 (Core Paths)

### 프로젝트 헌법 및 에이전트 설정
- 프로젝트 헌법: `AGENTS.md`
- 에이전트 스킬: `.agents/skills/*/SKILL.md`
- 에이전트 규칙: `.agents/rules/*.md`
- 에이전트 정의 (Antigravity): `.agents/agents/*/agent.json`
- 에이전트 정의 (Codex): `.codex/agents/*.toml`
- 훅 (Antigravity): `.agents/hooks.json`, `.agents/hooks/*.py`
- 훅 (Codex): `.codex/hooks.json`, `.codex/hooks/*.py`

### 상위 문서
- 아키텍처 (Architecture): `docs/04_architecture/system_architecture.md`
- 제품 (Product): `docs/02_product/prd.md`
- 요구사항 (Requirements): `docs/03_requirements/functional_requirements.md`
- API 계약 (API Contract): `docs/05_contracts/api/api_contract.md`
- ERD: `docs/05_contracts/data/erd.md`

### PM / WBS
- WBS 인덱스 (WBS Index): `docs/09_pm/wbs/wbs_00_index.md`
- 활성 WBS (Active WBS): `docs/09_pm/wbs/`

### 운영
- TASK 파일: `ops/tasks/TASK-xxx.md`
- TASK 로그: `ops/logs/TASK-xxx.log.md`
- 템플릿: `ops/templates/`

## 라우팅 가이드 (Routing Guide)

### 구현 시 (For implementation)
- TASK 파일 (`ops/tasks/TASK-xxx.md`)
- 활성(Active) WBS
- 관련 요구사항 섹션
- 관련 계약(Contract) 섹션
- 대상 파일들 (src/)

### 검증 시 (For verification)
- TASK 파일의 acceptance criteria 및 verification commands
- 변경된 파일들
- TASK 로그 (`ops/logs/TASK-xxx.log.md`)

### 재시작 시 (For restart)
- WBS 인덱스의 Domain Branch Status
- 활성(Active) WBS
- 현재 TASK 파일
- AGENTS.md

## 읽기 정책 (Reading Policy)
- 기본적으로 문서 전체를 읽지 마십시오.
- 관련이 있는 섹션만 읽으십시오.
- 전체 문서 로딩보다 **섹션 단위의 참조(Section references)**를 우선하십시오.
