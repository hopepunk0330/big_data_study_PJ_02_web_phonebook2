# tech-architect 메모리

이 파일은 tech-architect의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **기술 아키텍처 결정사항 자체(현재 확정 상태)는 여기 없습니다 — `docs/planning/tech-architecture.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-14 — 신설
- design-prompter 패턴을 참고해 신설. 아직 실제 브리프 작업을 수행한 적 없음 — `docs/planning/tech-architecture.md`도 아직 생성 전(첫 실제 작업 때 이 역할이 만든다).

### 2026-07-14 — 비밀번호 찾기 API 2종(FR-14/FR-15) 계약 확정 + tech-architecture.md 최초 생성
- planning-pl 브리프: SCR-004(화면정의서 v1.3)를 01_구현요구사항서·03_기능정의서에 정식 반영. `tech-architecture.md`를 최초 생성(01/03 v1.0의 기존 관례를 canonical화 + 이번 판단 §4 추가).
- FR-14 `POST /auth/find-password`(아이디 확인, 로그인 불필요, 404/422), FR-15 `PATCH /auth/password`(재설정, 로그인 불필요, 404/422) — 사용자가 이미 번호 분리를 확정한 상태로 브리프만 구체화.
- 신규 설계 판단: 비밀번호 재설정 시 해당 user_id의 sessions 전체 DELETE(강제 재로그인) — service-concept.md §3 트레이드오프를 뒤집지 않되 피해 범위를 줄이는 보완책으로 채택.
- 03문서용 FN-014(get_user_by_username, 신규 공유 헬퍼)·FN-015(reset_password) 함수 스펙도 함께 브리프에 포함(PL이 이번 라운드 예외적으로 03문서까지 tech-architect에 라우팅).
- 01/03 md 파일 자체는 작성하지 않음(planning-writer 몫) — 브리프만 최종 메시지로 전달.

### 2026-07-15 — TRD static/ 물리적 위치 정정 브리프 (backend/ 중첩 → 프로젝트 루트 독립 폴더)
- planning-pl 브리프: TRD v1.0 §2/§3이 "같은 오리진 유지 → CORS 불필요"의 근거로 static/을 backend/ 아래 물리적 중첩시킨 전제 오류를 사용자가 확정 승인한 대로 정정.
- 핵심 판단: 오리진은 파일의 디스크 경로가 아니라 서빙 프로세스의 프로토콜·호스트·포트로 결정됨 — `StaticFiles(directory="../static")` 마운트로 static/을 backend/ 밖(프로젝트 루트)에 둬도 오리진은 그대로 하나(127.0.0.1:8000).
- 새 구조: `backend/`·`static/`·`frontend/`(하네스 전용, 런타임 코드 없음) 3개가 프로젝트 루트 형제 폴더. `docker-compose.yml`도 backend 전용이 아닌 공유 인프라로 판단해 프로젝트 루트 배치 권장.
- `tech-architecture.md`는 이번에 직접 갱신(§1-1 "프로젝트 파일 구조" 신설 + §5 결정 이력 추가) — tech-architect가 canonical 문서 소유자이므로 브리프만 전달하지 않고 실제로 덮어씀. TRD(05 문서) v1.0→v1.1 반영은 planning-writer 몫 — 브리프를 스크래치패드(`trd-structure-brief.md`)에 §2 mermaid/CORS 문장, §3 트리+마운트 코드, §4-4 NFR-05 문장(브리프 요청은 "§7"이라 했으나 실제 위치는 §4-4임을 정정 안내), §9-1 docker-compose 주석까지 그대로 복사 가능한 수준으로 작성해 전달.
- 03_기능정의서 v1.2의 `contact_app/` 트리(backend/ 래퍼 없음)와의 이름 체계 차이는 이번 범위 밖으로 명시적으로 보류.

### 2026-07-15 — 03_기능정의서 §1-1 이름 체계 통일 브리프 (`contact_app/` → `backend/`·`static/`·`frontend/`)
- planning-pl 브리프: 지난 라운드 각주에 남겨둔 이름 체계 차이(03 §1-1 `contact_app/` vs tech-architecture.md/05 TRD의 `backend/` 형제 구조)를 사용자가 이번 라운드에서 명시적으로 통일 승인.
- 03 v1.2 전문 재검색으로 `contact_app` 문자열이 §1-1 트리 단 한 곳에만 있음을 확인(§1-2 다이어그램·§2~§7은 상대 파일명만 써서 영향 없음).
- 핵심 판단(Surgical Changes): 폴더 이름 체계만 05/tech-architecture.md 기준으로 바꾸고, 03 원본 트리의 파일별 설명 주석(예: "DB 연결: 엔진, DB세션 공장, get_db")은 그대로 보존 — 05식 상세 주석으로 교체하지 않음. 03에 없던 신규 항목(`requirements.txt`, `frontend/`)만 05 TRD §3 문구를 그대로 채택.
- `docker-compose.yml`은 05 TRD §3 상세 트리에도 없으므로(§9-1에서만 다룸) 03 트리에도 미포함.
- `tech-architecture.md` §1-1 "참고" 각주를 "해소(2026-07-15)"로 갱신 + §5 결정 이력에 이번 판단 추가 완료(직접 갱신). 03 md 자체는 작성하지 않음(planning-writer 몫) — 브리프는 세션 스크래치패드 `03-structure-brief.md`로 전달.
