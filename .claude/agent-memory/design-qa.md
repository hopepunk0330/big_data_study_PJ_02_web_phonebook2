# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-17 (35차) — Button/NeoBtn Leading Icon 슬롯 신설(34절) + 8지점 적용(ui-designer) 독립 재검증 — 구조/등록 PASS, 적용 지점 2건 HIGH(신규, 이번 라운드 이전부터 있던 마스터 결함이 그대로 화면에 노출)

배경: 34차 HIGH 2건을 design-systems가 `Show Leading Icon`(BOOLEAN)+`Leading Icon`(INSTANCE_SWAP) 프로퍼티 신설로 정정하고, ui-designer가 8개 지점에 적용한 라운드에 대한 독립 재검증.

**PASS — 컴포넌트 구조(60 variant 전체), Pixel/ArrowRight·ArrowEnter 비파괴 추출, Join/login/main-수정 5지점, login "회원가입" detach 재현 정확도**: 상세는 이전 로그 참고.

**HIGH(신규, 지정 범위 밖에서 발견) — NeoBtn Style=Sky 텍스트 색이 확정 원본과 다름**: 마스터(`712:2`) 기본값이 `color/ink-900`(검정)에 바인딩돼 있으나 확정 원본(`501:6423`)은 흰색. **(36차에서 정정 완료)**

**HIGH(신규, 지정 범위 밖에서 발견) — NeoBtn Style=Sky/Navy 마스터 둘 다 확정 원본에 있는 2px ink 보더가 없음**. **(36차에서 정정 완료)**

**종합**: 슬롯 신설·아이콘 등록·8지점 중 6곳 PASS. HIGH 2건(NeoBtn Sky/Navy 마스터 텍스트색/보더 결함)은 36차에서 정정 완료.

### 2026-07-17 (36차) — NeoBtn Sky/Navy 2px ink 보더 추가 + Sky 텍스트 재바인딩(35차 HIGH 2건 후속 정정) 독립 재검증 — PASS(지정 4항목 전부), 텍스트색 판정은 보류 기록만

**재검증 범위 1~4(Sky/Navy 12 variant 전수, FocusRing 비충돌, 인스턴스 반영, Component Specs 일치) 전부 PASS**, 확정 원본 대조 hex 단위 일치 확인.

**정보성 기록(판정 보류) — Sky 텍스트 색상**: 흰색으로 확정 원본과 일치하나 WCAG AA 버튼 라벨 기준(4.5:1) 미달(~3.24:1) 가능성 있어 최종 정책 결정은 사용자 판단 대기.

**종합**: 지정 검증 4항목 전부 PASS. 신규 HIGH/MEDIUM 없음.

### 2026-07-17 (37차) — QA 트랙 A(design-system.md 36~38절) 6개 항목 마감 임박 최종 감사 — MEDIUM 1건 신규(ConfettiFooter 이중 불투명도) + 나머지 5항목 PASS

**PASS — clipsContent 17곳, NeoBtn/Button Sky·Coral 텍스트·보더, 흰색 토큰 184개 리바인딩, Table 높이, CategoryManage 유령공간, CountPillText 컬러**: 전부 스팟체크 재조회 결과 문서 기재값과 정확히 일치.

**PASS — BgPixels 다이아몬드/십자 불투명도**: `936:976` 9개 요소 순환 배정 정확 확인.

**MEDIUM(신규) — ConfettiFooter 개별 요소 불투명도 0.25 정정은 정확하나 부모 프레임 자체도 opacity 0.25를 가지고 있어 실제 합성 결과가 약 0.0625(6.25%)로 렌더링됨**: `936:954`(Join)/`936:1103`(login) 두 곳. brand-guide 7번 스펙("0.25로 통일") 대비 최종 렌더링 값이 스펙과 다름 — design-systems/graphic-designer에게 이중 적용 해소 권고(둘 중 하나만 남기기).

**종합**: HIGH 0건, MEDIUM 1건(ConfettiFooter 이중 불투명도, 시각 임팩트 낮음), 나머지 5개 항목 전부 PASS.

### 2026-07-17 (38차) — 마감 임박 최종 라운드: 934:2 페이지 사용자 직접 색상 수정 검증(A) + 오늘 변경분 전체(B) 감사 — HIGH 3건(신규) + MEDIUM 2건(신규) + PASS 다수

배경: 사용자가 934:2 페이지 확정 3프레임(Join `935:33`/login `936:1042`/login-알림창 `936:1191`)의 컬러를 Figma에서 직접 수정한 직후, 그 페이지 전체(비밀번호 재설정 3프레임 + 배너 2프레임 포함, A구간·읽기전용 검증만)와 오늘 변경된 나머지 화면(B구간, 정상 감사) 전체를 감사. A구간은 절대 수정하지 않고 발견만 보고.

**[A구간] PASS — 색상 값 자체(sky #1395e6/amber #ffce2c/coral #ff5a76)는 Join/login/login-알림창 3곳 모두 확정 원본(`501:4692`/`501:4940`/`501:5188`)과 hex 단위로 정확히 일치**. 배경 그라디언트(원본의 3-layer gradient)도 최상단 레이어가 불투명이라 실제 렌더링은 신규 구현의 flat sky와 동일 — 문제 없음.

**[A구간] HIGH(신규) — Join "로그인으로 돌아가기" 버튼(`936:948`)이 확정 원본(`501:4888`)의 코랄 원형 배지+반전 화살표 장식을 재현하지 못함**: 원본은 흰 버튼 안에 코랄 20px 원형 배지(2px ink 보더)를 넣고 그 안에 14px 화살표를 180도 회전+세로 반전시켜 "뒤로" 방향을 표현하지만, 신규 구현은 배지 없이 Button/Neutral 컴포넌트에 평범한 PixelArrowRight(정방향, "가입하기"와 동일 아이콘)만 배치해 장식과 방향성이 모두 소실됨. 이 결함은 Button 컴포넌트 자체에 배지 슬롯이 없어서 생긴 시스템 전체 결함으로, Join 화면뿐 아니라 비밀번호 재설정 3프레임(`995:303`/`996:376`/`996:2575`/`996:2713`)의 동일 버튼에도 전부 동일하게 나타남. **(2026-07-17 39차에서 정정 완료 확인 — 신규 node id 1043:9/1043:3229/1043:3237/1043:3245/1043:3251로 재조립되어 코랄 20px 배지+2px ink 보더+반전 화살표 5곳 전부 재현됨)**

**[A구간] HIGH(신규) — login-알림창(`936:1191`) 카드 내부 버튼이 형제 화면 login(`936:1042`)과 불일치**: login-알림창의 "로그인" 버튼은 Leading Icon이 없고(login 화면은 화살표 아이콘 있음), "회원가입" 버튼은 코랄 배지+Plus 아이콘이 없이 텍스트만 있음(login 화면은 `959:307`처럼 코랄 배지+PixelPlus 정상 배치). 35차의 "Button/NeoBtn Leading Icon 슬롯 8지점 적용" 롤아웃 때 login-알림창의 detached 카드는 적용 대상 목록에 없어 누락된 것으로 추정. **(2026-07-17 39차에서 정정 완료 확인 — "로그인" 버튼 Leading Icon 정상, "회원가입" 버튼(신규 node `1044:38`) 코랄 배지+PixelPlus 정상, login(`936:1042`)과 완전히 동일)**

**[A구간] MEDIUM(신규, 확인 필요) — CornerInput Disabled 배경 토큰과 Button Disabled 배경 토큰이 같은 이름(`color/bg-disabled`)인데 실제 렌더링 hex가 다름**: 비밀번호 재설정 성공 화면(`996:2575`)의 아이디 필드 Disabled는 `var(--color-bg-disabled,#bbb)`로 렌더링되나, design-system.md에 기록된 Button Disabled의 `color/bg-disabled`는 `#929292`. 같은 토큰명이 다른 실제 값으로 나온다면 변수 바인딩 혼선(또는 codegen 캐시 이슈)이니 design-systems가 실제 변수 정의를 재확인 필요. **(39차에서는 재검증 범위 밖 — 미확인 상태 유지)**

**[B구간] HIGH(신규) — 연락처 삭제 모달(`941:1508`)이 확정 원본(`501:4172`)과 여러 치수에서 어긋남**: SummaryBox 행간격 20px(원본 24px, 4px 부족), 카드 전체 높이 378px(원본 392px, 14px 부족), ButtonRow y=292/높이46(원본 y=308/높이48), 버튼 높이 42px(원본 44px). WarningBox 자체(392×74)는 원본과 정확히 일치해 사용자가 지시한 "경고배너 정정"은 잘 됐으나, 그 아래 요약 박스·버튼 행이 함께 눌린 것으로 보임. **(39차 재검증 결과: 카드 높이 392px·SummaryBox 행간격 24px 두 항목은 정정 완료 확인, 그러나 버튼 높이는 여전히 42px로 미정정 — 아래 39차 로그 참고)**

**[B구간] MEDIUM(신규) — 모달 시스템 전반의 Button 높이가 42px로, 확정 원본의 44px보다 낮고 4px 그리드에서도 벗어남(42/4=10.5)**: `941:1508`뿐 아니라 신규 모달 `1001:1594`(카테고리 삭제 확인)·`1002:1611`(카테고리 이름 수정)에도 동일하게 Button height=42/ButtonRow height=46이 쓰여 시스템 전반의 패턴으로 확인됨(Button 컴포넌트의 padding 12+텍스트 line-height 18+padding 12=42 자연 hug 결과로 추정). WCAG 44×44 최소 터치 타겟 권장값에 2px 못 미침 — token-architecture-guide의 "padding+hug 높이" 원칙 자체는 지켜지고 있으나 원본 44px과의 괴리가 있어 design-systems 확인 필요. **(39차에서도 미해결 확인, 아래 참고)**

**[B구간] PASS — 메인 오류배너(`996:3165`) Toast 오버레이 위치**: `x=474,y=93,w=812,h=44`로 확정 원본 main-알림창(`501:6548`)의 Message Banner와 좌표까지 정확히 일치. 검색행 버튼 일부가 배너 아래로 살짝 보이는 것도 원본과 동일한 의도된 오버랩(신규 버그 아님).

**[B구간] PASS — FieldRow/SearchRow 레이아웃 붕괴 해소 확인(스팟체크 각 1곳)**: `939:356`(FieldRow)/`938:340`(SearchRow) 자식 간 8px gap·전체 폭 모두 정상, 겹침 없음.

**[B구간] PASS — CategoryManage CatRow 폭 168px 확정(스팟체크 `937:1178`)**: 39차 정정 그대로 유지, 라벨/버튼 분리 확인.

**[B구간] PASS — Coral Button(`941:3043`, "삭제하기") 보더/텍스트**: `border-2 border-[var(--color-ink-900)]` + `text-[color:var(--color-text-inverse,white)]` 확인, 36차 정정 유지.

**[A구간] PASS — 비밀번호 표시/숨김 토글(Pixel/Eye) `996:376`에 정상 배치**: 새 비밀번호/비밀번호 확인 두 필드 모두 아이콘 확인.

**종합**: HIGH 3건(신규 — Join 로그인으로 돌아가기 배지 소실 시스템 결함, login-알림창 카드 아이콘/배지 롤아웃 누락, 연락처 삭제 모달 치수 다수 불일치) + MEDIUM 2건(신규 — 모달 Button 높이 42px 시스템 패턴, Disabled 토큰명 동일·값 상이 의심) + PASS 다수(색상 값 자체, Toast 위치, FieldRow/SearchRow, CategoryManage, Coral Button, 비밀번호 토글). **A구간 자체는 무수정** — 위 3건 중 2건(로그인으로 돌아가기 배지, login-알림창 아이콘 누락)은 A구간에서 발견됐으나 원인은 A구간 밖의 컴포넌트/조립 결함이라 design-pl이 사용자에게 "A프레임 자체는 이번에 안 건드렸고, 색상 수정은 정확했다"는 점과 함께 명확히 전달해야 함.

### 2026-07-17 (39차, 마감 임박 최종 라운드) — 38차 HIGH 3건 중 4건 재확인 지시(삭제모달 치수/코랄배지 5곳/login-알림창 버튼/NeoBtn Neutral 그림자) 독립 재검증 — HIGH 1건 잔존(삭제모달 버튼 높이) + PASS 3건 + LOW 2건(신규, 문서/네이밍 stale)

배경: 마감 임박으로 38차 HIGH 3건 중 정정 지시된 항목만 좁게 재확인. 934:2 페이지 색상 구간 자체는 이번 재검토 대상에서 제외(이미 38차에서 PASS 확정).

**부분 PASS/HIGH 잔존 — 연락처 삭제 모달(`941:1508`) vs 확정 원본(`501:4172`) 치수 재실측**: SummaryBox 행간격(row pitch) 24px로 정정 확인(4px gap + 20px row = 24px, 원본과 동일 패턴) — PASS. 카드 전체 높이 392px로 정정 확인(원본과 정확히 일치) — PASS. **그러나 ButtonRow 내 두 버튼(`941:3043`/`941:3045`) 실제 인스턴스 높이는 여전히 42px(원본 44px) — 지시된 "버튼 높이 44px 정정"이 반영되지 않음.** ButtonRow 자체는 y=308/h=48로 원본과 일치하나, 그 안의 버튼만 4px 여백을 남기고 42px로 남아 WCAG 44×44 최소 터치 타겟에 2px 미달. 38차 MEDIUM(모달 시스템 전반 Button 42px 패턴)과 동일 원인 — 아직 해소 안 됨. **HIGH로 재상향**(명시적 정정 지시 후에도 미해결 + 접근성 기준 미달).

**PASS — 코랄 원형 배지+반전 화살표 5개 지점**: node id가 세션 중 재조립되며 이동함(`936:948`→`1043:9`, `995:2485`→`1043:3229`, `996:409`→`1043:3237`, `996:2614`→`1043:3245`, `996:2753`→`1043:3251` — 각각 부모 프레임 `935:33`/`995:303`/`996:376`/`996:2575`/`996:2713` 안에서 재확인). 5곳 모두 코랄 20px 원형 배지(2px ink 보더)+PixelArrowRight 조합이 화면에서 반전(좌향) 방향으로 정상 렌더링됨, `501:4888` 원본과 시각적으로 일치 — PASS.

**PASS — login-알림창(`936:1191`) 버튼 vs login(`936:1042`)**: "로그인" 버튼(Leading Icon 포함)·"회원가입" 버튼(코랄 Plus 배지 포함, 신규 node `1044:38`, description에 "원본 936:1042/959:307과 동일" 명시) 둘 다 login과 완전히 동일한 구성으로 확인 — PASS.

**PASS — Button 컴포넌트셋 Style=Neutral(`259:607`) NeoPop 그림자**: `259:603`(Amber)과 동일한 `drop-shadow-[var(--shadow-offset-hard-2,2px)_var(--shadow-offset-hard-2,2px)_calc(var(--shadow-blur-none,0px)/2)_var(--shadow-color-ink-solid,#1a1a1a)]` 그림자가 그대로 적용됨 — offset/color 전부 토큰 바인딩(하드코딩 없음), 두 스타일 완전 동일 — PASS.

**LOW(신규) — Button 컴포넌트(`259:609`) description이 여전히 "Neutral=취소류 보조 액션(흰 배경+ink 보더, 그림자 없음)"이라고 적혀있어, 방금 확인한 실제 적용(그림자 있음)과 문서 내용이 모순**: description 텍스트만 stale — design-systems가 그림자 적용 결정에 맞춰 description 문구("그림자 없음"→"2px 하드 그림자, Amber/Coral과 동일")를 갱신 필요.

**LOW(신규) — 코랄 배지 버튼 5곳 중 3곳(`1043:3229`/`1043:3237`/`1043:3251`)의 텍스트 레이어 내부 이름이 실제 렌더링 문구("로그인으로 돌아가기")와 다르게 "저장하기"로 남아있음**: 시각적 렌더링에는 영향 없음(레이어 name 속성만 stale, 실제 text content는 정상) — 컴포넌트 복제 시 이름을 안 바꾼 흔적으로 추정, 추후 레이어 정리 때 함께 정정 권고.

**종합**: HIGH 1건(연락처 삭제 모달 버튼 높이 42px, 정정 지시 후에도 미해결 — 재작업 필요) + PASS 3건(코랄 배지 5곳, login-알림창 버튼 동일화, NeoBtn Neutral 그림자) + LOW 2건 신규(Button description 문구 stale, 코랄배지 버튼 3곳 레이어명 stale). SummaryBox 행간격·카드 높이는 정정 완료로 확인(부분 PASS).
