# HARNESS-DEV.md

## 1. 이 문서의 목적

이 문서는 `harness-dev` 템플릿을 실제 프로젝트에서 사용하는 방법을 설명한다.

핵심은 간단하다.

```text
Mode 2 = 기획/설계/명세 문서 완성 단계
Mode 3 = TASK 단위 개발/검증/커밋 단계
```

사용자는 제품 오너다.  
AI는 기획자, 설계자, UX 명세자, 아키텍트, 계약 설계자, 개발자, QA 역할을 나누어 수행한다.

---

## 2. 전체 사용 흐름

```text
1. Mode 2에서 기획/설계/명세 문서를 완성한다.
2. 필요한 경우 Stitch로 화면을 생성하고 결과를 문서에 반영한다.
3. API/DB/상태/에러 계약을 완성한다.
4. WBS/TASK를 생성한다.
5. spec-reviewer로 개발 착수 가능 여부를 검토한다.
6. 사용자가 승인한다.
7. Mode 3에서 TASK 단위로 개발한다.
```

---

## 3. Mode 2 문서 완성 순서

Mode 2에서는 소스 코드를 구현하지 않는다.  
기획/설계/명세 문서만 작성한다.

| 순서 | 사용할 스킬 | 완성 문서 |
|---|---|---|
| 0 | `write-project-overview` | `docs/01_overview/project_overview.md` |
| 1 | `plan-commercial-v1` | `docs/02_product/product_brief.md`, `prd.md`, `scope.md`, `business_rules.md` |
| 2 | `write-functional-spec` | `docs/03_requirements/functional_spec/_index.md`, `functional_spec/<domain>.md`, `acceptance_criteria.md` |
| 3 | `write-screen-definition` | `docs/03_requirements/screen_definition/_index.md`, `screen_definition/<domain>.md`, `user_flows.md` |
| 4 | `write-design-system-doc` | `docs/06_design/DESIGN.md`, `docs/06_design/frontends/<frontend>/DESIGN.md`, `docs/06_design/design_direction.md` 선택 |
| 5 | `prepare-stitch-prompt` | `docs/06_design/stitch/prompts/<domain>.md` |
| 6 | `ingest-stitch-output` | `docs/06_design/stitch/results/<domain>.md`, `docs/06_design/ui_handoff/<domain>.md` |
| 7 | `write-system-architecture` | `docs/04_architecture/system_architecture.md`, `module_boundaries.md`, `runtime_flow.md` |
| 8 | `write-architecture-diagrams` | `docs/04_architecture/architecture_diagrams.md` |
| 9 | `write-sequence-diagrams` | `docs/04_architecture/sequence_diagrams.md` |
| 10 | `write-data-api-contracts` | `docs/05_contracts/api/api_contract.md`, `docs/05_contracts/data/erd.md`, `table_spec.md`, `state_model.md`, `error_spec.md` |
| 11 | `create-wbs-from-spec` | `docs/09_pm/wbs/`, `ops/tasks/` |
| 12 | `review-spec-completeness` | `docs/09_pm/spec_gap_report.md`, `docs/09_pm/release_readiness_for_development.md` |

---

## 4. Mode 2 단계별 사용 프롬프트

아래 프롬프트를 순서대로 사용한다.

---

### 4.0 프로젝트 개요 작성

사용 스킬:

```text
write-project-overview
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-project-overview/SKILL.md를 사용해서
프로젝트 개요 문서를 작성해줘.

출력 문서:
- docs/01_overview/project_overview.md

기준:
- 제품 상세 PRD로 들어가기 전의 상위 개요만 작성할 것
- 프로젝트 목적, 문제 정의, 핵심 사용자, 핵심 가치, 현재 상태를 정리할 것
- 기술 스택은 확정/후보 상태를 구분할 것
- 이후 plan-commercial-v1이 참고할 수 있게 작성할 것

서비스 아이디어:
[여기에 서비스 설명 작성]
```

---

### 4.1 제품 정의 작성

사용 스킬:

```text
plan-commercial-v1
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/plan-commercial-v1/SKILL.md를 사용해서
[서비스명]의 제품 정의 문서를 작성해줘.

다음 문서를 완성해줘.

- docs/02_product/product_brief.md
- docs/02_product/prd.md
- docs/02_product/scope.md
- docs/02_product/business_rules.md

기준:
- MVP로 핵심 기능을 과도하게 줄이지 말 것
- Enterprise 문서처럼 과설계하지 말 것
- Lean Commercial v1 기준으로 작성할 것
- 내가 제품 오너이므로 필요한 결정사항은 별도로 정리할 것
- docs/01_overview/project_overview.md가 있으면 참고할 것

서비스 아이디어:
[여기에 서비스 설명 작성]
```

---

### 4.2 기능명세 작성

사용 스킬:

```text
write-functional-spec
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-functional-spec/SKILL.md를 사용해서
[도메인명] 도메인의 기능명세서를 작성해줘.

입력 문서:
- docs/02_product/product_brief.md
- docs/02_product/prd.md
- docs/02_product/scope.md
- docs/02_product/business_rules.md

출력 문서:
- docs/03_requirements/functional_spec/_index.md
- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/acceptance_criteria.md

각 기능에는 반드시 다음을 포함해줘.

- 기능 ID
- 기능명
- 사용자 유형
- 선행 조건
- 입력값
- 처리 절차
- 성공 결과
- 실패/예외
- 상태 변화
- 관련 화면 ID
- 관련 API ID
- 관련 테이블
- 테스트 기준

"회원 기능", "결제 기능"처럼 큰 덩어리로 끝내지 말고,
실제 개발 가능한 하위 기능까지 분해해줘.

대상 도메인:
[도메인명]
```

---

### 4.3 화면정의 작성

사용 스킬:

```text
write-screen-definition
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-screen-definition/SKILL.md를 사용해서
[도메인명] 도메인의 화면정의서를 작성해줘.

입력 문서:
- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/user_flows.md

출력 문서:
- docs/03_requirements/screen_definition/_index.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/03_requirements/user_flows.md

각 화면에는 반드시 다음을 포함해줘.

- 화면 ID
- URL/path
- Frontend ID
- Design Reference
- 접근 권한
- 화면 목적
- 표시 컴포넌트
- 입력 필드
- 버튼/액션
- 기본 상태
- 로딩 상태
- 빈 상태
- 에러 상태
- 권한 없음 상태
- 성공 상태
- 관련 기능 ID
- 관련 API ID

대상 도메인:
[도메인명]

프론트엔드:
[customer-web/admin-web/owner-web 등]
```

---

### 4.4 DESIGN.md 작성

사용 스킬:

```text
write-design-system-doc
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-design-system-doc/SKILL.md를 사용해서
프론트엔드 UI/UX 기준 문서 DESIGN.md를 작성해줘.

입력 문서:
- docs/02_product/product_brief.md
- docs/03_requirements/screen_definition/
- docs/06_design/ui_handoff/ 있으면 참고
- docs/06_design/stitch/results/ 있으면 참고

출력 문서:
- docs/06_design/DESIGN.md
- docs/06_design/frontends/<frontend>/DESIGN.md
- docs/06_design/design_direction.md (디자인 선호/방향성이 필요한 경우)

포함 항목:
- Design Principles
- Brand Tone
- Layout Principles
- Navigation Rules
- Responsive Rules
- Color / Typography / Spacing
- Component Guidelines
- Form / Validation UX
- Error / Empty / Loading States
- Accessibility Rules
- Screen Pattern Rules
- Stitch Extraction Notes
- Frontend Implementation Notes

프론트엔드 목록:
[customer-web, admin-web 등]
```

---

### 4.5 Stitch 프롬프트 작성

사용 스킬:

```text
prepare-stitch-prompt
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/prepare-stitch-prompt/SKILL.md를 사용해서
[도메인명] 도메인의 Stitch Prompt Pack을 작성해줘.

입력 문서:
- docs/02_product/product_brief.md
- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/03_requirements/user_flows.md
- docs/06_design/DESIGN.md
- docs/06_design/frontends/<frontend>/DESIGN.md

출력 문서:
- docs/06_design/stitch/prompts/<domain>.md

조건:
- 화면별로 Stitch 프롬프트를 작성할 것
- DESIGN.md의 톤, 레이아웃, 컴포넌트 기준을 반영할 것
- Stitch를 직접 실행하지 말고 프롬프트만 작성할 것

대상 도메인:
[도메인명]

프론트엔드:
[frontend명]
```

---

### 4.6 Stitch 결과 반영

사용자가 Stitch에서 화면을 생성한 뒤, 결과를 AI에게 전달한다.

사용 스킬:

```text
ingest-stitch-output
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/ingest-stitch-output/SKILL.md를 사용해서
내가 전달한 Stitch 결과를 정리해줘.

입력:
- Stitch 스크린샷 또는 export 코드
- 사용자 승인/수정 코멘트
- 기존 screen_definition
- 기존 DESIGN.md
- 기존 Stitch Prompt Pack

출력 문서:
- docs/06_design/stitch/results/<domain>.md
- docs/06_design/ui_handoff/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md 보정 제안
- docs/06_design/DESIGN.md 보정 제안

조건:
- Stitch 결과 코드를 프로덕션 코드로 바로 채택하지 말 것
- 화면 구조, 컴포넌트, 상태, 레이아웃 기준만 추출할 것
- API/DB/상태/에러에 영향이 있으면 별도로 표시할 것

대상 도메인:
[도메인명]

Stitch 결과:
[여기에 붙여넣기]
```

---

### 4.7 시스템 아키텍처 작성

사용 스킬:

```text
write-system-architecture
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-system-architecture/SKILL.md를 사용해서
시스템 아키텍처, 모듈 경계, 런타임 흐름 문서를 작성해줘.

입력 문서:
- docs/01_overview/project_overview.md
- docs/02_product/product_brief.md
- docs/02_product/prd.md
- docs/03_requirements/functional_spec/
- docs/03_requirements/screen_definition/
- docs/03_requirements/user_flows.md
- docs/06_design/DESIGN.md 있으면 참고

출력 문서:
- docs/04_architecture/system_architecture.md
- docs/04_architecture/module_boundaries.md
- docs/04_architecture/runtime_flow.md

포함 항목:
- 기술 스택
- 시스템 구성도
- 배포 구조
- 외부 연동
- 보안 기준
- 모듈 목록과 의존
- 요청 처리 흐름
- 인증/인가 흐름
- 에러 처리 흐름
```

---

### 4.8 아키텍처 다이어그램 작성

사용 스킬:

```text
write-architecture-diagrams
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-architecture-diagrams/SKILL.md를 사용해서
아키텍처 다이어그램을 작성해줘.

입력 문서:
- docs/04_architecture/system_architecture.md
- docs/04_architecture/module_boundaries.md
- docs/04_architecture/runtime_flow.md
- docs/03_requirements/functional_spec/
- docs/03_requirements/screen_definition/

출력 문서:
- docs/04_architecture/architecture_diagrams.md

필수 다이어그램:
- System Context Diagram
- Container Diagram
- Module Boundary Diagram
- Deployment Diagram

필요하면 추가:
- Data Flow Diagram
- Security Boundary Diagram
- Frontend App Architecture Diagram
- Event / Async Flow Diagram
```

---

### 4.9 시퀀스 다이어그램 작성

사용 스킬:

```text
write-sequence-diagrams
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-sequence-diagrams/SKILL.md를 사용해서
도메인별 시퀀스 다이어그램을 작성해줘.

입력 문서:
- docs/03_requirements/functional_spec/
- docs/03_requirements/screen_definition/
- docs/03_requirements/user_flows.md
- docs/04_architecture/system_architecture.md
- docs/04_architecture/module_boundaries.md
- docs/04_architecture/architecture_diagrams.md
- docs/05_contracts/api/api_contract.md 있으면 참고

출력 문서:
- docs/04_architecture/sequence_diagrams.md

시퀀스는 대표 하나만 만들지 말고,
도메인별 핵심 흐름을 SEQ ID 기준으로 작성해줘.

SEQ ID 형식:
SEQ-{DOMAIN}-{SEQ}
```

---

### 4.10 API/DB/상태/에러 계약 작성

사용 스킬:

```text
write-data-api-contracts
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/write-data-api-contracts/SKILL.md를 사용해서
API/DB/상태/에러 계약 문서를 작성해줘.

입력 문서:
- docs/03_requirements/functional_spec/
- docs/03_requirements/screen_definition/
- docs/06_design/ui_handoff/
- docs/04_architecture/system_architecture.md
- docs/04_architecture/sequence_diagrams.md

출력 문서:
- docs/05_contracts/api/api_contract.md
- docs/05_contracts/data/erd.md
- docs/05_contracts/data/table_spec.md
- docs/05_contracts/state_model.md
- docs/05_contracts/error_spec.md

다음 연결을 반드시 유지해줘.

기능 ID
→ 화면 ID
→ SEQ ID
→ API ID
→ 테이블
→ 상태
→ 에러 코드
→ 테스트 기준

도메인별 시퀀스 없이 API 계약을 완료 처리하지 마.
```

---

### 4.11 WBS/TASK 생성

사용 스킬:

```text
create-wbs-from-spec
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/create-wbs-from-spec/SKILL.md를 사용해서
완성된 명세 문서를 기반으로 WBS와 TASK를 생성해줘.

입력 문서:
- docs/01_overview/project_overview.md
- docs/03_requirements/functional_spec/
- docs/03_requirements/screen_definition/
- docs/05_contracts/api/api_contract.md
- docs/05_contracts/data/erd.md
- docs/06_design/DESIGN.md
- docs/06_design/frontends/
- docs/06_design/ui_handoff/
- docs/04_architecture/system_architecture.md
- docs/04_architecture/architecture_diagrams.md
- docs/04_architecture/sequence_diagrams.md

출력:
- docs/09_pm/wbs/wbs_XX_<domain>.md
- docs/09_pm/wbs/wbs_00_index.md 갱신
- ops/tasks/TASK-XXX.md

조건:
- WBS 파일은 도메인 단위로 작성
- Feature는 사용자 관점 기능
- TASK는 실제 구현 가능한 작업 단위
- 각 Feature 마지막에 EVAL TASK 배치
- 각 Domain 마지막에 통합 EVAL TASK 배치

"회원가입", "로그인" 같은 큰 덩어리를 TASK로 만들지 말고,
기능명세/화면정의/API/DB/백엔드/프론트엔드/테스트/EVAL 단위로 분해해줘.
```

---

### 4.12 개발 착수 가능성 검토

사용 스킬:

```text
review-spec-completeness
```

프롬프트:

```text
Mode 2. Planning / Specification Mode로 진행한다.

.agents/skills/review-spec-completeness/SKILL.md를 사용해서
현재 프로젝트가 개발 착수 가능한 상태인지 검토해줘.

검토 대상:
- 프로젝트 개요
- 제품 정의
- 기능명세
- 화면정의
- DESIGN.md
- 프론트엔드별 DESIGN.md
- Stitch 결과
- UI handoff
- 시스템 아키텍처
- 모듈 경계
- 런타임 흐름
- 아키텍처 다이어그램
- 도메인별 시퀀스 다이어그램
- API 계약
- ERD
- 테이블 명세
- 상태 모델
- 에러 명세
- WBS
- TASK
- EVAL TASK

판정값:
- PASS
- CONDITIONAL_PASS
- NEEDS_SPEC
- BLOCKED

보고서 초안을 작성해줘.

보고 대상:
- docs/09_pm/spec_gap_report.md
- docs/09_pm/release_readiness_for_development.md

spec-reviewer는 read-only 검수자이므로,
파일 기록이 필요하면 메인 에이전트가 기록해줘.
```

---

## 5. 개발 단계로 넘어가는 기준

Mode 3 개발 단계로 넘어가기 전에 최소한 아래 문서가 있어야 한다.

```text
- 프로젝트 개요
- 기능명세
- 화면정의
- DESIGN.md
- 프론트엔드별 DESIGN.md
- UI handoff
- 시스템 아키텍처
- 모듈 경계
- 런타임 흐름
- 아키텍처 다이어그램
- 도메인별 시퀀스 다이어그램
- API 계약
- ERD / 테이블 명세
- 상태 모델
- 에러 명세
- WBS
- TASK
- EVAL TASK
```

`review-spec-completeness` 결과가 `PASS` 또는 사용자가 승인한 `CONDITIONAL_PASS`이면 개발 단계로 넘어간다.

---

## 6. 개발 단계: Antigravity 사용 시

Antigravity에서는 TASK 실행 시 다음 스킬을 사용한다.

```text
antigravity-execute-task
```

프롬프트:

```text
Mode 3. TASK Execution Mode로 진행한다.

.agents/skills/antigravity-execute-task/SKILL.md를 사용해서
아래 TASK를 실행해줘.

TASK 파일:
ops/tasks/TASK-XXX.md

규칙:
- 현재 브랜치가 TASK의 Branch와 일치하는지 먼저 확인할 것
- allowed files 안에서만 작업할 것
- forbidden files는 수정하지 말 것
- 필요한 구현/테스트/검증을 수행할 것
- TASK 로그를 작성할 것
- 검증이 끝나면 커밋할 것
- 완료 후 사용자에게 요약 보고할 것
```

EVAL TASK도 동일하게 실행한다.

```text
Mode 3. TASK Execution Mode로 진행한다.

.agents/skills/antigravity-execute-task/SKILL.md를 사용해서
아래 EVAL TASK를 실행해줘.

TASK 파일:
ops/tasks/TASK-XXX.md

Type이 eval이면 implementer를 사용하지 말고,
verifier → evaluator → recorder → commit → user validation guide 순서로 진행해줘.
```

---

## 7. 개발 단계: Codex CLI 사용 시

Codex CLI에서는 TASK 실행 시 다음 스킬을 사용한다.

```text
execute-task
```

프롬프트:

```text
Mode 3. TASK Execution Mode로 진행한다.

.agents/skills/execute-task/SKILL.md를 사용해서
아래 TASK를 실행해줘.

TASK 파일:
ops/tasks/TASK-XXX.md

규칙:
- 현재 브랜치가 TASK의 Branch와 일치하는지 먼저 확인할 것
- allowed files 안에서만 작업할 것
- forbidden files는 수정하지 말 것
- 필요한 구현/테스트/검증을 수행할 것
- TASK 로그를 작성할 것
- 검증이 끝나면 커밋할 것
- 완료 후 사용자에게 요약 보고할 것
```

EVAL TASK도 동일하게 실행한다.

```text
Mode 3. TASK Execution Mode로 진행한다.

.agents/skills/execute-task/SKILL.md를 사용해서
아래 EVAL TASK를 실행해줘.

TASK 파일:
ops/tasks/TASK-XXX.md

Type이 eval이면 implementer를 사용하지 말고,
verifier → evaluator → recorder → commit → user validation guide 순서로 진행해줘.
```

---

## 8. 브랜치 운영

도메인별 브랜치에서 TASK를 진행한다.

예:

```text
main
└── dev
    ├── common
    ├── auth
    ├── reservation
    ├── payment
    ├── board
    └── notification
```

TASK 실행 전 반드시 현재 브랜치를 확인한다.

```bash
git branch --show-current
```

현재 브랜치와 TASK의 `Branch`가 다르면 작업하지 않는다.

```text
BLOCKED - TASK branch mismatch
```

---

## 9. TASK 실행 시 읽어야 하는 문서

TASK 파일의 Source Context를 기준으로 필요한 문서만 읽는다.

대표 문서:

```text
- docs/01_overview/project_overview.md
- docs/09_pm/wbs/wbs_XX_<domain>.md
- docs/03_requirements/functional_spec/<domain>.md
- docs/03_requirements/screen_definition/<domain>.md
- docs/06_design/DESIGN.md
- docs/06_design/frontends/<frontend>/DESIGN.md
- docs/06_design/ui_handoff/<domain>.md
- docs/04_architecture/system_architecture.md
- docs/04_architecture/module_boundaries.md
- docs/04_architecture/runtime_flow.md
- docs/04_architecture/architecture_diagrams.md
- docs/04_architecture/sequence_diagrams.md
- docs/05_contracts/api/api_contract.md
- docs/05_contracts/data/table_spec.md
- docs/05_contracts/state_model.md
- docs/05_contracts/error_spec.md
```

문서 전체를 무작정 읽지 말고, 현재 TASK와 관련된 섹션만 읽는다.

---

## 10. 금지사항

```text
- Mode 2에서 소스 코드를 구현하지 않는다.
- 기능명세 없이 WBS/TASK를 만들지 않는다.
- 화면정의 없이 프론트엔드 TASK를 만들지 않는다.
- DESIGN.md 없이 프론트엔드 구현 TASK를 만들지 않는다.
- UI handoff 없이 프론트엔드 구현 TASK를 만들지 않는다.
- 도메인별 시퀀스 없이 API 계약을 완료하지 않는다.
- 아키텍처 다이어그램 없이 아키텍처 문서를 완료하지 않는다.
- 텍스트 아키텍처 없이 아키텍처 다이어그램을 작성하지 않는다.
- API/DB 명세 없이 백엔드 TASK를 만들지 않는다.
- Stitch 결과 코드를 프로덕션 코드로 바로 사용하지 않는다.
- Mode 3에서 forbidden files를 수정하지 않는다.
```

---

## 11. 가장 짧은 사용 요약

기획/설계:

```text
write-project-overview
→ plan-commercial-v1
→ write-functional-spec
→ write-screen-definition
→ write-design-system-doc
→ prepare-stitch-prompt
→ ingest-stitch-output
→ write-system-architecture
→ write-architecture-diagrams
→ write-sequence-diagrams
→ write-data-api-contracts
→ create-wbs-from-spec
→ review-spec-completeness
```

개발:

```text
Antigravity:
antigravity-execute-task

Codex CLI:
execute-task
```