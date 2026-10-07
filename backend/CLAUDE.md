# backend/ 작업 가이드 (backend-engineer 전용)

이 파일은 `backend/` 폴더에서 작업할 때 참고하는 요약 가이드다. 정본(source of truth)은 항상 아래 `docs/planning` 문서들이다 — 여기 내용과 정본이 어긋나면 정본이 맞다. API 계약·DB 스키마 전체 내용을 여기 복사하지 않는다(중복되면 나중에 어긋난다) — 실제 값은 항상 정본 문서를 열어서 확인한다.

## 정본 문서
- `docs/planning/05_연락처관리_웹서비스_TRD_v1.4.md` — 기술 스택 확정, 전체 아키텍처, 프로젝트 파일 구조, DB 설계(DDL), 인증 설계
- `docs/planning/tech-architecture.md` — TRD와 같은 내용의 canonical 요약본
- `docs/planning/03_연락처관리_웹서비스_기능정의서_*.md` — 파일·함수 단위 설계

## 이 프로젝트의 확정 스택 (TRD §1)
Python 3.12+ / FastAPI 0.139.0 / Pydantic 2.13.4 / SQLAlchemy 2.0.51 / psycopg 3.3.4 / pwdlib[argon2] 0.3.0 / Uvicorn 0.50.0 / PostgreSQL 16(Docker, 컨테이너명 `pg-lab`) / pytest-playwright. 인증은 세션 쿠키(JWT 아님).

## 이 폴더의 실제 파일 구조 (TRD §3)
```
backend/
├── main.py          # FastAPI 앱 생성, 라우터 등록, static/ 마운트
├── database.py       # engine, SessionLocal, Base, get_db()
├── models.py           # User, LoginSession, Category, Contact
├── schemas.py           # Pydantic 입출력 스키마
├── security.py           # hash_password, verify_password
├── crud.py                 # DB 작업 함수 (조회/생성/수정/삭제)
├── routers/
│   ├── auth.py               # signup, login, logout, me, get_current_user
│   ├── contacts.py             # 연락처 CRUD 4개
│   └── categories.py            # 카테고리 CRUD 4개
└── requirements.txt
```

**주의 — 화면 코드(`index.html`/`app.js`)는 이 폴더 안에 없다.** 최상위 `static/` 폴더(프로젝트 루트, `backend/`·`frontend/`와 형제)에 있고, `main.py`가 `StaticFiles`로 그 경로를 마운트해서 서빙한다. 물리적으로 안 겹쳐 있어도 같은 포트(`127.0.0.1:8000`)에서 서빙되므로 오리진은 하나 그대로다 — CORS 미들웨어를 추가할 필요 없다.

## 레이어 원칙 (TRD §2, 기능정의서 §1-2 계승)
4계층: 화면(`static/`) → 표현(`routers/`, `schemas.py`) → 로직(`crud.py`, `security.py`) → 데이터(`models.py`, `database.py`). 각 계층은 자기 아래 계층만 호출한다(계층 건너뛴 호출 금지). **라우터가 상태 코드를 결정하고, `crud.py`는 DB 작업만 하며 상태 코드를 모른다.**

## `frontend/`와의 관계
화면(`static/`)을 만드는 건 frontend-engineer의 몫이다. 이 폴더(backend-engineer)는 API/DB 로직까지만 담당하고, 프론트가 호출하는 API의 계약(엔드포인트/스키마)만 정확히 지키면 된다.
