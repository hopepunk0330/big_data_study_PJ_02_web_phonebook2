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
