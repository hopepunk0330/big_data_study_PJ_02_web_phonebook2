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
