# docs/_index.md

## 목적 (Purpose)
이 파일은 **문서 라우팅 맵(Document Routing Map)**입니다.
현재 작업에 필요한 내용만 선택적으로 읽으십시오.

## 핵심 경로 (Core Paths)

### 프로젝트 헌법 및 에이전트 설정
- 프로젝트 헌법: `AGENTS.md`
- 에이전트 스킬: `.agents/skills/*/SKILL.md`
- 에이전트 규칙: `.agents/rules/*.md`
- 에이전트 정의 (Antigravity): `.agents/agents/*/agent.md`
- 에이전트 정의 (Codex): `.codex/agents/*.toml`
- 기획/설계 템플릿: `.agents/templates/*.template.md`
- 훅 (Antigravity): `.agents/hooks.json`, `.agents/hooks/*.py`
- 훅 (Codex): `.codex/hooks.json`, `.codex/hooks/*.py`

### 프로젝트 개요 (Overview)
- 프로젝트 개요: `docs/01_overview/project_overview.md`

### 제품/요구사항 (Product / Requirements)
- 제품 정의: `docs/02_product/product_brief.md`, `docs/02_product/prd.md`
- 범위/정책: `docs/02_product/scope.md`, `docs/02_product/business_rules.md`
- 기능명세: `docs/03_requirements/functional_spec/`
- 사용자 흐름: `docs/03_requirements/user_flows.md`
- 화면정의: `docs/03_requirements/screen_definition/`
- 인수 기준: `docs/03_requirements/acceptance_criteria.md`

### 아키텍처 (Architecture)
- 시스템 아키텍처: `docs/04_architecture/system_architecture.md`
- 아키텍처 다이어그램: `docs/04_architecture/architecture_diagrams.md`
- 모듈 경계: `docs/04_architecture/module_boundaries.md`
- 런타임 흐름: `docs/04_architecture/runtime_flow.md`
- 시퀀스 다이어그램: `docs/04_architecture/sequence_diagrams.md`

### 계약 (Contracts)
- API 계약: `docs/05_contracts/api/api_contract.md`
- ERD: `docs/05_contracts/data/erd.md`
- 테이블 명세: `docs/05_contracts/data/table_spec.md`
- 상태 모델: `docs/05_contracts/state_model.md`
- 에러 명세: `docs/05_contracts/error_spec.md`

### 디자인 (Design)
- 전역 디자인 기준: `docs/06_design/DESIGN.md`
- 프론트엔드별 디자인 기준: `docs/06_design/frontends/<frontend>/DESIGN.md`
- 디자인 방향: `docs/06_design/design_direction.md`
- Stitch 프롬프트: `docs/06_design/stitch/prompts/`
- Stitch 결과 정리: `docs/06_design/stitch/results/`
- UI handoff: `docs/06_design/ui_handoff/`

### PM / WBS
- WBS 인덱스: `docs/09_pm/wbs/wbs_00_index.md`
- 활성 WBS: `docs/09_pm/wbs/`
- 명세 갭 보고서: `docs/09_pm/spec_gap_report.md`
- 개발 착수 가능성 보고서: `docs/09_pm/release_readiness_for_development.md`

### 운영
- TASK 파일: `ops/tasks/TASK-xxx.md`
- TASK 로그: `ops/logs/TASK-xxx.log.md`
- TASK 템플릿: `ops/templates/`

## 라우팅 가이드 (Routing Guide)

### 기획/설계/명세 시 (For planning/specification — Mode 2)
- 프로젝트 개요: `docs/01_overview/project_overview.md`
- 제품 정의: `docs/02_product/`
- 기능명세: `docs/03_requirements/functional_spec/`
- 사용자 흐름: `docs/03_requirements/user_flows.md`
- 화면정의: `docs/03_requirements/screen_definition/`
- 전역 디자인 기준: `docs/06_design/DESIGN.md`
- 프론트엔드별 디자인: `docs/06_design/frontends/`
- 디자인 방향: `docs/06_design/design_direction.md`
- Stitch 프롬프트: `docs/06_design/stitch/prompts/`
- Stitch 결과: `docs/06_design/stitch/results/`
- UI handoff: `docs/06_design/ui_handoff/`
- 아키텍처/다이어그램: `docs/04_architecture/`
- 시퀀스 다이어그램: `docs/04_architecture/sequence_diagrams.md`
- API/DB/상태/에러 계약: `docs/05_contracts/`
- WBS/TASK: `docs/09_pm/wbs/`, `ops/tasks/`

### 구현 시 (For implementation — Mode 3)
- TASK 파일 (`ops/tasks/TASK-xxx.md`)
- 활성(Active) WBS
- 관련 기능명세 섹션
- 관련 화면정의 섹션
- 관련 DESIGN.md
- 관련 UI handoff
- 관련 계약(Contract) 섹션
- 관련 시퀀스 다이어그램
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
