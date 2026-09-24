# harness-dev

AI 하네스 엔지니어링을 위한 프로젝트 템플릿. **기획·설계·디자인 문서를 완성한 뒤, WBS에서 정의한 TASK를 단위별로 구현·검증·기록**한다.

실행 정책은 [AGENTS.md](AGENTS.md), 단계별 사용 프롬프트는 [HARNESS-DEV.md](HARNESS-DEV.md)를 참고한다.

## 1. 전체 스킬 워크플로우

```mermaid
flowchart TD
    S["서비스 아이디어 / 요구사항"] --> P["기획<br/>프로젝트 개요 · 제품 정의"]
    P --> R["요구사항·화면 설계<br/>기능명세 · 사용자 흐름 · 화면정의"]
    R --> D["UI/UX 디자인<br/>디자인 시스템 · 필요 시 Stitch · UI handoff"]
    D --> A["시스템 설계<br/>아키텍처 · 구성도 · 시퀀스"]
    A --> C["계약 설계<br/>API · DB · 상태 · 에러"]
    C --> W["개발 계획<br/>WBS · TASK · EVAL TASK"]
    W --> G{"명세 검수 및<br/>개발 착수 승인"}
    G -- "보강 필요" --> R
    G -- "승인" --> T["개발<br/>TASK 단위 구현 · 검증 · 리뷰 · 기록 · 커밋"]
    T --> E["기능/도메인 완료 시 EVAL TASK<br/>통합 검증 · 평가 · 사용자 검증"]
    E --> U{"사용자 검증 승인"}
    U -- "수정 요청" --> T
    U -- "APPROVED" --> N{"다음 기능/도메인이 있는가?"}
    N -- "예" --> T
    N -- "아니오" --> F["개발 범위 완료"]
```

- **Mode 1 — General / Analysis:** 저장소 분석·문서 점검·계획 검토. TASK 파일 없이 수행할 수 있다.
- **Mode 2 — Planning / Specification:** 아래 0~12단계의 문서를 작성·검수한다. **소스 코드는 구현하지 않는다.**
- **Mode 3 — TASK Execution:** 사용자가 `execute-task`(Codex) 또는 `antigravity-execute-task`(Antigravity)로 지정한 `ops/tasks/TASK-xxx.md` 하나를 실행한다. 브랜치와 허용/금지 파일을 먼저 확인한다.

## 2. Mode 2 — 기획 → 설계 → 디자인 → 개발 준비

다음 다이어그램의 번호는 [HARNESS-DEV.md의 Mode 2 문서 완성 순서](HARNESS-DEV.md#3-mode-2-문서-완성-순서)와 일치한다. 상자의 영문 이름은 실제 `.agents/skills/<스킬명>/SKILL.md` 경로에 대응한다.

```mermaid
flowchart TD
    A0["0. 프로젝트 개요<br/>write-project-overview<br/>project_overview.md"]
    A1["1. 제품 기획<br/>plan-commercial-v1<br/>product_brief · PRD · scope · business_rules"]
    A2["2. 기능명세<br/>write-functional-spec<br/>도메인별 기능 · 인수 기준"]
    A3["3. 화면 설계<br/>write-screen-definition<br/>사용자 흐름 · 화면정의"]
    A4["4. UI/UX 디자인 기준<br/>write-design-system-doc<br/>전역/프론트엔드별 DESIGN.md"]
    Q{"Stitch를 사용하는가?"}
    A5["5. Stitch 프롬프트<br/>prepare-stitch-prompt"]
    ST["Stitch에서 화면 생성 및 결과 확인<br/>외부 디자인 작업"]
    A6["6. 디자인 결과 반영<br/>ingest-stitch-output<br/>결과 정리 · UI handoff"]
    ALT["Stitch 없이 진행<br/>필요한 UI handoff 별도 정리"]
    A7["7. 시스템 아키텍처<br/>write-system-architecture<br/>시스템 · 모듈 경계 · 런타임"]
    A8["8. 아키텍처 시각화<br/>write-architecture-diagrams<br/>시스템 · 컨테이너 · 배포 다이어그램"]
    A9["9. 도메인 시퀀스<br/>write-sequence-diagrams<br/>주요 요청 · 상태 전이 흐름"]
    A10["10. 데이터/API 계약<br/>write-data-api-contracts<br/>API · ERD · 테이블 · 상태 · 에러"]
    A11["11. WBS/TASK 분해<br/>create-wbs-from-spec<br/>Domain → Feature → TASK → EVAL TASK"]
    A12["12. 개발 착수 검수<br/>review-spec-completeness<br/>명세 갭 · 개발 준비 보고서"]
    G{"검수 결과 및 제품 오너 승인"}
    FIX["누락된 명세·디자인·계약 보강"]
    DONE["Mode 3: 해당 TASK 실행"]

    A0 --> A1 --> A2 --> A3 --> A4 --> Q
    Q -- "사용" --> A5 --> ST --> A6 --> A7
    Q -- "미사용" --> ALT --> A7
    A7 --> A8 --> A9 --> A10 --> A11 --> A12 --> G
    G -- "NEEDS_SPEC / BLOCKED 등" --> FIX --> A12
    G -- "PASS 또는 승인된 CONDITIONAL_PASS" --> DONE
```

**Stitch는 선택 경로**다. `prepare-stitch-prompt`는 프롬프트를 작성하며 Stitch 자체를 실행하지 않는다. Stitch 결과를 사용한 경우 `ingest-stitch-output`으로 화면정의·디자인 기준과 대조한 뒤 UI handoff를 정리한다. Stitch를 생략하더라도 프론트엔드 구현에 필요한 화면정의·DESIGN.md·UI handoff는 개발 착수 전에 준비한다.

**명세 검수는 구현 실행이 아니다.** `review-spec-completeness`는 누락 사항과 착수 가능 여부를 보고한다. 보강이 필요한 경우 관련 Mode 2 단계로 돌아가 문서를 수정한 후 재검수한다.

## 3. Mode 3 — TASK별 반복 개발 및 EVAL

```mermaid
flowchart TD
    START["execute-task / antigravity-execute-task<br/>TASK-xxx.md 지정"]
    PRE["orchestrator<br/>TASK 계약 · 브랜치 · 작업 트리 점검"]
    TYPE{"TASK Type"}
    IMP["implementer<br/>허용된 범위 내 구현 및 테스트 작성"]
    VER["verifier<br/>검증 명령 · 인수 기준 확인"]
    VOK{"검증 PASS?"}
    REV["reviewer<br/>diff · 범위 · 위험 검토"]
    ROK{"리뷰 PASS 또는 PASS_WITH_NOTES?"}
    REC["recorder<br/>ops/logs/TASK-xxx.log.md"]
    COM["orchestrator<br/>최종 확인 · 커밋 · 사용자 보고"]
    EVAL["evaluator<br/>기능/도메인 평가 · 사용자 검증 안내"]
    EOK{"평가 PASS 또는 CONDITIONAL_PASS?"}
    EREC["recorder<br/>평가 기록 · 사용자 검증 PENDING"]
    ECOM["orchestrator<br/>EVAL 커밋 · 검증 안내 · STOP"]
    APPROVE{"사용자 검증"}
    NEXT["APPROVED<br/>다음 기능/도메인 진행"]
    CORRECT["수정 가능 시 implementer부터 재실행<br/>반복 한도 준수"]
    STOP["FAIL / BLOCKED<br/>원인 보고 · 커밋하지 않음"]
    CHANGE["수정 요청<br/>correction TASK / 재검증"]

    START --> PRE --> TYPE
    TYPE -- "일반 TASK" --> IMP --> VER --> VOK
    VOK -- "예" --> REV --> ROK
    VOK -- "아니오: 수정 가능" --> CORRECT --> IMP
    VOK -- "BLOCKED / 수정 불가" --> STOP
    ROK -- "예" --> REC --> COM
    ROK -- "아니오: 수정 가능" --> CORRECT
    ROK -- "BLOCKED / 수정 불가" --> STOP
    TYPE -- "eval" --> EVER["verifier<br/>선행 TASK 기반 통합 검증"] --> EVOK{"통합 검증 PASS?"}
    EVOK -- "예" --> EVAL --> EOK
    EVOK -- "아니오" --> STOP
    EOK -- "예" --> EREC --> ECOM --> APPROVE
    EOK -- "아니오" --> STOP
    APPROVE -- "APPROVED" --> NEXT
    APPROVE -- "REQUEST_CHANGES / REJECTED" --> CHANGE
    CHANGE --> START
    APPROVE -- "DEFERRED" --> HOLD["보류 · 후속 결정 대기"]
```

일반 TASK의 고정 순서는 **orchestrator → implementer → verifier → reviewer → recorder → commit**이다. EVAL TASK는 구현을 하지 않고 **orchestrator → verifier → evaluator → recorder → commit → 사용자 검증 안내 → STOP** 순서로 수행한다. 사용자 `APPROVED` 전에는 다음 기능 그룹으로 넘어가지 않는다. 실패·차단된 TASK는 커밋하지 않는다.

각 스킬의 상세 입력·출력 및 실행 프롬프트는 [HARNESS-DEV.md](HARNESS-DEV.md), TASK 경계·승인·평가 규칙은 [AGENTS.md](AGENTS.md)를 따른다.
