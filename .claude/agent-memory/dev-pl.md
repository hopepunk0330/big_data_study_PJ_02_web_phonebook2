# dev-pl 작업 로그

## 2026-07-17 — 프론트엔드 전체 구현 + 백엔드 테스트 정합화, 데드라인 라운드 — 118/118 GREEN, 두 게이트 통과

**배경**: 마감 23:00(원래 23:30) → 사용자가 제출 마감 연장. "카테고리 이름 11자 검증 백엔드 버그"+"프론트엔드 전체 미구현" 지시.

**핵심 발견**: 지시된 백엔드 버그는 실제로 테스트 데이터 버그(`backend/schemas.py`엔 이미 `max_length=10` 정확히 있었음, `test_categories.py` 문자열이 실제론 10자인데 주석만 "11자") — backend 무변경, 테스트만 정정. signup()만 하고 login() 안 한 채 인증 API 호출하는 패턴 12곳도 수정.

**프론트엔드 최초 구현**: `docs/planning/02`+`docs/design/confirmed/user-confirmed-final-design.md`(8개 확정 프레임)+백엔드 API 계약+테스트 하드코딩 텍스트를 스펙으로 `static/index.html`/`app.js`/`styles.css` 신규 작성.

**게이트**: qa-engineer 118/118 GREEN, code-reviewer 통과. 하네스 신설(단위/통합 분리 실행+`docs/test-reports/` 문서화).

## 2026-07-17(밤)~07-18 — 카테고리 모달 2건 + design-qa 검수 4건 + "전체 재추출" 대규모 UI 정합화 (다수 라운드)

**카테고리 삭제확인/이름수정 모달(missing-screens.md 4/6번)**: design-pl 확정 후 정식 반영. TDD 순서(Figma 조사→qa-engineer 테스트 5개 선작성→frontend-engineer 구현→재검증) 준수. **주의**: qa-engineer 작업 중 세션 API 한도로 에이전트가 끊겼지만 디스크 반영분은 정상이라 재작업 불필요 — 에이전트 "완료 보고" 유무와 무관하게 파일 상태를 항상 직접 재확인해야 함(재발 교훈).

**design-qa 정식 검수 4건**: Pydantic 영문 메시지(backend-engineer 한글화 완료) / Join-login 미분화(사용자 확인 후 "통합 구조 유지"로 종결) / 로고 렌더링 8+화면(재조사 결과 스테일 스크린샷 1개만 확인, 나머지 정상) / 카테고리 삭제거부 배너(실제론 이미 존재, 테스트 대기조건 flaky만 발견).

**"전체 재추출" 대규모 라운드(담당자 frontend-engineer 고정, `figma-design-to-code` 스킬 정식 워크플로우 전환)**: 매우 많은 라운드에 걸쳐 처리 — 로고-배너 순서, Row Action 버튼 완전 교체, 아이콘 22종 체크리스트(Avatar 완전 누락 발견), Hover/Press/Focus/Disabled 전체 구현, CategoryNav/Manage 실측 스크롤, FOUC, `.banner` 10곳 전역 오버레이, 빈 상태 카피/CTA, 테이블 컬럼 고정폭, 검색 Enter키, **사이드바 카테고리 nav 클릭 필터링(신규 기능, docs/planning/02 255번째 줄과 충돌 — 사용자 결정으로 확장, qa-engineer 테스트 4건 추가, 문서 개정은 planning 팀 후속 필요)**, 인풋 포커스 마우스/키보드 구분, `.banner` 자동소멸 타이머, 테이블 8행 스크롤(1차 시도 실패 후 wrapper+sticky 방식으로 성공).

**메인 세션 직접 처리(재작업 불필요)**: `.brand-badge` 색상, 전역 focus 리셋, 테이블 tr→td 보더, TypeSelector 2건, `categoryStyleFor(name,id)` 시그니처 변경.

## 2026-07-18 — 최종 마무리 라운드: 사파리→크롬 정정, 웹폰트 누락 발견, 배너 완전 공통화, sticky→분리헤더 재구현, 최종 122/122 GREEN

**sticky 헤더 브라우저별 재검증**: 처음엔 Safari 가설로 WebKit 설치·재현 지시(사용자가 나중에 "크롬 사용"으로 정정) — WebKit 자체에서는 기존 sticky 방식도 재현 안 됐지만, 이미 지시한 대로 더 견고한 구조(헤더를 테이블 밖 별도 `div`로 완전 분리, sticky 자체 제거, 컬럼폭은 CSS 변수로 헤더/본문 공유)로 교체 완료 — 브라우저 무관하게 안전. 재구현 중 진짜 회귀(`td.actions`의 flex가 `table-layout:fixed` 계산을 깨뜨림) 추가 발견·수정.

**웹폰트 완전 누락 발견(메인 세션 직접 확인·수정)**: `static/index.html`에 `font-family: "Noto Sans KR"/"Baloo 2"`를 CSS 전체가 지정만 하고, 실제로 로드하는 `<link>`/`@font-face`가 어디에도 없었음 — 폰트 없는 모든 환경에서 계속 기본 sans-serif로 조용히 폴백되고 있었음(로고 폰트 다름 지적의 근본 원인). Google Fonts 링크 추가로 해결, frontend-engineer가 `document.fonts` API로 로드 확인 + 주요 화면 재스크린샷 대조 — 폭/줄바꿈 회귀 없음 확인(기존 CSS가 이미 여유 있게 설계돼 있었음).

**main 화면 배너 완전 공통화(사용자 결정)**: 카테고리 삭제 에러가 사이드바 "새 카테고리" 입력창을 가리던 트레이드오프 해소 — 유일하게 남아있던 `#category-error`(사이드바 로컬 오버레이)를 `main-error-toast` 공용 슬롯(콘텐츠 영역 상단, 검색행 위)으로 통합. 나머지 main 화면 배너는 이전 라운드에서 이미 통합 완료 상태였음. 모달 내부 배너(`edit-error-banner`)는 `test_tc_e2e_scr002_08`의 "모달 유지" 단언 때문에 예외로 모달 안에 유지(의도적 유지). 로그인/가입/비밀번호재설정 카드 배너는 범위 밖(그대로 유지).

**최종 검증**: 단위 76 + 통합 46(E2E 42 + PERSIST 4) = **122/122 GREEN**, 오늘 하루 전체 작업 회귀 없음. `docs/test-reports/{unit,integration}-2026-07-18.md` 최신화, 어제자(07-17) 보고서는 `docs/test-reports/old/`로 아카이브. `docs/screenshot/`는 사용자 결정으로 전체 삭제 후 재생성 — 82장(주요 플로우 전체 커버 확인, 과거 orphan 파일도 사라짐).

**Notion 동기화 미처리**: `CLAUDE.md`의 "테스트 보고서 Notion 동기화" 절이 요구하는 두 Notion 페이지 반영은, 이번 세션에 연결된 MCP 서버가 context7·Figma뿐이고 Notion MCP가 없어서 dev-pl 팀 어떤 워커도 수행 불가 — **메인 세션/사용자가 별도 처리 필요**(Notion MCP 연결 후 재요청).

**후속 필요 사항(사용자/코디네이터 판단 대기)**:
1. Notion 동기화 — MCP 도구 부재로 미처리(위 참고).
2. `docs/planning/02` 255번째 줄("클릭 시 필터링 없음") — 카테고리 nav 필터 기능 확장에 따른 개정 필요, planning 팀 후속(dev-pl 권한 밖).
3. Button 리딩 아이콘 슬롯, 로그인 체크박스 네이티브 스타일 — 발견만, 낮은 우선순위로 미처리.
4. code-reviewer가 반복 지적한 이중 제출 가드 일관성 부족 — 후속 후보.
5. git commit/push는 진행 안 함(dev-pl 권한 밖, 메인 세션이 사용자 승인 하에 처리 — 완료 보고 후 커밋 예정이라고 코디네이터가 확인함).
6. **하네스 누적 교훈**: (a) 에이전트가 세션 한도로 끊겨도 디스크 반영분은 유효 — 항상 파일 직접 재확인. (b) `:focus-visible`은 버튼/링크와 텍스트 인풋에서 브라우저 동작이 다름(인풋은 마우스 클릭도 매치) — JS 마우스/키보드 추적 필요. `:focus-within`(래퍼)도 같은 이슈가 있고, 인풋 자체가 전역 `*:focus-visible`에 별도로 매치될 수 있어 래퍼+필드 양쪽 다 확인 필요. (c) `border-collapse`/`overflow`/`table-layout`/`display:block` 분리 등 CSS 상호작용 버그는 겉보기와 실제 원인이 다를 수 있어 실측 필수. (d) 대규모 UI 정합화는 화면별 개별 대조만으로 공유 클래스 버그를 놓칠 수 있어 클래스 단위 전수 확인이 별도 필요. (e) 브라우저 가설(Safari 등)은 실제 재현 전까지 확정하지 않는다 — 이번엔 가설이 틀렸어도 더 견고한 대안 구현 자체는 유효했음.
