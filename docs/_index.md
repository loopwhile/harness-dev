# docs/_index.md

## 목적 (Purpose)
이 파일은 **문서 라우팅 맵(Document Routing Map)**입니다.
현재 작업에 필요한 내용만 선택적으로 읽으십시오.

## 핵심 경로 (Core Paths)
- 아키텍처 (Architecture): `docs/04_architecture/system_architecture.md`
- 상태 (Status): `docs/08_ops/status/status_report.md`
- WBS 인덱스 (WBS Index): `docs/09_pm/wbs/wbs_00_index.md`
- 활성 WBS (Active WBS): `docs/09_pm/wbs/`
- 제품 (Product): `docs/02_product/prd.md`
- 요구사항 (Requirements): `docs/03_requirements/functional_requirements.md`
- API 계약 (API Contract): `docs/05_contracts/api/api_contract.md`
- ERD: `docs/05_contracts/data/erd.md`
- 부트스트랩 (Bootstrap): `docs/00_governance/project_bootstrap_guide.md`
- 통제 매트릭스 (Control Matrix): `docs/00_governance/agent_control_matrix.md`
- 스킬 (Skills): `.agents/skills/*/SKILL.md`
- 명령 규칙 (Rules): `.codex/rules/harness.rules`
- 훅 (Hooks): `.codex/hooks.json`, `.codex/hooks/*.py`

## 라우팅 가이드 (Routing Guide)
- **구현 시 (For implementation):**
  - 활성(Active) WBS
  - 관련 요구사항 섹션
  - 관련 계약(Contract) 섹션
  - 대상 파일들 (src/)
  - 역할 계약서 (`agent_roles/`)
  - 관련 페르소나 계약서 (`agent_personas/`)

- **검증 시 (For verification):**
  - 현재 작업 패킷 (Current task packet)
  - 변경된 파일들
  - 증거 패킷 (Evidence packet)

- **재시작 시 (For restart):**
  - 상태 보고서 (Status report)
  - WBS 인덱스
  - 활성(Active) WBS
  - 현재 작업 패킷 (`ops/packets/`)
  - 부트스트랩 가이드 (초기화 단계인 경우)

## 읽기 정책 (Reading Policy)
- 기본적으로 문서 전체를 읽지 마십시오.
- 관련이 있는 섹션만 읽으십시오.
- 전체 문서 로딩보다 **섹션 단위의 참조(Section references)**를 우선하십시오.
