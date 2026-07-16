# tech-architect 메모리

이 파일은 tech-architect의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **기술 아키텍처 결정사항 자체(현재 확정 상태)는 여기 없습니다 — `docs/planning/tech-architecture.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

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

### 2026-07-16 — TRD(05 문서) §6/§10/§11의 FR-14/15 누락 갭 패치 (v1.1 → v1.2)
- 배경: 06_테스트계획서 작성 승인 전에, 01 문서(§2 FR표·§3-5)·04 PRD(§9 AC-18)에는 이미 확정된 FR-14/15(비밀번호 재설정)가 05 TRD v1.1의 §6 API 설계 요약 표·§10 테스트 전략(`tests/` 파일 구조, "API 계약 FR-01~13" 범위 문구)·§11 요구사항 추적표 세 곳에서만 빠져 있던 갭을 발견 — 06 작성 전 선행 패치로 요청받음.
- 새 API/DB 판단 없음(§4의 기존 결정을 그대로 인용) — 01 §3-5·§5-1 근거로 성공 200/실패 404,422 재확인만 함.
- 확정: ① §6에 인증 그룹 행 2개(`POST /auth/find-password`, `PATCH /auth/password`) 추가. ② §10-1 `tests/` 구조에서 FR-14/15·AC-18을 신규 파일로 쪼개지 않고 기존 `test_auth.py`에 포함(그룹·로그인 불필요 성격이 FR-01~04와 이어짐, Simplicity First — 4개 파일 구조를 이유 없이 5개로 늘리지 않음), §10-2 "FR-01~13"→"FR-01~15" 정정. ③ §11에 FR-14~15 행 추가(대응: §6 API 설계, §5 인증 설계 — 세션 전체 무효화 로직 포함).
- `tech-architecture.md`는 이번에 직접 갱신(§4 말미에 "후속 갱신" 문단 추가 + §5 결정 이력 추가) — TRD(05 문서) v1.1→v1.2 실제 반영은 planning-writer 몫. 브리프는 스크래치패드 `trd-v1.2-brief.md`에 §6 표 행 문구, §10-1/§10-2 정확한 변경 전후 문구, §11 행 문구, 변경 이력에 넣을 v1.2 항목 문구까지 그대로 복사 가능한 수준으로 작성.

### 2026-07-16 — harness-auditor 감사 후속 2건: TRD §6 로그아웃 각주 판단 브리프 + tech-architecture.md §4 stale 버전 인용 직접 정정
- 배경: harness-auditor가 TRD v1.2/02 v1.6/06 v1.0 라운드를 감사해 발견한 항목 중 tech-architect 몫 2건을 planning-pl(메인 세션)이 전달.
- ① TRD §6 354행(`POST /auth/logout` "인증 필요: 필요") 판단: 텍스트만 보면 "실패 코드: -"라 모순은 아니지만(단순 그룹 분류 표시), 06 문서 작성 중 qa-planner가 실제로 이 지점에서 혼란을 겪었던 전례(변경 이력 v1.0, `[^logout-idempotent]`)가 있어 "이미 한 차례 발생한 오독"으로 판단 — 각주 1줄 추가가 맞다고 결론. 표 재구조화 없이 354행에 각주 마커, 표 아래에 각주 정의 1줄 추가하는 문구를 브리프로 작성(01 §3-1 FR-03 근거, "실패코드 -"가 이미 반영하고 있다는 논리, 06 §4-1 각주 상호 참조). TRD md 자체는 갱신하지 않음(planning-writer 몫) — 브리프는 스크래치패드 `trd-logout-footnote-brief.md`.
- ② tech-architecture.md §4 "배경" 문단의 "화면정의서 v1.3" 인용: §4는 "§5 결정 이력"과 달리 보존 안내 없는 유효 canonical 절이므로 stale 인용은 단순 실수로 판단 — SCR-004 내용 서술은 그대로 두고 버전 숫자만 v1.6으로 직접 정정(Write로 전체 갱신). §5 결정 이력에도 이번 정정 이력 1줄 추가.
- `tech-architecture.md`는 이번에 직접 갱신(§4 배경 문단 버전 수정 + §5 결정 이력 추가). ①의 05 TRD md 실제 갱신은 별도로 planning-writer 몫.

### 2026-07-16 — DB 커넥션 재연결 설계 브리프 (`pool_pre_ping=True`, TRD v1.3 → v1.4)
- 배경: 06 테스트계획서 §7 `TC-PERSIST-02`(DB 컨테이너 `pg-lab` 재시작 후 서버 재기동 없이 즉시 재요청 → 데이터 그대로 조회, AC-16 근거)를 통과시키려면 SQLAlchemy 커넥션 풀이 죽은 커넥션을 자동 재연결해야 하는데, 05 TRD §4-4 `database.py` 예시(`engine = create_engine(DATABASE_URL)`)·tech-architecture.md §1 어디에도 재연결 설계가 없어 01 문서 NFR-01(500 금지) 위반 소지가 있었음. 사용자가 "pool_pre_ping=True 같은 SQLAlchemy 표준 방식으로 지시해도 될까"를 구체적으로 확인 후 승인.
- 판단: `create_engine(DATABASE_URL, pool_pre_ping=True)` 한 줄(옵션 추가)만 surgical하게 변경 — 커넥션 체크아웃 직전 헬스체크·자동 재연결이 애플리케이션 코드 밖(풀 내부)에서 일어나므로 `get_db()`의 rollback 예외 처리는 손대지 않음. TRD 본문에는 06/`TC-PERSIST-02`를 직접 인용하지 않기로 판단(TRD는 00~04만 근거 문서로 인용하는 기존 관례 — 06이 05를 인용하는 방향만 있고 반대 방향 전례 없음, 05 §10이 `test_persistence.py`를 언급하면서도 06을 인용 안 한 것과 동일 패턴). "DB 재시작" 시나리오는 일반 서술로만 설명.
- `tech-architecture.md`는 이번에 직접 갱신(§1 표에 "DB 커넥션 복원력" 행 신설 + §5 결정 이력에 `TC-PERSIST-02` 인용 포함한 판단 배경 추가 — 그 문서는 내부 판단 로그라 인용 제약이 TRD와 다름). TRD(05 문서) v1.3→v1.4 실제 반영은 planning-writer 몫 — 브리프는 스크래치패드 `db-reconnect-brief.md`에 코드 diff(277행 1줄), NFR-01 연결 문단, 변경 이력 v1.4 문구, 함께 손볼 곳 체크리스트까지 그대로 옮겨쓸 수 있는 수준으로 작성.
