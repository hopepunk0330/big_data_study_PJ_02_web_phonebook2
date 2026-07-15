# frontend/ 작업 가이드 (frontend-engineer 전용)

**이 폴더는 실제 화면 코드가 위치하는 곳이 아니다.** frontend-engineer의 작업 가이드(이 파일) 홈일 뿐이고, 실제로 편집하는 파일은 최상위 `static/` 폴더(`backend/main.py`가 `StaticFiles`로 마운트해서 서빙)에 있다: `static/index.html`, `static/app.js`. 정본(source of truth)은 항상 아래 문서들이다 — 여기 내용과 정본이 어긋나면 정본이 맞다.

## 정본 문서
- `docs/design/design-system.md` — 토큰(색상/타이포/spacing/elevation)·컴포넌트 인벤토리, 인터랙션 상태(Hover/Press/Focus/Disabled 등)
- `docs/design/confirmed/` — 확정 프레임 요약(화면별)
- `docs/planning/02_연락처관리_웹서비스_화면정의서_*.md` — 화면 목적·구성요소-동작 표·상태 분기 플로우차트
- `docs/planning/05_연락처관리_웹서비스_TRD_v1.1.md` §2/§3 — 실제 파일 구조, 정적 파일 서빙 방식

## 실제 화면 코드 위치
```
static/
├── index.html   # SCR-001~003
└── app.js        # fetch 호출 + DOM 갱신
```
별도 프론트엔드 프레임워크나 빌드 단계 없음 — 순수 HTML/CSS/JS, FastAPI가 같은 오리진에서 직접 서빙(CORS 불필요).

## 토큰 사용 원칙
`design-system.md`의 토큰(예: `color/amber/500`)을 raw hex로 하드코딩하지 않는다 — CSS 커스텀 프로퍼티(`var(--color-amber-500)` 등)로 참조한다. 값이 애매하면 Figma 노드를 직접 재조회해서 확인한다(`get_design_context`/`get_screenshot`, 쓰기 권한 없음).

## `backend/`와의 관계
API 호출은 fetch로 backend의 엔드포인트를 그대로 호출한다(계약은 `backend/CLAUDE.md`가 가리키는 TRD 문서 참고). API 로직/DB 작업은 backend-engineer의 몫 — 이 폴더(frontend-engineer)는 화면·인터랙션까지만 담당한다.
