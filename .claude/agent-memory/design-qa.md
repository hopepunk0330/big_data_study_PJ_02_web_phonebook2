# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-13 (3라운드 최종 재감사) — 컴포넌트 레벨 수정(design-systems) + 파일럿 3화면 반영(ui-designer) 검증

- **PASS**: edit/delete 아이콘 오배선 재발 없음(14곳 전수 확인). 검색 Input 아이콘/높이 정상. 헤더 로그아웃 IconText 정상.
- **MEDIUM(문서화 누락, design-systems 담당)**: Icon/Add·Icon/Category 미사용 근거는 실측상 타당하나 design-system.md "알려진 갭"에 미기록. 버튼 색 스왑 "미해결" 문구가 실제로는 이미 해소됐는데 문서 갱신 안 됨.
- **종합**: HIGH 신규 없음. MEDIUM 3건(전부 문서 갱신 이슈, 화면 자체 결함 아님).

### 2026-07-13 — 사용자 확정 8개 프레임 기반 토큰/컴포넌트 1차 추출 감사

fileKey `zgGlMBwFglaDlaeyP4CkgR`. B-2 파일럿을 완전히 대체한 사용자 확정 8개 프레임(부모 `248:11689`)과 design-systems가 그로부터 추출한 design-system.md 1~7절(신규) 대조.

- **HIGH 6건**: 사이드바 비활성 nav 텍스트 대비 미달(≈2.5:1), "CATEGORY"/"카테고리 관리" 라벨 대비 미달(≈2.9:1), Table Row Action teal/coral 텍스트 대비 미달(≈3.0~3.1:1), TypeSelector 등록값이 원본과 불일치(보더/텍스트 색), Table Row Action 텍스트 크기 13px(원본 10px), 터치 타겟 44×44 미달 다수(문서화 누락).
- **MEDIUM 1건**: Row Action Button Neutral 보더가 `#1c1f21`이 아니라 ink-900(#1a1a1a)에 흡수됨.
- **PASS**: 사이드바 teal 풀블리드/로고 스펙, CatBadge 4종 토큰 바인딩, 알림 오버레이 배치, 뮤트 텍스트 3종 계산 재확인.
- **후속**: 위 HIGH 6건 + MEDIUM 1건은 이후 라운드(0-1절 design-systems 정정)에서 전부 hex 단위 재확인·해소됨(design-system.md 0-1절 참고). 터치 타겟 4건은 사용자가 "이번 프로젝트 범위에서 개선하지 않음"으로 명시적 확정(design-system.md 7-1절 RESOLVED) — 더 이상 열린 이슈 아님.

### 2026-07-14 — 신규 산출물 3종 감사: Pixel/Eye 아이콘, 인터랙션 상태(Hover/Press/Focus/Disabled/Loading), 라벨링

fileKey 동일. (1) Icons 페이지 신규 `Pixel/Eye`(`281:405`)와 `Pixel/Star`(`255:11`) description 정정, (2) interaction-designer가 NeoBtn/Button/Icon Button/Row Action Button/Table Row Action(`259:126`/`259:609`/`259:613`/`260:95`/`260:100`)에 추가한 State축과 Sidebar Nav Item/TypeSelector/NeoInput/CornerInput(`258:29`/`257:28`/`288:12`/`288:27`)에 추가한 Focus축, (3) 파일럿 3개(`153:19`/`153:373`/`153:547`)·old-사용하지말것 7개(`242:2330`)·확정 8개(`248:11689`)·legacy 5개(`100:46`/`101:64`/`102:65`/`103:7`/`104:108`) 라벨링을 감사.

- **HIGH(신규)**: `Sidebar Nav Item`(`258:29`)의 `State=Inactive, Focus=Yes`(`287:17`) — Focus 링 효과가 레이어에는 있으나 실제 렌더 시 `drop-shadow(0px 0px 0px #1a1a1a)`(오프셋·블러·스프레드 전부 0, 완전히 비가시)로 나타남. 스크린샷 바운딩박스로 교차검증: Focus=No(`258:23`) 173×40, Focus=Yes(`287:17`) 173×40 — **성장 0, 링 없음**. 반면 같은 컴포넌트의 `State=Active,Focus=Yes`(`287:14`)는 175×42→179×46로 성장, TypeSelector/NeoInput/CornerInput/NeoBtn/Button/Icon Button/Row Action Button/Table Row Action의 Focus 변형은 전부 +6px(각 변 +3px) 성장 확인(각 컴포넌트 Default↔Focus 스크린샷 페어 비교, 8쌍 전수 확인) — Sidebar Nav Item Inactive만 예외적으로 링이 렌더링되지 않음. 카테고리 nav 항목 중 보통 3~4개가 Inactive 상태이므로, 키보드 탭 포커스 시 대부분의 사이드바 항목에서 포커스 인디케이터가 완전히 보이지 않는 WCAG 2.4.7 위반. design-system.md 9-1절 "모든 컴포넌트·모든 색상이 동일한 ink 링을 공유" 원칙과도 배치.
- **HIGH(신규)**: Disabled 상태 `opacity=0.45`(컴포넌트 전체, bg+텍스트 동일 비율로 배경에 블렌딩)가 WCAG 대비를 심각하게 훼손함 — 직접 계산: NeoBtn Style=Teal Disabled를 흰 페이지 배경 위에 렌더링 시 텍스트(ink #1a1a1a→약 rgb(152,152,152))와 배경(teal #17a398→약 rgb(151,214,209)) 대비 **≈1.76:1**(AA 4.5:1 대비 크게 미달). 가장 유리한 경우인 Neutral 스타일(흰 배경+ink 텍스트, 배경이 페이지와 동색이라 배경 자체는 안 흐려짐)도 텍스트만 흐려져 **≈2.89:1**로 여전히 미달(큰 텍스트 3:1 기준도 근소 미달). NeoBtn/Button/Icon Button/Row Action Button/Table Row Action 5개 컴포넌트 전부 동일 규칙(9-1절)이라 구조적으로 전체 Disabled variant(38개)에 재현됨. 원본 8개 확정 프레임에는 애초에 Disabled 상태가 없어 사용자의 7-1절 RESOLVED 결정(원본에 내재된 대비 미달 5건) 대상이 아닌 **이번 라운드에 새로 도입된, 아직 아무도 검토하지 않은 결함**이다. design-system.md 9절/9-4절 "알려진 갭"에 전혀 언급 없음 — 문서화도 누락.
- **PASS(확인)**: `Pixel/Eye`(`281:405`) — 원본 login 프레임의 `PixelEye`(`247:6814`)와 정확히 동일한 14×10 크기, 문서상 비파괴적 clone 방식(createComponentFromNode, 원본 무수정)이라 형태·색상도 구조적으로 동일. description도 정확("비밀번호 표시/숨김 토글 마이크로 아이콘(14x10px)"). `Pixel/Star`(`255:11`) description이 "잉크 #1a1a1a"로 정확히 정정됨 확인.
- **PASS(확인)**: 라벨링 — 파일럿 3개(`153:19`/`153:373`/`153:547`) 전부 "❌ 미채택 — " 정확히 부착. 사용자 확정 8개 프레임 중 5개가 원본 라벨 그대로 무수정 보존. Legacy 5개 전부 "[Legacy B-2] " 접두사 정확히 유지.
- **종합**: HIGH 2건(신규, Focus 링 미렌더링·Disabled 대비 붕괴 — 둘 다 interaction-designer 담당, 원본 8프레임 무관한 신규 설계 결함) + LOW 1건(감사 커버리지 갭, 재현 필요) + PASS 다수. 다음 감사 시 HIGH 2건의 수정 여부 최우선 확인.

### 2026-07-14 — "old-사용하지말것" 7개 프레임 라벨 재검증(직전 라운드 LOW 커버리지 갭 해소)

fileKey 동일. 직전 라운드에서 토큰 한계로 검증 못 한 `242:2330` 하위 7개 프레임(`242:2331`/`242:2814`/`242:3089`/`242:3294`/`242:3380`/`242:3691`/`242:4002`)을 개별 nodeId로 `get_metadata` 호출(페이지 전체 조회 대신 노드 단위 조회로 토큰 문제 회피)해 `name` 속성을 문자열 단위로 확인.

- **PASS(확인, LOW 재현 해소)**: 7개 전부 `❌ 미채택 — Document`로 정확히 일치(이모지+공백+em dash+공백 접두사, 원래 이름 Document 보존). 오타·누락 없음.
- **PASS(확인)**: 사용자 확정 8개 프레임(부모 `248:11689`)이 이 7개 프레임 하위 트리에 혼입되어 있지 않음.
- **종합**: 직전 라운드 LOW 1건(라벨링 검증 미완료) 완전 해소. 신규 결함 없음. 직전 라운드 HIGH 2건(Sidebar Nav Item Inactive Focus 링 미렌더링, Disabled opacity 대비 붕괴)은 이번 세션 범위 밖 — 다음 감사에서 우선 확인 필요.

### 2026-07-14 (4차) — Legacy 컴포넌트 해제 7건 + CornerInput 브래킷 제거 + 문서 동기화 감사

fileKey 동일. 이번 라운드 3가지 변경사항 감사: (1) Legacy 컴포넌트 7개 COMPONENT/COMPONENT_SET→FRAME 전환(`314:843`/`314:319`/`314:876`/`314:879`/`314:893`/`314:897`/`314:902`) + Table Row(`103:7`) 해제 보류 상태, (2) CornerInput(`261:12`/`288:13`) 브래킷 제거, (3) `docs/design/graphic-assets.md`·`docs/design/design-system.md`와 Figma 실제 상태(`90:2` 삭제, `96:7` 아이콘 18종) 동기화. 직전 라운드 HIGH 2건(Focus 링 미렌더링/Disabled 대비)은 이번 라운드 감사 지시 범위 밖이라 재검증하지 않음 — 다음 감사에서 확인 필요.

- **PASS**: 7개 전환 전부 확인 — 신규 FRAME 루트가 `<frame>` 태그이고 자식도 전부 `<frame>`/`<text>`/`<instance>`(COMPONENT_SET이라면 variant 자식이 `<symbol>` 태그로 나와야 함 — 대조군으로 확인 중인 CatBadge `256:17`은 실제로 자식이 `<symbol>`로 나옴, 전환된 7개는 그렇지 않음). 스크린샷 대조 결과 시각 내용 손실 없음(Button 32종 그리드, Row Action Button 2종, Sidebar Nav Item 2종, Input 4종, Select 3종, Badge 4종, Alert 2종 전부 정상 렌더링). 기존 COMPONENT_SET ID(`97:47`/`100:46` 직접 조회) "not found" 확인 — 완전 삭제, 고아 노드 없음.
- **PASS**: Table Row(`103:7`) — COMPONENT_SET이 아니라 단일 COMPONENT(variant 없음, `<symbol>` 태그)로 미해제 상태 그대로 유지 확인. 인스턴스 7개(`103:77`/`110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290`) 전수 조회 — 전부 정상 인스턴스로 존재, 깨짐/고아 참조 없음.
- **PASS**: CornerInput(`261:12`/`288:13`) — CornerBracket 노드 완전 제거 확인(자식은 placeholder 텍스트뿐), 순수 2px ink 사각 보더+radius 0, 스크린샷상 확정 프레임(`247:6801` 등)과 동일한 형태. 폭 392px 유지 확인. 부모 ComponentSet(`288:27`) description에 리사이즈 방침("로그인/가입은 인스턴스 리사이즈로 대응") 명시 확인.
- **MEDIUM(신규)**: CornerInput 개별 variant 노드(`261:12` "Focus=No", `288:13` "Focus=Yes") description이 갱신되지 않고 구 스펙("네 모서리 8x8 ㄱ자 브래킷(2px ink)... NeoInput과 혼용 금지")을 그대로 유지 — 실제 시각 상태(브래킷 없음) 및 부모 ComponentSet(`288:27`)의 정정된 description("모서리 브래킷 장식 없음 — 확정 프레임 실측 결과 없는 걸 확인해 제거함")과 모순. `get_design_context`로 컴포넌트를 소비하는 에이전트/개발자가 개별 variant description을 읽으면 브래킷을 다시 추가해야 한다고 오인할 위험이 있음. 개별 variant description도 부모와 동일하게 갱신 필요(design-systems 담당).
- **PASS**: 문서-Figma 동기화 — Graphic Assets 페이지(`90:2`) 직접 nodeId 조회 결과 "not found" 확인(목록 누락이 아니라 실제 삭제 확인, house rule 0번 절차 준수). Icons 페이지(`96:7`) 실측 결과 Icon/* 8종(`96:12`/`96:17`/`96:22`/`96:27`/`96:31`/`96:36`/`96:41`/`96:45`)+Pixel/* 10종(`255:11`/`255:26`/`255:30`/`255:43`/`255:62`/`255:104`/`255:107`/`255:120`/`255:149`/`281:405`) 총 18개, `docs/design/graphic-assets.md`·`docs/design/design-system.md` 4절 기재 내용과 nodeId 단위로 정확히 일치.
- **종합**: HIGH 0건. MEDIUM 1건(CornerInput 개별 variant description 미갱신 — 시각적 결함 아님, 문서/description 일관성 이슈). Legacy 해제 작업과 문서 동기화는 전부 정확했음.
