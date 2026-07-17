# code-reviewer 메모리

이 파일은 code-reviewer가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-16 — backend/ (feat/backend 브랜치) FastAPI 백엔드 정적 리뷰
대상: backend/main.py, database.py, models.py, schemas.py, security.py, crud.py, routers/{auth,contacts,categories}.py, requirements.txt, static/index.html, docker-compose.yml, .env.example, .gitignore

- **blocker**: `backend/database.py`가 `from dotenv import load_dotenv`를 쓰는데 `backend/requirements.txt`에 `python-dotenv`가 없음 → 클린 설치 시 서버 기동 자체가 ModuleNotFoundError로 실패. TRD §4-4 예시엔 애초에 dotenv가 없음(os.environ만 사용) — 확정 스택에도 없는 라이브러리를 추가하면서 requirements.txt 등록을 빠뜨린 케이스. 다음 리뷰에서도 requirements.txt 누락 여부는 계속 체크.
- 레이어 원칙(라우터=상태코드 결정, crud.py=DB작업만)은 잘 지켜짐 — crud.py에 HTTPException 없음, 확인함.
- 보안 체크(세션 쿠키 httpOnly/samesite, ORM 파라미터 바인딩, 인증 미들웨어 covering) 전부 이상 없음.
- .env는 .gitignore 등록되어 있고 .env.example엔 placeholder("changeme")만 있어 실제 비밀값 노출 없음.
- minor: crud.py에서 SQLAlchemy 2.0 스타일(select()+db.scalar)과 레거시 스타일(db.query().filter())이 혼용됨(reset_password, count_contacts_in_category). 다음에도 반복되면 일관성 지적 재사용 가능.
- minor: schemas.LoginIn에 길이 제한 없음(SignupIn과 달리 max_length 미지정) — 다음 리뷰에서도 신규 스키마에 길이 제한 빠졌는지 체크 포인트로 둘 것.
- 이번 라운드는 반복 지적 없음(첫 리뷰).

### 2026-07-17 — static/(index.html, app.js, styles.css) 프론트엔드 신규 구현 + tests/*.py 로케이터 정밀화 정적 리뷰
대상: static/index.html, static/app.js, static/styles.css(신규), tests/test_auth.py, tests/test_contacts.py, tests/test_categories.py(수정), pytest.ini(신규). backend/는 이번 라운드 변경 없어 제외.

- XSS 체크 결과 양호: app.js는 동적으로 꽂는 사용자 입력(contact.name/phone/addr/category_name, cat.name)에 전부 `escapeHtml()`(textContent→innerHTML 왕복 표준 기법)을 거치거나, `.value`/`.textContent`/`setAttribute`(HTML 파싱 안 함)로만 대입함 — innerHTML에 원본 문자열을 그대로 꽂는 곳 없음. `window.confirm()`/`prompt()` 문자열에 이름을 넣는 것도 네이티브 다이얼로그라 HTML 파싱 경로 자체가 없어 안전.
- **medium**: `apiRequest()`(app.js ~53-75)가 `resp.json()` 파싱 실패만 try/catch로 감싸고 `fetch()` 자체의 네트워크 예외는 처리하지 않음. add-contact-form(try/finally로 감쌈)을 제외한 나머지 호출부(로그인 폼 제출, 회원가입/비번찾기/비번재설정 폼 제출, 카테고리 추가/수정/삭제, 연락처 수정/삭제)는 try/catch가 없어 네트워크 장애 시 unhandled rejection이 발생하고 사용자에게 아무 에러 메시지도 안 뜬 채 그대로 멈춤 → apiRequest 내부에서 fetch를 try/catch로 감싸 `{status:0, ok:false, body:null}` 같은 값을 반환하도록 일원화 권장.
- **low**: 이중 제출 가드(`state.addingContact`)가 연락처 추가 폼에만 있고 카테고리 추가/수정/삭제, 연락처 수정/삭제엔 없음 — 서버 유니크 제약으로 대부분 흡수되긴 하나(중복 클릭 시 두 번째 요청은 409/404로 처리됨) 일관성이 떨어짐. 다음 라운드에 반복되면 지적 재사용 가능.
- **low**: "테스트 호환" 목적의 DOM 순서 조정/placeholder 비우기 패턴(app.js AUTH_PLACEHOLDERS·CONTACT_FIELD_PLACEHOLDERS, index.html 로그인 필드 CSS order 트릭, 연락처/카테고리 "추가" 버튼 DOM 순서)은 주석이 잘 달려 있고 시각/포커스 순서는 보존돼 있어 이번 라운드 자체를 막을 정도는 아님. 다만 필드 추가 시마다 이 표들을 계속 갱신해야 하는 부채이므로, 장기적으로는 `data-testid` 같은 안정적 로케이터로 이전하는 걸 권장(후속 티켓감, 이번엔 승인).
- **low**: 카테고리 삭제/이름수정 네이티브 confirm()/prompt() 사용 — 보안 문제는 없음(다이얼로그는 HTML 파싱 안 함). 확정 디자인 문서(커스텀 ConfirmModal)와의 불일치가 이미 주석과 dev-pl 보고로 추적되고 있어 임시 조치로 수용 가능.
- tests/test_auth.py, test_contacts.py, test_categories.py 검토 결과 로케이터 정밀화(`.first`, `.nth(0)/.nth(1)`, `exact=True`, `get_by_role("row"/"listitem", name=...)`)만 있고 어설션을 약화/삭제/우회한 곳은 없음. 스크린샷 캡처는 추가적(additive)이라 검증 로직에 영향 없음. conftest.py의 unique_phone()/contact_payload() 등 헬퍼도 문서상 전화번호 규칙(^010\d{8}$)과 일치.
- pytest.ini는 실행 설정(base_url)만 추가, 비밀값 없음.
- 이번 라운드 반복 지적: 없음(백엔드 리뷰와 대상 파일이 겹치지 않음). 다음 프론트엔드 라운드에서는 위 medium(네트워크 에러 처리 누락)과 이중 제출 가드 일관성 재확인 필요.
