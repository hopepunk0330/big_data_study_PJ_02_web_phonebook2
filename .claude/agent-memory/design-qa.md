# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-12 — SCREENS 3차본(Login `153:19` / Contacts-With Data `153:373` / Contacts-Empty `153:547`) 감사

- **PASS**: 사이드바 teal(`#17A398`) 풀블리드 — 자식 요소 흰 fill로 가려지는 이전 결함 재발 없음(두 Contacts 화면 모두 확인).
- **PASS**: 워드마크(Baloo 2 Bold 26px, 자간 0%, `#0F7A6E`, 심볼 24×24 간격 14px) — 9-2절 표와 정확히 일치.
- **HIGH(신규)**: Button/Input/Select/Badge(Pill)/Table Row/Sidebar Nav Item/Alert(Message Banner) 전부 실제 컴포넌트 인스턴스가 아니라 하드코딩 프레임(get_metadata상 `<frame>`, `<instance>` 아님) — fill/stroke/spacing이 리터럴 값으로 박혀 있어 "No token = no component" 위반. Size=Large/Default 분리 적용도 실제 variant 스위치가 아니라 수치 눈대중 흉내(Contacts Input 10×7/Button 12×7은 design-system.md의 Default 스펙과도 불일치, 옛 원본 수치와만 일치).
- **HIGH(신규)**: Row Actions SmallBtn(수정/삭제) 터치 타겟 37×21px — WCAG 44×44px 미달(테이블 행 6곳 + 사이드바 카테고리 관리 4곳, 두 Contacts 화면 공통).
- **MEDIUM(신규)**: Contacts—Empty 빈 상태 그래픽이 로고 심볼(코랄+잉크 스트로크) 재사용이 아니라 앰버 단색 원으로 대체됨(1-3절 위반).
- **MEDIUM(신규)**: 로고 심볼 노드명이 Figma 기본값 "Ellipse"로 방치(다른 레이어는 전부 의미있는 이름).
- **LOW**: b-2-contacts-layout.md 6절 색상표에서 teal·amber 행 모두 "추가 버튼"을 언급해 실제 화면에서 메인 추가(teal)/카테고리 추가(amber) 색이 문서상 모호함(화면 자체는 내부 일관, 문서만 모호).
- **기존 트래킹**: Button Disabled 4종 WCAG 미달(1.93:1) — 이번 화면엔 미노출, 재확인 대상 아님.
- 다음 감사 시 확인할 것: 위 HIGH 2건(컴포넌트 미바인딩, 터치 타겟)이 실제 인스턴스 교체로 수정됐는지 최우선 재확인.

### 2026-07-12 (재감사) — 같은 3화면, design-systems(2회)+ui-designer(2회) 수정 후 재확인

fileKey `zgGlMBwFglaDlaeyP4CkgR`. `get_metadata`+`get_design_context`+`get_screenshot`로 세 화면(Login `153:19`/Contacts-With Data `153:373`/Contacts-Empty `153:547`) 직접 재확인, `docs/design/design-system.md`·`docs/design/confirmed/b-2-contacts-layout.md` 최신본과 대조.

- **PASS(해소 확인)**: Button/Input/Select/Table Row/Sidebar Nav Item/Alert/Row Action Button 전부 실제 `<instance>`로 교체됨(get_metadata), get_design_context 코드에서도 `bg-[var(--component-...)]`/`border-[var(--color-border-ink,...)]`/`px-[var(--spacing-...)]` 등 전 속성이 CSS 변수 바인딩. 하드코딩 리터럴 없음. Input(size="Large"), Table Row 등에서 실제 variant prop 확인. Default padding도 confirmed와 정확히 일치(Input 10×7=spacing-2-5/1-75, Button 12×7=spacing-3/1-75, Table Row 12×9=spacing-3/2-25) — "No token = no component" 위반 해소.
- **PASS(해소 확인)**: Row Action Button(수정/삭제) 터치 타겟 44×44px로 확정(component `166:421`의 Style=Neutral/Danger 둘 다 44×44, 테이블 행 내부 edit-action/delete-action div `size-[44px]`, 사이드바 카테고리 관리 8개 인스턴스 전부 width/height=44 — get_metadata로 개별 확인). WCAG 44×44 충족.
- **PASS(해소 확인)**: Contacts—Empty 빈 상태 그래픽이 코랄 채움+잉크 스트로크 원(로고 심볼) 재사용으로 교체됨 — 스크린샷으로 색상 직접 확인(앰버 단색 아님).
- **PASS(해소 확인)**: 로고 심볼 노드명이 두 Contacts 화면 모두 "Logo Symbol"로 정정됨("Ellipse" 잔존 없음). Login 화면은 사이드바 구조 자체가 적용 안 되는 화면(confirmed 스펙상 "적용 안 함")이라 로고 노드가 원래 없음 — 검사 대상 아님, 결함 아님.
- **PASS(해소 확인)**: 색상 배정 완전히 정정됨 — 사이드바 "새 카테고리 추가" 버튼=teal Primary(`component-button-bg-primary`, 스크린샷 확인), 본문 "연락처 추가" 버튼=amber(`component-button-bg-amber`, 스크린샷 확인). confirmed 6절(카테고리 추가=teal / 연락처 추가=amber)과 정확히 일치. 문서 자체도 현재는 "카테고리 추가 버튼"/"연락처 추가 버튼"으로 명시돼 모호함 해소됨(이전 LOW 지적 반영 확인).
- **회귀 없음 확인**: Sidebar Nav Item Default(투명, bg 클래스 없음)/Active(amber `component-navitem-bg-active`) 정상. Alert 내부 content 서브프레임 흰 박스 없음(bg 클래스 없이 투명, 민트 틴트 배경 그대로 노출). Table Row divider `border-[var(--component-table-row-border,#e0e0e0)]` — confirmed `#E0E0E0`과 정확히 일치. Button Style=Amber variant 정상 동작.
- **기존 트래킹 재확인**: Button Disabled 4종 WCAG 미달 — 이번 3화면에도 Disabled 버튼 인스턴스 자체가 노출되지 않음(로그인/Contacts 모두 Default 상태만 사용), 발생 여부 재확인 결과 미노출 유지. `docs/design/design-system.md` "알려진 갭"에 여전히 트래킹 중(별도 라운드 필요, 이번 감사 범위 밖).
- **종합**: 지난 라운드 HIGH 2건 + MEDIUM 2건 + LOW 1건 전부 PASS(해소 확인). 신규 발견 없음.

### 2026-07-13 (3라운드 최종 재감사) — 컴포넌트 레벨 수정(design-systems) + 파일럿 3화면 반영(ui-designer) 검증

fileKey `zgGlMBwFglaDlaeyP4CkgR`. Row Action Button(`166:421`) edit/delete 아이콘 배선, Input(`100:46`) 검색 아이콘, Button(`97:8`) 헤더 로그아웃 패턴, Table Row(`103:7`) 14개 인스턴스, Sidebar Nav Item(`103:106`) 구조를 개별 조회.

- **PASS**: edit/delete 아이콘 오배선 재발 없음 — Table Row 6행(With Data) + 사이드바 카테고리 관리 4행×2화면=8행, 총 14곳 전부 `get_design_context`로 개별 확인: edit-action은 흰 bg+연필 아이콘(Icon/Edit 비주얼), delete-action은 coral bg(`#ff5a76`)+IconDelete 컴포넌트로 서로 다르게 렌더링. 스크린샷 교차 확인도 일치. 이전 "Danger variant가 Icon/Edit를 잘못 참조" 버그 재발 없음.
- **PASS**: 검색 Input(`177:499`) — Icon/Search 실제 노출 확인(스크린샷), 높이 38px(metadata: width 1072 height 38, Default 31px 대비 확장 반영), Search Row(`153:443`) 내 버튼과 시각적 정렬 정상(items-center로 검색/전체 버튼과 수직 중심 정렬).
- **PASS**: 헤더 로그아웃(`177:497`/`177:702`) — Content=IconText, Label="로그아웃" 확인. 스크린샷상 teal 배경 위에 아이콘+라벨 정상 렌더링(양쪽 화면 동일). **도구 한계 발견**: `get_design_context`의 코드 출력에서는 icon 슬롯이 빈 `<div>`로만 나와(인스턴스 스왑 오버라이드가 코드 생성에 반영 안 됨) 실제로는 문제없는데도 버그처럼 보일 수 있음 — 이번처럼 코드 출력과 스크린샷을 반드시 병행 확인해야 함(design-system.md의 "알려진 도구 이슈"에 이미 있는 유사 패턴, 이번엔 반대 방향 사례로 추가 참고할 것).
- **PASS(알려진 갭이나 문서화 FAIL)**: Icon/Add — Add Contact Row 필드 5개 실측(140+150+588+180+50, gap 12×4, padding 16×2) 합이 정확히 1188px로 컨테이너 폭과 일치, 여유 0 확인 → IconText 전환 시 오버플로우 근거는 실측으로 타당. 그러나 `docs/design/design-system.md` "알려진 갭/이슈" 섹션 전체를 검색해도 Icon/Add 관련 항목이 전혀 없음 — **문서화 누락(FAIL)**.
- **PASS(알려진 갭이나 문서화 FAIL)**: Icon/Category — Sidebar Nav Item 컴포넌트(`103:106`) 구조를 직접 열람한 결과 Label(TEXT)+Badge(Count) 두 슬롯뿐, 아이콘 인스턴스 슬롯 자체가 없음 → "구조 변경 필요" 근거 타당. 이 역시 design-system.md "알려진 갭/이슈"에 기록되어 있지 않음 — **문서화 누락(FAIL)**.
- **문서 정합성 이슈(신규, MEDIUM)**: design-system.md "알려진 갭/이슈"에 "화면상 버튼 색 스왑 미해결... 여전히 ui-designer 후속 작업 대기"라는 줄이 그대로 남아있음. 그러나 이 항목은 지난 재감사(위 2026-07-12 재감사 항목)에서 이미 PASS(해소 확인)로 검증됐고 이번 라운드에서도 스크린샷으로 재확인(teal/amber 정상). 실제 상태와 문서가 어긋남 — design-systems가 [해소됨]으로 갱신 필요.
- **11차 PASS 회귀 재확인 — 전부 PASS, 회귀 없음**: (1) raw 프레임→실제 인스턴스 전환 유지, (2) Row Action Button 44×44 터치 타겟 유지(아이콘 스왑 후에도 outer div size-44 + inner visual px-8/py-4/radius-5/border-1 구조 불변, 테이블 행 내부·사이드바 8곳 전부 재확인), (3) 빈 상태 그래픽(코랄 채움+잉크 스트로크, 확대 스크린샷으로 스트로크 링 직접 확인) 유지, (4) 로고 심볼 노드명 "Logo Symbol" 일관 유지, (5) confirmed 문서 표기(카테고리 추가=teal/연락처 추가=amber) 유지.
- **종합**: HIGH 신규 없음. MEDIUM 3건(Icon/Add·Icon/Category 문서화 누락 2건 + 버튼 색 스왑 해소 문구 미갱신 1건) — 전부 design-systems 담당(문서 갱신), Figma 화면 자체의 결함 아님. 11차 PASS 전항목 회귀 없음.
