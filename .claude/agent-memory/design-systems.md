# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-14 — `Pixel/Star` description 정정 + `Pixel/Eye` 아이콘 마저 추출·등록 (원본 확정 프레임 무수정)
- **Pixel/Star(`255:11`) description 오기 정정**: description 텍스트가 "흰색"이라고 적혀 있었으나 마스터 컴포넌트 vector fill 실측값은 잉크 `#1a1a1a`(graphic-designer가 이미 관찰해 `docs/design/graphic-assets.md`에 특이사항으로 기록해둔 것). fill 값은 정상이라 건드리지 않고 description 텍스트만 실측값에 맞게 정정.
- **Pixel/Eye 신규 등록**: 최초 9종 추출 라운드(2026-07-13)에서 누락됐던 비밀번호 표시/숨김 토글 아이콘. 확정 login 프레임(`247:6666`) 내 `PixelEye`(`247:6814`, 14×10, 6개 vector 블록, 잉크 `#1a1a1a`)를 `node.clone()` → 페이지 이동(파일럿 페이지 `222:524` → Icons 페이지 `96:7`, x=1080/y=2000) → `createComponentFromNode()`로 `Pixel/Eye`(`281:405`) 컴포넌트화. 원본은 무수정으로 `247:6814`에 그대로 존재함을 clone 직후 재확인. 스크린샷으로 형태(눈 실루엣, 6블록) 검증 완료.
- `docs/design/design-system.md`(0-2절 신설 + 4절 Icons 목록 10종으로 갱신) / `docs/design/graphic-assets.md`(Pixel/* 10종 표 갱신 + 발견사항 처리 완료로 갱신) 문서 반영.

### 2026-07-13 — WCAG/터치타겟 5건 RESOLVED 전환 + Legacy 5개 컴포넌트 리네임 + 상단 경고 문구 추가 (문서·이름 변경만, 원본/내용 무수정)
- 배경: 사용자가 design-qa 감사에서 지적된 WCAG 대비/터치 타겟 미달 5건(뮤트 텍스트 2건, 사이드바 비활성 nav 텍스트/라벨 대비 미달, Table Row Action 텍스트 대비 미달, 터치 타겟 44×44px 미달 다수, placeholder 텍스트 대비 미달)을 "이번 프로젝트에 한해 무시하고 원본 그대로 유지"하기로 명시적으로 확정.
- `docs/design/design-system.md` 7절을 7-1(RESOLVED, 위 5건 — 각 항목에 "사용자 확인 후 이번 프로젝트 범위에서 개선하지 않기로 결정 — 원본 확정 프레임 값 그대로 최종" 명시)/7-2(TODO, TypeSelector 미관찰 accent 등 별개 4건 그대로 유지)로 분리 재구성. 3절 뮤트 텍스트 대비 계산 하단의 "별도 보고 필요" 문구도 RESOLVED로 갱신. 원본 확정 프레임 8개는 전혀 손대지 않음(문서 텍스트만 변경).
- Figma에서 Legacy 컴포넌트 5개(`Input` 100:46, `Select` 101:64, `Badge` 102:65, `Table Row` 103:7, `Alert` 104:108) 이름 앞에 `[Legacy B-2] ` 접두사 추가(내용 무수정, 이름만 변경) — 기존에 이미 리네임된 Button/Row Action Button/Sidebar Nav Item과 합쳐 legacy 9개 중 8개가 접두사로 구분됨. Avatar(104:131)는 현재도 유효해 접두사 없이 그대로 둠(유일한 예외). design-system.md 0절/8절 표도 갱신.
- 문서 최상단(1절 시작 전)에 굵은 경고 문구 추가: "ui-designer 등 컴포넌트를 소비하는 모든 에이전트는 반드시 1~7절만 참조하고 8절(Legacy)은 절대 사용하지 않는다."

### 2026-07-13 — 사용자 확정 디자인(8개 프레임)에서 토큰/컴포넌트 전면 추출 (2-4번 규칙, B-2 파일럿 완전 대체)
- 배경: 사용자가 Figma에서 직접 만들어 확정한 8개 프레임("확정 디자인 - 절대 원본 건들지 말것-")에서 파일럿을 거치지 않고 직접 추출. `docs/design/confirmed/user-confirmed-final-design.md` + `docs/design/brand-guide.md`(둘 다 이번 라운드 갱신본)를 최우선 근거로, 8개 프레임을 `get_screenshot`/`get_metadata`로 직접 재관찰(읽기 전용, 원본 무수정)해 실측값만 옮김.
- **토큰**: `color/ink/900`을 실측값 `#1a1a1a`로 정정(기존 `#1C1F21`). CatBadge 카테고리 팔레트(친구/가족/기타/회사 × bg/border/text) 신규 semantic 12개 + primitive 10개. 뮤트 텍스트 3종(`#555/#777/#888`) 신규 — **WCAG 실측 결과 `text-muted`(4.46:1)·`text-muted-subtle`(3.55:1) AA 미달을 발견, 원본 실측값이라 임의로 진하게 바꾸지 않고 미달인 채로 기록**(이후 라운드에서 사용자 확정으로 RESOLVED 처리됨, 위 항목 참고). 하드 "스티커" 그림자(블러 없음, ink 100%, 1/2/6px) 3개 Effect Style을 소프트 `Elevation/Raised`(alert 전용, 재사용 시작)와 완전히 분리 신설 — confirmed 문서가 명시적으로 요구한 항목. radius 0/6/10, border-weight 1/2/3px 신규. 텍스트 스타일 10종(Baloo2/Inter/NotoSansKR 5단 위계) 신규.
- **TypeSelector vs CatBadge 불일치 결정**: CatBadge를 정식 카테고리 팔레트로 채택, TypeSelector는 원본을 그대로 재현하되 `component/typeselector-*` 전용 토큰으로 격리(혼용 금지). 근거·미관찰 상태(친구/기타 선택 accent) 처리 방식을 design-system.md 2절에 기록.
- **아이콘**: 보호된 원본 프레임에서 `node.clone()` → 페이지 이동 → `createComponentFromNode()` 방식으로 비파괴 추출(원본 전혀 미수정), `Pixel/*` 네임스페이스 9종(Star/Search/Plus/Logout/Edit/Delete/Close/Warning/NoResult) 신규 등록. `Icon/Alert`·`Icon/User`(기존 8종)는 확정 디자인에서도 그대로 재사용됨을 확인해 중복 생성 안 함.
- **컴포넌트 15개 신규**: CatBadge, TypeSelector, Count Pill, Sidebar Nav Item, NeoBtn(Style×Size=8), Button(Style=3), Icon Button(Close), Row Action Button(아이콘, 사이드바 카테고리 관리 전용), Table Row Action(텍스트 pill, main 테이블 전용 — Row Action Button과 의도적으로 별개 컴포넌트), NeoInput, CornerInput(4모서리 ㄱ자 브래킷, `layoutPositioning='ABSOLUTE'` 필요했음 — 처음엔 auto-layout 자식으로 배치되어 브래킷이 위치를 잃는 버그 발생, 수정 확인), NeoSelect, Card(Type=Modal/Auth 쉘, Content는 화면 조립 시 채움), Toast(Type=Success/Error, 플로팅 오버레이 패턴을 컴포넌트 설명에 명시), Logo(Background=Teal/White, 워드마크 색 반전). Avatar는 기존 컴포넌트가 확정 디자인과 정확히 일치해 재사용, 신규 작업 없음.
- **이름 충돌 3건 처리**: 새 컴포넌트가 기존 B-2 파일럿 컴포넌트와 이름이 겹친 Button/Row Action Button/Sidebar Nav Item — 기존 것을 `[Legacy B-2] ` 접두사로 리네임(내용 무수정, 이름만 변경)해 구분.
- 신규 페이지 2개(Card, Logo)를 COMPONENTS 규칙 순서에 맞게 `insertChild`로 삽입(Alert 페이지 앞).
- 도구 이슈 재확인: `use_figma` 스크립트는 원자적(atomic) — 중간에 에러 나면 그 호출 전체가 롤백되어 부분 생성물이 전혀 남지 않음(Card 페이지 생성 스크립트가 `layoutSizingHorizontal` 순서 오류로 실패했을 때 페이지 자체가 사라졌던 것으로 확인).
- `docs/design/design-system.md` 전면 갱신 — 1~7절을 이번 확정 디자인 기준 신규 내용으로 교체, 기존 B-2 인벤토리는 8절 "Legacy"로 이동(삭제 안 함).

### 2026-07-13 — `color/text-inverse` 시맨틱 토큰 신설 (SCREENS 파일럿 승인 전 예외 호출, 시스템 레벨 단독 작업)
- 배경: 파일럿이 아직 사용자 최종 승인 전이라 원칙상 design-systems를 부를 단계가 아니지만, design-pl이 "화면 결함 수정이 아니라 사용자가 직접 요청한 시스템 레벨 신규 토큰 작업"이라 명시적으로 예외 승인. 화면 적용은 하지 않고 토큰 신설·문서화까지만 진행.
- WCAG 2.1 상대휘도 공식으로 브랜드 3색(teal/coral/amber) 배경×흰 텍스트(#FFFFFF) 대비를 직접 재계산: teal 3.1200:1, coral 3.0111:1, amber 1.5122:1 — design-pl 사전 검증표(3.12/3.01/1.51)와 소수점까지 정확히 일치 확인.
- 결론: teal·coral은 큰 텍스트(3:1) 기준 PASS(coral은 여유폭 0.01로 매우 근소), amber는 큰 텍스트 기준조차 크게 미달(1.51:1)해 전면 사용 금지로 확정.
- 신규 primitive 만들지 않음 — 기존 `color/gray/0`(#FFFFFF)을 그대로 alias해 `color/text-inverse` 생성. scope=TEXT_FILL, WEB code syntax 설정.
- 적용 범위를 좁게 문서화: teal·coral 배경 위 Display/제목급 텍스트에만 허용, amber는 금지, Body/Caption 제외.

### 2026-07-12 — "등록된 아이콘 실사용" 규칙 첫 적용: 컴포넌트 레벨 결함 3건 수정 (신규 토큰/컴포넌트 없음)
- Row Action Button(`166:421`, 이번 라운드 [Legacy B-2]로 리네임됨) Neutral/Danger 아이콘 오류 수정(Icon/Delete로 정정). Input에 검색 아이콘 슬롯 신설. 헤더 로그아웃은 기존 Button Icon 스왑으로 충분함을 확인.
